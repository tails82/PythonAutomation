__author__ = 'Tails'

import os
from abc import ABCMeta, abstractmethod
from selenium import webdriver

class AbstractBaseTestCase:

    __metaclass__ = ABCMeta

    def __init__(self, dicConfig, testCaseConfig):
        self.dicConfig = dicConfig
        self.testCaseConfig = testCaseConfig

    def setUp(self):
        #Set initial test case pass/fail status
        self.allPassed = True
        self.initialWebDriver()

    def tearDown(self):
        self.closeBrowser()

    @abstractmethod
    def run(self):
        pass

    def initialWebDriver(self):
        dicConfig = self.dicConfig
        browser = dicConfig['Browser']
        if browser == 'Firefox':
            self.driver = webdriver.Firefox()
        elif browser == 'Chrome':
            self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(self.dicConfig['Implicitly Wait Time'])
        self.driver.set_page_load_timeout(self.dicConfig['Page Load Time'])

    def closeBrowser(self):
        self.driver.delete_all_cookies()
        self.driver.quit()

    def saveScreenShot(self):
        currDir = os.getcwd()
        failedScreenShotDir = currDir + os.path.sep + self.dicConfig['Failed Screenshot Folder']
        fileName = self.testCaseConfig.moduleName + "_" + self.testCaseConfig.testCaseID + ".jpg"
        fullFilePathName = failedScreenShotDir + os.path.sep + fileName
        self.driver.get_screenshot_as_file(fullFilePathName)