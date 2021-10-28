from selenium.webdriver.common.keys import Keys


class searchPage:
    def __init__(self, driver):
        self.driver = driver

        self.advancesearch_link_linktext = "Advanced search"

    def advancesearch_click(self):
        self.driver.find_element_by_link_text(self.advancesearch_link_linktext).click()
