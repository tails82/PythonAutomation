__author__ = 'Tails'

from testCases.AbstractBaseTestCase import AbstractBaseTestCase
from pages.LoginMainPage import  LoginMainPage

class Demo_01_01(AbstractBaseTestCase):

    def __init__(self, dicConfig, testCaseConfig):
        AbstractBaseTestCase.__init__(self, dicConfig, testCaseConfig)

    def run(self):
        print self.testCaseConfig.testCaseID +  " is runnung..."
        loginUrl = self.dicConfig['Login Main Site']
        loginUserName = self.dicConfig['B2B User Name']
        loginPassword = self.dicConfig['B2B User Password']
        self.driver.get(loginUrl)
        loginMainPage = LoginMainPage(self.driver)
        loginMainPage.setUserName(loginUserName)
        loginMainPage.setPassword(loginPassword)
        loginMainPage.clickLoginButton()
        self.driver.find_element_by_xpath()