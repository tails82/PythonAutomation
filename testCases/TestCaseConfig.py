__author__ = 'Tails'

class TestCaseConfig:
    def __init__(self, sheetName, moduleName, testCaseID):
        self.sheetName = sheetName
        self.moduleName = moduleName
        self.testCaseID = testCaseID
        self.testCaseRunResult = 'Passed'
        self.timeElapsedSec = 0
        self.failureMessage = None
        self.failureStackTrace = None