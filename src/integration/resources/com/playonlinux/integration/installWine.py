from com.playonlinux.integration import ServiceManagerGetter
from com.playonlinux.framework import SetupWizard, WineInstallation
from com.playonlinux.contexts import WineVersionServicesContext
from com.playonlinux.framework import Environment

from java.lang import Class

import unittest, time, os
from com.playonlinux.core.utils import OperatingSystem


class TestExample(unittest.TestCase):
    def setUp(self):
        ServiceManagerGetter.serviceManager.init(WineVersionServicesContext())

    def testInstallWineVersion(self):
        setupWizard = SetupWizard("Mock setup wizard")
        setupWizard.init()

        wineVersionManager = ServiceManagerGetter.serviceManager\
            .getService(Class.forName("com.playonlinux.engines.wine.WineVersionManager"))

        while(wineVersionManager.isUpdating()):
            print "Updating wine version list..."
            time.sleep(2)

        wineInstallation = WineInstallation("1.7.36", "upstream-x86", setupWizard)
        wineInstallation.install()

        print "Checking that wine binary is installed"
        self.assertTrue("%s/engines/wine/upstream-%s-x86/1.7.36/bin/wine" %
                        (os.path.exists(Environment.getUserRoot(),
                            OperatingSystem.fetchCurrentOperationSystem().getNameForWinePackages))
        )


    def tearDown(self):
        ServiceManagerGetter.serviceManager.shutdown()