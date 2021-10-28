from selenium.webdriver.support.ui import Select


class advSearchPage():
    def __init__(self, driver):
        self.driver = driver

        self.languagename_dropdown_id = "search_language"
        self.starcount_textbox_id = "search_stars"
        self.followers_textbox_id = "search_followers"
        self.licname_dropdown_id = "search_license"
        self.search_button_xpath = "//body/div[4]/main[1]/form[1]/div[2]/div[1]/div[1]/button[1]"

    def writtenlanselect(self, LanName):
        select = Select(self.driver.find_element_by_id(self.languagename_dropdown_id))
        select.select_by_visible_text(LanName)

    def starcount(self, StarCount):
        self.driver.find_element_by_id(self.starcount_textbox_id).send_keys(StarCount)

    def followercount(self, followCount):
        self.driver.find_element_by_id(self.followers_textbox_id).send_keys(followCount)

    def licenseselect(self, LicName):
        select = Select(self.driver.find_element_by_id(self.licname_dropdown_id))
        select.select_by_visible_text(LicName)

    def clicksearch(self):
        self.driver.find_element_by_xpath(self.search_button_xpath).click()

