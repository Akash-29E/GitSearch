from selenium.webdriver.common.keys import Keys
class frontPage():
    def __init__(self, driver):
        self.driver = driver

        self.search_textbox_name = "q"

    def search_text(self, search_text):
        self.driver.find_element_by_name(self.search_textbox_name).clear()
        self.driver.find_element_by_name(self.search_textbox_name).send_keys(search_text)
        self.driver.find_element_by_name(self.search_textbox_name).send_keys(Keys.RETURN)



