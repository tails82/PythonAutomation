__author__ = 'Tails'

from  testCases.AbstractBaseTestCase import AbstractBaseTestCase

class Demo_01_01(AbstractBaseTestCase):

    def __init__(self, dicConfig, moduleName, testCaseID):
        AbstractBaseTestCase.__init__(self, dicConfig, moduleName, testCaseID)

    def run(self):
        print self.testCaseID +  " is runnung..."
        print 'open url: ' + self.dicConfig['Login Site']
        print 'input userName: ' + self.dicConfig['B2B User Name']
        print 'input userName: ' + self.dicConfig['B2B User Password']