__author__ = 'Tails'

from pages.AbstractBasePage import AbstractBasePage

class LoginMainPage(AbstractBasePage):

    def __init__(self, driver):
        AbstractBasePage.__init__(self, driver)


    def isTargetPage(self):
        return False

    def initialXPATH(self):
        pass