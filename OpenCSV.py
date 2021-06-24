'''
Open csv file which contains the information of PR.
'''
import os
import re
import csv

HeaderName = {
    "使用成本中心":"CostCenter",
    "廠商名稱":"VendorName",
    "自組設備":"MachineNumber",
    "財務專案":"ProjectCode",
    "申請事由":"Reason",
    "備註":"Comment",
    "廠區":"Organization",
    "需求日期":"NeedDate",
    "報價單":"Quotation",
    "其他":"Others",
    "類別":"Category"}

class OpenCSV():
    def __init__(self, FilePath):
        self.__FilePath = os.path.normpath(FilePath)
        self.__dictData = {}

    def OpenFile(self):
        with open(self.__FilePath, encoding="utf-8-sig") as csvFile:
            csvReader = csv.reader(csvFile)
            self.__listReport = list(csvReader)
        return self.__listReport

    def DictData(self):
        __CategoryOccur = False
        __ItemList = []
        for row in self.__listReport:
            if __CategoryOccur:
                __ItemList.append(row)
                continue

            if self.FindHeader(row) == 1:
                __CategoryOccur = True
        self.__dictData["ItemsList"] = __ItemList
        return self.__dictData


    def FindHeader(self, Row):
        for header in HeaderName.keys():
            __index = self.FindIndex(Row,header)
            if __index >= 0 and header != "類別":
                keyName = HeaderName.get(header)
                self.__dictData[keyName] = Row[__index+1]
                return 0
            elif __index >= 0 and header == "類別":
                return 1

    def FindIndex(self, Row, Name):
        try:
            return Row.index(Name)
        except:
            return -1
def main():
    openCsv = OpenCSV(
    r"D:\Documents\_Hayman files\1_Project\WebCrawler\AutoFillPRForm\Template.csv")
    listTable = openCsv.OpenCsv()
    print(listTable)
    print(listTable[0].index("使用成本中心"))

    print(openCsv.DictData())


if __name__ == '__main__':
    main()