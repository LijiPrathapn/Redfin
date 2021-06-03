import pytest
from Pages.findPage import findPage
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen
from Utilities import Xutils
import time

class Test_002_DDT_find():
    baseURL = ReadConfig.getApplicationURL()
    path = "C:\\Users\\lijin\\PycharmProjects\\Redfin\\TestData\\Redfindata.xlsx"
    #logger = LogGen.loggen()  # Logger
    #integer="25"
    #integernew="3"


    def test_find_ddt(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.fp = findPage(self.driver)

        self.rows = Xutils.getRowCount(self.path,'Sheet1')
        print('Number of rows...',self.rows)


        for r in range(2,self.rows+1):
            self.City = Xutils.readData(self.path,'Sheet1',r,1)
            self.integer=Xutils.readData(self.path,'Sheet1',r,2)
            self.integernew = Xutils.readData(self.path, 'Sheet1', r, 3)
            self.fp.clickPlace(self.City)
            time.sleep(2)
            self.fp.clickPopup()
            time.sleep(2)
            #act_title=self.driver.title
            #exp_title="Sunnyvale Homes for Sale: Sunnyvale, CA Real Estate | Redfin"
            self.fp.clickPrice()
            self.fp.clickMinPrice(self.integer)
            self.driver.execute_script("document.getElementsByClassName('option')[" + self.integer + "].click();")
            time.sleep(2)
            self.fp.clickMaxPrice(self.integernew)
            self.driver.execute_script("document.getElementsByClassName('option')[" + self.integernew + "].click();")
            time.sleep(2)
            self.fp.clickDone()
            self.fp.clickTotal()
            self.fp.clickCity()
































