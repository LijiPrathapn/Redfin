from selenium import webdriver
import pytest

@pytest.fixture()
def setup():
    driver=webdriver.Chrome(executable_path="C:\\Users\\lijin\\Downloads\\chromedriver_win32 (5)\\chromedriver.exe")
    driver.maximize_window()

    return driver