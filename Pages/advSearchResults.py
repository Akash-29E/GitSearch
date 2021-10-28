
class advSearchResults():
    def __init__(self, driver):
        self.driver = driver

        self.heading_xpath = "//h3[contains(text(),'1 repository result')]"
        self.first_link_linktext = "mvoloskov/decider"

    def verifyResultHead(self, Heading3):
        element = self.driver.find_element_by_xpath(self.heading_xpath)
        assert element.text == Heading3

    def verifyResultText(self, text):
        assert text in self.driver.page_source

    def clickLink1(self):
        self.driver.find_element_by_link_text(self.first_link_linktext).click()

