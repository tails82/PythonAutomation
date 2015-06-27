__author__ = 'Tails'

from abc import ABCMeta, abstractmethod

class AbstractBaseTestCase:

    __metaclass__ = ABCMeta

    def __init__(self, dicConfig, testCaseConfig):
        self.dicConfig = dicConfig
        self.testCaseConfig = testCaseConfig

    def setUp(self):
        print 'setUp...'

    def tearDown(self):
        print 'tearDown...'

    @abstractmethod
    def run(self):
        pass