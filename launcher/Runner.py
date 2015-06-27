__author__ = 'Tails'

from openpyxl import load_workbook
from testCases.TestCaseConfig import TestCaseConfig

class Runner:

    def __init__(self):
        pass

    def run(self):
        dicConfig = self.getConfigDic('config/config.xlsx')
        lstAllTestCaseConfig = self.getAllTestCases('config/Automation_Test_Suite.xlsx')
        for testCaseConfig in lstAllTestCaseConfig:
            exec 'from testCases.%s.%s import %s' % (testCaseConfig.moduleName, testCaseConfig.testCaseID, testCaseConfig.testCaseID)
            testCaseInstance = eval(testCaseConfig.testCaseID)(dicConfig, testCaseConfig)
            testCaseInstance.setUp()
            testCaseInstance.run()
            testCaseInstance.tearDown()


    def getConfigDic(self, fileName):
         wb = load_workbook(filename=fileName, read_only=True)
         #get which env is selected
         envWs = wb.get_sheet_by_name('Env')
         dicEnvConfig = {}
         rowId = 0
         for row in envWs.rows:
             #skip the first row, it's title
             if rowId == 0:
                 rowId += 1
                 continue
             lstCurrCell = []
             for cell in row:
                 lstCurrCell.append(cell.value)
             #insert the config item to the dictionary
             item = lstCurrCell[0]
             value = lstCurrCell[1]
             dicEnvConfig[item] = value
             rowId += 1
         env = dicEnvConfig['Environment']
         dicConfig = {}
         #read all configs in the [env] sheet
         configWs = wb.get_sheet_by_name(env)
         rowId = 0
         for row in configWs.rows:
             #skip the first row, it's title
             if rowId == 0:
                 rowId += 1
                 continue
             lstCurrCell = []
             for cell in row:
                 lstCurrCell.append(cell.value)
             #insert the config item to the dictionary
             item = lstCurrCell[0]
             value = str(lstCurrCell[1])
             dicConfig[item] = value
             rowId += 1
         return dicConfig

    def getAllTestCases(self, fileName):
        """
        :param fileName:
        :return: A list contains all testcase (testCaseConfig) to be run
        """
        lstAllTestCases = []
        lstAllTestCaseConfig = []
        wb = load_workbook(filename=fileName, read_only=True)
        lstSheetNames = wb.get_sheet_names()
        for sheetName in lstSheetNames:
            lstCurrSheetTestCases = []
            ws = wb[sheetName]
            currTestCase = []
            for row in ws.rows:
                currTestCase = []
                currTestCase.append(sheetName)
                for cell in row:
                    currTestCase.append(cell.value)
                if currTestCase[3] == 'Run':
                    lstCurrSheetTestCases.append(currTestCase)
            if len(lstCurrSheetTestCases) > 0:
                lstAllTestCases += lstCurrSheetTestCases
        for testCase in lstAllTestCases:
            currTestCaseConfig = TestCaseConfig(testCase[0], testCase[1], testCase[2])  #sheetName, moduleName, testCaseID
            lstAllTestCaseConfig.append(currTestCaseConfig)
        return lstAllTestCaseConfig