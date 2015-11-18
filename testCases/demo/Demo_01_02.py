from hamcrest import assert_that, equal_to

__author__ = 'Tails'

from testCases.AbstractBaseTestCase import AbstractBaseTestCase

class Demo_01_02(AbstractBaseTestCase):

    def __init__(self, dicConfig, testCaseConfig):
        AbstractBaseTestCase.__init__(self, dicConfig, testCaseConfig)

    def run(self):
        print self.testCaseConfig.testCaseID +  " is runnung..."
        print 'open url: ' + self.dicConfig['Login Main Site']
        print 'input userName: ' + self.dicConfig['B2B User Name']
        print 'input userName: ' + self.dicConfig['B2B User Password']
        assert_that(True, equal_to(False))