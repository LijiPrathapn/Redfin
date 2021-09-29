from selenium import webdriver
import pytest

@pytest.fixture()
def setup():
    driver=webdriver.Chrome(executable_path="C:\\Users\\lijin\\Downloads\\chromedriver_win32 (6)\\chromedriver.exe")
    driver.maximize_window()

    return driver