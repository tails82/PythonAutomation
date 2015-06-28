__author__ = 'Tails'
import os
from testCases.AbstractBaseTestCase import AbstractBaseTestCase
from pages.LoginMainPage import LoginMainPage

class PL40_01_01(AbstractBaseTestCase):

    def __init__(self, dicConfig, testCaseConfig):
        AbstractBaseTestCase.__init__(self, dicConfig, testCaseConfig)

    def run(self):
        self.driver.get(self.dicConfig['Login Main Site'])
        loginMainPage = LoginMainPage(self.driver)
