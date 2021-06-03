import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from Pages.findPage import findPage
import time

class Test_001_Main:
    baseURL="https://www.redfin.com/"
    City="Sunnyvale,CA,USA"

    def test_main(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        print(self.baseURL.title())
        self.fp =findPage(self.driver)
        self.fp.clickPlace(self.City)
        time.sleep(5)
        self.fp.clickPopup()


