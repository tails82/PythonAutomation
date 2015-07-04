__author__ = 'Tails'

from pages.AbstractBasePage import AbstractBasePage
from page_objects import PageElement
from selenium.webdriver.common.by import By

class LoginMainPage(AbstractBasePage):

    txtUserName = PageElement(xpath="//input[@id='username']")
    txtPassword = PageElement(xpath="//input[@id='password']")
    btLogin = PageElement(xpath="//div[@id='loginbtn']")

    def __init__(self, driver):
        self.driver = driver
        AbstractBasePage.__init__(self, driver)

    def isTargetPage(self):
        return self.isElementDisplayed(By.XPATH, "//div[@id='loginbtn']")


    def setUserName(self, userName):
        self.logger.info('setUserName is started')
        self.txtUserName.clear()
        self.txtUserName.send_keys(userName)

    def setPassword(self, password):
        self.txtPassword.clear()
        self.txtPassword.send_keys(password)

    def clickLoginButton(self):
        self.btLogin.click()