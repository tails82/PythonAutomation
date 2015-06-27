__author__ = 'Tails'

from abc import ABCMeta, abstractmethod
from nose.tools import *
from selenium.common.exceptions import NoSuchElementException

class AbstractBasePage:

    __metaclass__ = ABCMeta

    def __init__(self, driver):
        self.driver = driver
        assert_true(self.isLoad(),self.__class__.__name__ + " is not load!" )

    def isLoad(self):
        try:
            return self.isTargetPage()
        except NoSuchElementException:
            return False

    #This function will be implement by sub class
    @abstractmethod
    def isTargetPage(self):
        pass
