# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 16:02:01 2021

@author: chanhayman
"""

from selenium import webdriver
# from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

class AutoFillPRForm():
    def __init__(self, url):
        self.__url = url
        
    def GetDropDownList_XPath(__driver, __XPath):
        time.sleep(3)
        __driver.implicitly_wait(10)
        __dropDownList = __driver.find_element_by_xpath(__XPath)

        for __element in __dropDownList:
            print(__element.get_attribute('textContent'))

    def TypeInWords_ID(__driver, __id, __string):
        __textBox = __driver.find_element_by_id(__id)
        try:
            __textBox.send_keys(Keys.CONTROL + "a")
            __textBox.send_keys(Keys.DELETE)

        except:
            print(__id + "cannot be cleared.")

        __textBox.send_keys(__string)
        time.sleep(0.5)
        __textBox.send_keys(Keys.ENTER)

    def applyForm():
        url = "https://shiwpa-etrex9.garmin.com:9099/FINSystem/PrApplyInit.action"

        # headless = webdriver.ChromeOptions()
        # headless.add_argument('headless')
        # driver = webdriver.Chrome(options=headless)

        driver = webdriver.Chrome()
        driver.get(url)

        # time.sleep(3)
        
        # Example of how to select a item in the drop-down list. Here, we select the Financial Project to demonstrate.
        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//div[contains(text(), 'Loading...')]"))
        )
        WebDriverWait(driver, 20).until_not(
            EC.visibility_of_element_located((By.XPATH, "//div[contains(text(), 'Loading...')]"))
        )
        triggerCostCenterDropDownButton = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.ID, "ext-gen1358")))
        triggerCostCenterDropDownButton.click()
        time.sleep(1)

        WebDriverWait(driver, 40)
        driver.implicitly_wait(10)
        # WebDriverWait(driver, 60).until_not(
        #     EC.alert_is_present(), "Loading..."
        # )
        selectCostCenter = driver.find_element_by_xpath("//li[contains(text(),'Manufacturing(二)')]")
        time.sleep(1)
        driver.execute_script("arguments[0].scrollIntoView();", selectCostCenter)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//li[contains(text(),'Manufacturing(二)')]"))
        )
        time.sleep(1)
        selectCostCenter.click()

        # 自組設備編號
        keyInMachineNumber = driver.find_element_by_xpath("//input[@id='diyProject-inputEl']")
        keyInMachineNumber.send_keys("P-00678")
        keyInMachineNumber = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//li[contains(text(), 'P-00678')]"))
        )
        time.sleep(1)
        keyInMachineNumber.click()

        # selectCostCenter = driver.find_element_by_xpath("//input[@id='costCenter-inputEl']")
        # time.sleep(1)
        # selectCostCenter.send_keys("630. Manufacturing(一)")
        # time.sleep(1)

        # TypeInWords_ID(driver, "vendor-inputEl", "盛禾")
        keyinVendor = driver.find_element_by_id("vendor-inputEl")
        keyinVendor.send_keys("盛禾")
        selectVendor = driver.find_element_by_xpath("//b[contains(text(),'盛禾')]")
        selectVendor.click()
        
        triggerFinProjectDropDownButton = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "ext-gen1400")))

        triggerFinProjectDropDownButton.click()

        time.sleep(1)
        
        # dropDownList = driver.find_elements_by_xpath(
        #     "//div[@id='boundlist-1137-listEl']//ul[@class='x-list-plain']//li")
        # for _element in dropDownList:
        #     print(_element.get_attribute('textContent'))

        selectFinProject = driver.find_element_by_xpath(
            "//li[contains(text(), '2021_電控組')]")
        selectFinProject.click()

        # Type words in the text box
        TypeInWords_ID(driver, "reason-inputEl", "自組設備/M-Sensor/其他/羅盤檢測台車外線配線/P-00678/無")

        textBox = driver.find_element_by_id('prComment-inputEl')
        textBox.send_keys("MP03_/新產品 Instinct 2，Venu 2 Plus，Venu 2S,..等產能準備/M-sensor測站，複製28台。(2021-175)/無/P-00678/量產製程部(MPPE)/陳昱仲/無")

        # Append items for purchasing
        addLine = driver.find_element_by_id('addLine-btnInnerEl')
        addLine.click()
        time.sleep(1)

        # triggerCategorySearch = WebDriverWait(driver, 20).until(
        #     EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), '分類檢索')]"))
        # )
        # triggerCategorySearch.click()

        # triggerCategoryDropDownList = WebDriverWait(driver, 20).until(
        #     EC.element_to_be_clickable((By.ID, "uxFinCategory-inputEl"))
        # )
        # triggerCategoryDropDownList.click()

        # time.sleep(1)
        # categoryDropDownList = driver.find_elements_by_xpath("//div[@class='x-boundlist-list-ct x-unselectable']//ul[@class='x-list-plain']//li")
        
        # for _element in categoryDropDownList:
        #     print(_element.get_attribute('textContent'))

        categoryTextBox = driver.find_element_by_id("categoryL-inputEl")
        categoryTextBox.send_keys('l-03. 自組設備-設備')
        time.sleep(0.5)
        selectCategoryList = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//li[contains(text(),'l-03. 自組設備-設備')]")))
        # selectCategoryList = driver.find_element_by_xpath("//li[contains(text(),'09-01. 消耗性器材')]")
        selectCategoryList.click()

        textBoxOrg = driver.find_element_by_id("divisionL-inputEl")
        try:
            textBoxOrg.send_keys(Keys.CONTROL + "a")
            textBoxOrg.send_keys(Keys.DELETE)
        except:
            print("Cannot Cleared")
        textBoxOrg.send_keys("T2-Jhongli")
        time.sleep(1)
        selectOrg = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//li[contains(text(),'T2-Jhongli')]"))
        )
        selectOrg.click()
        # TypeInWords_ID(driver, "divisionL-inputEl", "不分廠")

        TypeInWords_ID(driver, "needByDateL-inputEl", "2021-03-24")
        TypeInWords_ID(driver, "specificationL-inputEl", "羅盤檢測台車配線費用(測試箱)")
        TypeInWords_ID(driver, "descriptionL-inputEl", '''工程內容：
    1.羅盤檢測設備配線。
    2.管開銷費用。''')
        TypeInWords_ID(driver, "quantityL-inputEl", "2")
        TypeInWords_ID(driver, "unitPriceL-inputEl", "3500")

        saveButton = driver.find_element_by_xpath(
            "//div[@class='x-toolbar x-docked x-toolbar-footer x-docked-bottom x-toolbar-docked-bottom x-toolbar-footer-docked-bottom x-box-layout-ct']//span[@class='x-btn-wrap']/span[@class='x-btn-button']/span[text() = '儲存']")
        saveButton.find_element_by_xpath("..").click()
        

        WebDriverWait(driver, 20).until_not(
            EC.presence_of_element_located((By.XPATH, "//span[contains(text(), '表單明細編輯')]"))
        )
        time.sleep(1)

        driver.execute_script("arguments[0].scrollIntoView();", addLine)
        # Append items for purchasing
        addLine = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.ID, "addLine-btnInnerEl")))
        # driver.find_element_by_id('addLine-btnInnerEl')
        # time.sleep(1)
        
        addLine.click()

        categoryTextBox = driver.find_element_by_id("categoryL-inputEl")
        categoryTextBox.send_keys('l-03. 自組設備-設備')
        # categoryTextBox.send_keys(Keys.ENTER)
        time.sleep(0.5)
        
        # selectCategoryList = driver.find_element_by_xpath("//li[contains(text(),'09-01. 消耗性器材')]")
        for _i in range(5):
            time.sleep(1)
            try:
                selectCategoryList = WebDriverWait(driver, 20).until(
                    EC.visibility_of_element_located((By.XPATH, "//li[contains(text(),'l-03. 自組設備-設備')]")))
                selectCategoryList = WebDriverWait(driver, 20).until(
                    EC.element_to_be_clickable((By.XPATH, "//li[contains(text(),'l-03. 自組設備-設備')]")))
                selectCategoryList.click()
                break
            except:
                print("Try again...")

        textBoxOrg = driver.find_element_by_id("divisionL-inputEl")
        try:
            textBoxOrg.send_keys(Keys.CONTROL + "a")
            textBoxOrg.send_keys(Keys.DELETE)
        except:
            print("Cannot Cleared")
        textBoxOrg.send_keys("T2-Jhongli")
        time.sleep(1)
        selectOrg = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//li[contains(text(),'T2-Jhongli')]"))
        )
        selectOrg.click()
        # TypeInWords_ID(driver, "divisionL-inputEl", "不分廠")

        TypeInWords_ID(driver, "needByDateL-inputEl", "2021-03-24")
        TypeInWords_ID(driver, "specificationL-inputEl", "貨運費用")
        TypeInWords_ID(driver, "descriptionL-inputEl", '''工程內容：
    1.羅盤檢測設備配線。
    2.管開銷費用。''')
        TypeInWords_ID(driver, "quantityL-inputEl", "1")
        TypeInWords_ID(driver, "unitPriceL-inputEl", "2500")

        saveButton = driver.find_element_by_xpath(
            "//div[@class='x-toolbar x-docked x-toolbar-footer x-docked-bottom x-toolbar-docked-bottom x-toolbar-footer-docked-bottom x-box-layout-ct']//span[@class='x-btn-wrap']/span[@class='x-btn-button']/span[contains(text(), '儲存')]")
        saveButton.find_element_by_xpath("..").click()
        

        # Upload Files
        triggerUploadFiles = driver.find_element_by_xpath("//span[@id='btnFileUpload-btnInnerEl']")
        triggerUploadFiles.click()

        openFileSelector = driver.find_element_by_xpath("//input[@id='fileAttachment-button-fileInputEl']")
        # openFileSelector = WebDriverWait(driver, 30).until(
        #     EC.element_to_be_clickable((By.XPATH, "//input[@id='fileAttachment-button-fileInputEl']"))
        # )
        openFileSelector.send_keys("D:\\Documents\\_Hayman files\\1_Project\\羅盤\\羅盤採購\\20210309\\委外配線\\羅盤檢測配線2port(1套)報價單-20210315.doc")
        # waitUploadDialog = WebDriverWait(driver, 60).until(
        #     EC.presence_of_element_located((By.XPATH, "//span[contains(text(), '上傳附件視窗')]"))
        # )
        uploadFileButton = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text() = '上傳']"))
        )
        uploadFileButton.click()
        
        WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'file uploading')]"))
        )
        WebDriverWait(driver, 30).until_not(
            EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'file uploading')]"))
        )
        time.sleep(1)

        # Upload Files
        triggerUploadFiles = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//span[@id='btnFileUpload-btnInnerEl']"))
        )
        # driver.find_element_by_xpath("//span[@id='btnFileUpload-btnInnerEl']")
        
        time.sleep(1)
        triggerUploadFiles.click()

        openFileSelector = driver.find_element_by_xpath("//input[@id='fileAttachment-button-fileInputEl']")
        # openFileSelector = WebDriverWait(driver, 30).until(
        #     EC.element_to_be_clickable((By.XPATH, "//input[@id='fileAttachment-button-fileInputEl']"))
        # )
        openFileSelector.send_keys("D:\\Documents\\_Hayman files\\1_Project\\羅盤\\羅盤採購\\20210309\\_reference\\2021Sensor ROI.pptx")
        # waitUploadDialog = WebDriverWait(driver, 60).until(
        #     EC.presence_of_element_located((By.XPATH, "//span[contains(text(), '上傳附件視窗')]"))
        # )
        uploadFileButton = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text() = '上傳']"))
        )
        uploadFileButton.click()
        
        WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'file uploading')]"))
        )
        WebDriverWait(driver, 30).until_not(
            EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'file uploading')]"))
        )

        time.sleep(1)

        applyRequest = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text() = '開始傳簽']"))
        )
        time.sleep(1)
        applyRequest.find_element_by_xpath("..").click()

        waitApplySuccess = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH, "//span[text() = '完成']"))
        )

        print("Success!")

def main():
    for _i in range(2):
        applyForm()

if __name__ == '__main__':
    main()