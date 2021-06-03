
class findPage:
    textbox_place_id = "search-box-input"
    pop_up_xpath = "//*[@id='tabContentId0']/div/div/form/div[3]/div[1]/div/div[2]/div"
    place_xpath = "//*[@id='header-content']/header[2]/div[1]/div[1]/div"
    price_xpath = "//*[@id='exposed-filters-container']/div/div/form/div[1]/div[1]/span"
    MinPrice_xpath = "//span[@class='field select Select quickMinPrice withFlyout withOptions mounted selected clickable optional']"
    MaxPrice_xpath ="//span[@class='field select Select quickMaxPrice withFlyout withOptions mounted selected clickable optional']"
    Done_xpath = "//*[@id='exposed-filters-container']/div/div/form/div[1]/div[2]/div[1]/div/div[2]/div[2]/button[2]"
    Totallist_xpath = "//div[contains(@class,'descriptionSummary')]/div[@class='homes summary']"

    def __init__(self,driver):
        self.driver = driver

    def clickPlace(self,City):
        self.driver.find_element_by_id(self.textbox_place_id).send_keys(City)

    def clickPopup(self):
        self.driver.find_element_by_xpath(self.pop_up_xpath).click()

    def clickPrice(self):
        self.driver.find_element_by_xpath(self.price_xpath).click()

    def clickCity(self):
        self.driver.find_element_by_xpath(self.place_xpath).click()

    def clickMinPrice(self,integer):
        self.driver.find_element_by_xpath(self.MinPrice_xpath).click()

    def clickMaxPrice(self,integernew):
        self.driver.find_element_by_xpath(self.MaxPrice_xpath).click()

    def clickDone(self):
        self.driver.find_element_by_xpath(self.Done_xpath).click()

    def clickTotal(self):
        Total=self.driver.find_element_by_xpath(self.Totallist_xpath)
        print(Total.text," Listed for the Price Mentioned")















