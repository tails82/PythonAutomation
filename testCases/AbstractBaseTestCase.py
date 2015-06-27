__author__ = 'Tails'

from abc import ABCMeta, abstractmethod

class AbstractBaseTestCase:

    __metaclass__ = ABCMeta

    def __init__(self, dicConfig, moduleName, testCaseID):
        self.dicConfig = dicConfig
        self.moduleName = moduleName
        self.testCaseID = testCaseID

    def setUp(self):
        print 'setUp...'

    def tearDown(self):
        print 'tearDown...'

    @abstractmethod
    def run(self):
        pass