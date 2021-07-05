# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 16:02:01 2021

@author: chanhayman
"""

from selenium import webdriver
import selenium
# from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import os

class AutoFillPRForm():
    def __init__(self, url):
        self.__url = url
        self.__driver = webdriver.Chrome() #create a web driver of chrome browser
        self.__RetryTimes = 0
        self.__MaxRetryTimes = 3
    
    def AccessURL(self):
        # access url and open a chrome browser
        self.__driver.get(self.__url)
        
        # wait for loading completedly
        try:
            self.__driver.implicitly_wait(20)
            WebDriverWait(self.__driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//div[contains(text(), 'Loading...')]"))
            )
            WebDriverWait(self.__driver, 20).until_not(
                EC.visibility_of_element_located((By.XPATH, "//div[contains(text(), 'Loading...')]"))
            )
            return True
        except Exception as ex:
            print("Failed to load PR page: " + str(ex))
            return False

    def EditCostCenter(self, CostCenter):
        try:
            #trigger drop down list
            triggerCostCenterDropDownButton = WebDriverWait(self.__driver, 30).until(
                EC.element_to_be_clickable((By.ID, "ext-gen1358")))
            triggerCostCenterDropDownButton.click()
            time.sleep(0.5)

            __liString = "//li[contains(text(),'" + CostCenter + "')]" # "//li[contains(text(),'Manufacturing(二)')]"
            selectCostCenter = WebDriverWait(self.__driver, 20).until(
                EC.presence_of_element_located((By.XPATH, __liString))
            )
            selectCostCenter = self.__driver.find_element_by_xpath(__liString)
            #time.sleep(1)
            #scroll into view
            self.__driver.execute_script("arguments[0].scrollIntoView();", selectCostCenter)
            #wait until its clickable
            WebDriverWait(self.__driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, __liString))
            )
            time.sleep(0.5)
            selectCostCenter.click()
            self.__RetryTimes = 0
            return True
        except Exception as ex:
            print("failed to select cost center: " + str(ex))
            if self.__RetryTimes < self.__MaxRetryTimes:
                self.__RetryTimes+=1
                self.EditCostCenter(CostCenter)
                return
            else:
                self.__RetryTimes = 0
                print("Exceed maximum retry times...")
                os.system('pause')
                return False

    def EditMachineNumber(self, MachineNum):
        # 自組設備編號
        try:
            if self.__RetryTimes == 0:
                keyInMachineNumber = self.__driver.find_element_by_xpath("//input[@id='diyProject-inputEl']")
                keyInMachineNumber.send_keys(MachineNum)

            __liString = "//li[contains(text(), '" + MachineNum +"')]" # "//li[contains(text(), 'P-00678')]"
            keyInMachineNumber = WebDriverWait(self.__driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, __liString))
            )
            time.sleep(0.5)
            keyInMachineNumber.click()
            self.__RetryTimes = 0
            return True
        except Exception as ex:
            print("failed to select machine number: " + str(ex))
            if self.__RetryTimes < self.__MaxRetryTimes:
                self.__RetryTimes+=1
                self.EditMachineNumber(MachineNum)
                return
            else:
                self.__RetryTimes = 0
                print("Exceed maximum retry times...")
                os.system('pause')
                return False

    def EditVendorName(self, VendorName):
        try:
            if self.__RetryTimes == 0:
                keyinVendor = self.__driver.find_element_by_id("vendor-inputEl")
                keyinVendor.send_keys(VendorName)

            __bString = "//b[contains(text(),'" + VendorName + "')]" # "//b[contains(text(),'盛禾')]"
            selectVendor = self.__driver.find_element_by_xpath(__bString)
            selectVendor.click()
            self.__RetryTimes = 0
            return True
        except Exception as ex:
            print("failed to select vendoe name: " + str(ex))
            if self.__RetryTimes < self.__MaxRetryTimes:
                self.__RetryTimes+=1
                self.EditVendorName(VendorName)
                return
            else:
                self.__RetryTimes = 0
                print("Exceed maximum retry times...")
                os.system('pause')
                return False

    def EditProjectCode(self, ProjectCode):
        try:
            '''
            keyInProjectCode = self.__driver.find_element_by_id('project-inputEl')
            keyInProjectCode.send_keys(Keys.CONTROL + "a")
            keyInProjectCode.send_keys(Keys.DELETE)
            keyInProjectCode.send_keys(ProjectCode)
            keyInProjectCode.send_keys(Keys.ENTER)
            '''
            triggerFinProjectDropDownButton = WebDriverWait(self.__driver, 10).until(
        EC.element_to_be_clickable((By.ID, "ext-gen1400")))

            triggerFinProjectDropDownButton.click()
            
            #time.sleep(1)
            __liString = "//li[contains(text(), '" + ProjectCode + "')]" # "//li[contains(text(), '2021_電控組')]"
            #selectFinProject = WebDriverWait(self.__driver, 20).until(EC.presence_of_element_located(By.XPATH, __liString))
            selectFinProject = self.__driver.find_element_by_xpath(__liString)
            self.__driver.execute_script("arguments[0].scrollIntoView();", selectFinProject)
            time.sleep(0.5)
            selectFinProject = WebDriverWait(self.__driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, __liString)))
            
            selectFinProject.click()
            self.__RetryTimes = 0
            return True
        except Exception as ex:
            print("failed to select project code: " + str(ex))
            if self.__RetryTimes < self.__MaxRetryTimes:
                self.__RetryTimes+=1
                self.EditProjectCode(ProjectCode)
                return
            else:
                self.__RetryTimes = 0
                print("Exceed maximum retry times...")
                os.system('pause')
                return False
    
    def TypeInReason(self, ReasonCode):
        # Type words in the text box
        try:
            #"自組設備/M-Sensor/其他/羅盤檢測台車外線配線/P-00678/無"
            self.TypeInWords_ID("reason-inputEl", ReasonCode)
            return True
        except Exception as ex:
            print("Failed to edit reason code: " + str(ex))
            return False
    
    def TypeInComment(self, CommentCode):
        # Type words in the text box
        try:
            #"MP03_/新產品 Instinct 2，Venu 2 Plus，Venu 2S,..等產能準備/M-sensor測站，複製28台。(2021-175)/無/P-00678/量產製程部(MPPE)/陳昱仲/無"
            self.TypeInWords_ID('prComment-inputEl', CommentCode)
            return True
        except Exception as ex:
            print("Failed to edit comment code: " + str(ex))
            return False

    def AddLineInList(self):
        # Append items for purchasing
        addLine = self.__driver.find_element_by_id('addLine-btnInnerEl')
        self.__driver.execute_script("arguments[0].scrollIntoView();", addLine)
        # Append items for purchasing
        addLine = WebDriverWait(self.__driver, 60).until(
            EC.element_to_be_clickable((By.ID, "addLine-btnInnerEl")))
    
        addLine.click()
    
    def EditCategory(self, Category):
        try:
            if self.__RetryTimes == 0:
                categoryTextBox = self.__driver.find_element_by_id("categoryL-inputEl")
                categoryTextBox.send_keys(Category) #'l-03. 自組設備-設備'
                categoryTextBox.send_keys(Keys.ENTER)
                time.sleep(1)
            
            __liString = "//li[contains(text(),'" + Category + "')]" # "//li[contains(text(),'l-03. 自組設備-設備')]"
            selectCategoryList = WebDriverWait(self.__driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, __liString)))
            selectCategoryList = self.__driver.find_element_by_xpath(__liString)
            time.sleep(1)
            selectCategoryList.click()
            self.__RetryTimes = 0
            return True
        except Exception as ex:
            print("failed to select category: " + str(ex))
            if self.__RetryTimes < self.__MaxRetryTimes:
                self.__RetryTimes+=1
                self.EditCategory(Category)
                return
            else:
                self.__RetryTimes = 0
                print("Exceed maximum retry times...")
                os.system('pause')
                return False
        
    def EditOrganization(self, Organization):
        textBoxOrg = self.__driver.find_element_by_id("divisionL-inputEl")
        try:
            textBoxOrg.send_keys(Keys.CONTROL + "a")
            time.sleep(0.5)
            textBoxOrg.send_keys(Keys.DELETE)
            time.sleep(0.5)
        except:
            print("Cannot Cleared")
        
        try:
            textBoxOrg.send_keys(Organization)
            #textBoxOrg.send_keys(Keys.ENTER)
            time.sleep(1)
            __liString = "//li[contains(text(),'" + Organization + "')]" # "//li[contains(text(),'T2-Jhongli')]"
            selectOrg = WebDriverWait(self.__driver, 40).until(
                EC.element_to_be_clickable((By.XPATH, __liString))
            )
            selectOrg.click()
            self.__RetryTimes = 0
            return True
        except Exception as ex:
            print("failed to select organization: " + str(ex))
            if self.__RetryTimes < self.__MaxRetryTimes:
                self.__RetryTimes+=1
                self.EditOrganization(Organization)
                return
            else:
                self.__RetryTimes = 0
                print("Exceed maximum retry times...")
                os.system('pause')
                return False

    def EditNeedDate(self, NeedDate):
        self.TypeInWords_ID("needByDateL-inputEl", NeedDate)

    def EditSpecification(self, Specification):
        self.TypeInWords_ID("specificationL-inputEl", Specification)

    def EditDescription(self, Description):
        self.TypeInWords_ID("descriptionL-inputEl", Description)

    def EditQuantity(self, Quantity):
        self.TypeInWords_ID("quantityL-inputEl", Quantity)

    def EditUnitPrice(self, UnitPrice):
        self.TypeInWords_ID("unitPriceL-inputEl", UnitPrice)
    
    def SaveItemInfo(self):
        try:
            saveButton = self.__driver.find_element_by_xpath(
            "//div[@class='x-toolbar x-docked x-toolbar-footer x-docked-bottom x-toolbar-docked-bottom x-toolbar-footer-docked-bottom x-box-layout-ct']//span[@class='x-btn-wrap']/span[@class='x-btn-button']/span[text() = '儲存']")
            saveButton.find_element_by_xpath("..").click()
            
            '''
            WebDriverWait(self.__driver, 20).until_not(
                EC.presence_of_element_located((By.XPATH, "//span[contains(text(), '表單明細編輯')]"))
            )
            '''
            time.sleep(1)
            self.__RetryTimes = 0
            return True
        except Exception as ex:
            print("Failed to save item's infomation: " + str(ex))
            if self.__RetryTimes < self.__MaxRetryTimes:
                self.__RetryTimes+=1
                self.SaveItemInfo()
                return
            else:
                self.__RetryTimes = 0
                print("Exceed maximum retry times...")
                os.system('pause')
                return False

    def UploadFile(self, FilePath, Category):
        # Upload Files
        try:
            triggerUploadFiles = WebDriverWait(self.__driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//span[@id='btnFileUpload-btnInnerEl']"))
            )
            #triggerUploadFiles = self.__driver.find_element_by_xpath("//span[@id='btnFileUpload-btnInnerEl']")
            triggerUploadFiles.click()
            triggerUploadFiles = WebDriverWait(self.__driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//span[contains(text(), '上傳附件視窗')]"))
            )
            
            openFileSelector = self.__driver.find_element_by_xpath("//input[@id='fileAttachment-button-fileInputEl']") #'fileAttachment-InputEl'
            openFileSelector.send_keys(FilePath)
            time.sleep(0.5)
            selectCategory = self.__driver.find_element_by_xpath("//input[@id='fileCategoryId-inputEl']")
            '''
            Category contains following items:
            1) 報價單
            2) 圖面
            3) 發票
            4) 其他
            5) 出貨單
            '''
            selectCategory.send_keys(Keys.CONTROL + "a")
            selectCategory.send_keys(Keys.DELETE)
            selectCategory.send_keys(Category)
            selectCategory.send_keys(Keys.ENTER)
            time.sleep(0.5)

            uploadFileButton = WebDriverWait(self.__driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//span[text() = '上傳']"))
            )
            time.sleep(1)
            uploadFileButton.click()
            
            WebDriverWait(self.__driver, 30).until(
                EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'file uploading')]"))
            )
            WebDriverWait(self.__driver, 30).until_not(
                EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'file uploading')]"))
            )
            #time.sleep(1)
            return True
        except Exception as ex:
            print("Failed to upload file: " + str(ex))
            return False

    def ApplyRequest(self):
        applyRequest = WebDriverWait(self.__driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text() = '開始傳簽']"))
        )
        time.sleep(1)
        applyRequest.find_element_by_xpath("..").click()

        waitApplySuccess = WebDriverWait(self.__driver, 60).until(
            EC.presence_of_element_located((By.XPATH, "//span[text() = '完成']"))
        )

    def GetDropDownList_XPath(self, __driver, __XPath):
        time.sleep(3)
        __driver.implicitly_wait(10)
        __dropDownList = __driver.find_element_by_xpath(__XPath)

        for __element in __dropDownList:
            print(__element.get_attribute('textContent'))

    def TypeInWords_ID(self, __id, __string):
        __textBox = self.__driver.find_element_by_id(__id)
        try:
            __textBox.send_keys(Keys.CONTROL + "a")
            __textBox.send_keys(Keys.DELETE)

        except:
            print(__id + "cannot be cleared.")

        __textBox.send_keys(__string)
        time.sleep(0.5)
        __textBox.send_keys(Keys.ENTER)

'''
def main():
    for _i in range(2):
        applyForm()

if __name__ == '__main__':
    main()
'''