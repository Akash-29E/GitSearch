from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from Pages.frontPage import frontPage
from Pages.searchPage import searchPage
from Pages.advSearchPage import advSearchPage
from Pages.advSearchResults import advSearchResults
from Pages.readMe import readMe
from Utils import utils as utils
import pytest
import time

class TestSearch():

    @pytest.fixture(scope="class")
    def test_setup(self):
        global driver
        from selenium import webdriver
        from webdriver_manager.chrome import ChromeDriverManager
        driver = webdriver.Chrome(ChromeDriverManager().install())
        # driver.implicitly_wait(5)
        driver.maximize_window()
        yield
        driver.close()
        driver.quit()
        print("Test Completed!")

    def test_search(self, test_setup):

        driver.get("http://www.github.com")
        front = frontPage(driver)
        front.search_text(utils.SEARCH_QUERY)

        search = searchPage(driver)
        search.advancesearch_click()

        adsearch = advSearchPage(driver)
        adsearch.writtenlanselect("JavaScript")
        adsearch.starcount(">45")
        adsearch.followercount(">50")
        adsearch.licenseselect("Boost Software License 1.0")
        adsearch.clicksearch()

        adsres = advSearchResults(driver)
        adsres.verifyResultHead("1 repository result")
        adsres.verifyResultText("mvoloskov/decider")
        adsres.clickLink1()

        readme = readMe(driver)
        readme.clickReadMe()
        readme.printreadme(300)
        time.sleep(3)





