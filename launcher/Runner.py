__author__ = 'Tails'

from openpyxl import Workbook
from openpyxl import load_workbook
from testCases.TestCaseConfig import TestCaseConfig
import sys
import traceback
import time
import os

class Runner:

    def __init__(self):
        self.lstRunResult = []

    def run(self):
        dicConfig = self.getConfigDic('config/config.xlsx')
        lstAllTestCaseConfig = self.getAllTestCases('config/Automation_Test_Suite.xlsx')
        for testCaseConfig in lstAllTestCaseConfig:
            exec 'from testCases.%s.%s import %s' % (testCaseConfig.moduleName, testCaseConfig.testCaseID, testCaseConfig.testCaseID)
            testCaseInstance = eval(testCaseConfig.testCaseID)(dicConfig, testCaseConfig)
            try:
                testCaseInstance.setUp()
                testCaseInstance.run()
            except Exception as ex:
                #save screen shot when failed
                testCaseInstance.saveScreenShot()
                testCaseInstance.allPassed = False
                testCaseConfig.testCaseRunResult = "Failed"
                traceback.print_exc(file=sys.stdout)
            finally:
                testCaseInstance.tearDown()
                self.saveTestResult(testCaseConfig)
        self.outputResult(testCaseInstance)

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

    def saveTestResult(self, testCaseConfig):
        tupleRunResult = (testCaseConfig.sheetName, testCaseConfig.moduleName, testCaseConfig.testCaseID, testCaseConfig.testCaseRunResult)
        self.lstRunResult.append(tupleRunResult)

    def outputResult(self, testCaseInstance):
        """
        Write test case run result(pass, failed) to excel file
        :param lstTestResult:
        :return:
        """
        #create a folder with timestamp to save current test run result
        currDateTime = time.strftime("%Y%m%d%H%M%S",time.localtime(time.time()))
        currDir = os.getcwd()
        runResultDir = currDir + os.path.sep + testCaseInstance.dicConfig['Test Result Folder'] + os.path.sep +  currDateTime
        os.mkdir(runResultDir)

        #create excel file and write test result in
        resultFileName = runResultDir + os.path.sep + 'RunResult.xlsx'
        wb = Workbook()
        previousCaseSheetName = ''
        rowIndex = 0;
        for runResult in self.lstRunResult:
            #runResult (sheetName, moduleName, testCaseID, runResult)
            currCaseModuleName = runResult[0]
            #first sheet
            if previousCaseSheetName == "":
                ws = wb.active
                ws.title = currCaseModuleName
            #start another sheet
            elif not previousCaseSheetName == currCaseModuleName:
                ws = wb.create_sheet(title=currCaseModuleName)
                #reset row index in a new sheet
                rowIndex = 0
            rowIndex += 1
            ws['A' + str(rowIndex)] = runResult[1]
            ws['B' + str(rowIndex)] = runResult[2]
            ws['C' + str(rowIndex)] = runResult[3]
            previousCaseSheetName = currCaseModuleName
        wb.save(filename=resultFileName)