from selenium.webdriver.common import by

__author__ = 'Tails'

from abc import ABCMeta, abstractmethod
from nose.tools import *
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from page_objects import PageObject
import launcher.Logger

class AbstractBasePage(PageObject):

    __metaclass__ = ABCMeta

    def __init__(self, driver):
        #get logger from module Logger
        self.logger = launcher.Logger.logger
        # Don't change the variable name w. it's used by PageObject
        self.w = driver
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

    def isElementDisplayed(self, by, value):
        return self.driver.find_element(by, value).is_displayed()
