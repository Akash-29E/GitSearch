class readMe():
    def __init__(self, driver):
        self.driver = driver

        self.readme_link_linktext = "README.md"
        self.readme_codeblock_css = "#readme"

    def clickReadMe(self):
        self.driver.find_element_by_link_text(self.readme_link_linktext).click()


    def printreadme(self, charcount):
        readme = self.driver.find_element_by_css_selector(self.readme_codeblock_css)
        seltext = readme.text[0:charcount]
        print(seltext)
