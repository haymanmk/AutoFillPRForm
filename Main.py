# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 13:29:53 2021

@author: chanhayman
"""
import AutoFillPRForm
import OpenCSV
import os

def main():
    openCsv = OpenCSV.OpenCSV(
        r"D:\Documents\_Hayman files\1_Project\Watch Bonding 3\採購\T5_GigaFactory\稼動.csv")
    openCsv.OpenFile()
    dictData = openCsv.DictData()
    '''
    CostCenter = "Manufacturing(一)"
    MachineNumber = "P-00727"
    VendorName = "台灣百科"
    ProjectCode = "2021_T5_擴線專案_ASSY-TEST"
    ReasonCode = "Hi"
    '''
    url = "https://shiwpa-etrex9.garmin.com:9099/FINSystem/PrApplyInit.action"
    autoFill = AutoFillPRForm.AutoFillPRForm(url)
    autoFill.AccessURL()
    autoFill.EditCostCenter(dictData["CostCenter"])
    autoFill.EditMachineNumber(dictData["MachineNumber"])
    autoFill.EditVendorName(dictData["VendorName"])
    autoFill.EditProjectCode(dictData["ProjectCode"])
    autoFill.TypeInReason(dictData["Reason"])
    autoFill.TypeInComment(dictData["Comment"])
    
    for row in dictData["ItemsList"]:
        autoFill.AddLineInList()
        autoFill.EditCategory(row[0])
        autoFill.EditOrganization(dictData["Organization"])
        autoFill.EditNeedDate(dictData["NeedDate"])
        autoFill.EditSpecification(row[1])
        autoFill.EditDescription(row[4])
        autoFill.EditQuantity(row[2])
        autoFill.EditUnitPrice(row[3])
        autoFill.SaveItemInfo()
    autoFill.UploadFile(dictData["Quotation"],"報價單")
    autoFill.UploadFile(dictData["Others"], "報價單")
    
    
    autoFill.ApplyRequest()
    print("Success")
    os.system('pause')
    
    
if __name__ == '__main__':
    main()