from importlib.resources import path
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#chromedriver in PATH
driver = webdriver.Chrome("chromedriver")
driver.get("https://starcitygames.com/")
assert "Star City Games | Magic the Gathering | MTG Card Search | MTG Singles | Decks" in driver.title
elem = driver.find_element(By.XPATH, "/html/body/header/div[4]/div/div[2]/a[1]")
elem.click()
elem.clear()
elem.send_keys("Mana Crypt")
elem.send_keys(Keys.RETURN)


class PythonOrgSearch(unittest.TestCase):
    """A sample test class to show how page object works"""

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.starcitygames.org")

    def test_search_in_starcitygames_com(self):
        # Load mainpage
        main_page = page.MainPage(self.driver)
        # Checks if the word "Star City Games | Magic the Gathering | MTG Card Search | MTG Singles | Decks" is in title
        self.assertTrue(main_page.is_title_matches(
        ), 'Star City Games | Magic the Gathering | MTG Card Search | MTG Singles | Decks')
        # Sets the text of search textbox to "Mana Crypt"
        main_page.search_text_element = "Mana Crypt"
        main_page.click_go_button()
        search_results_page = page.SearchResultsPage(self.driver)
        # Verifies that the results page is not empty
        self.assertTrue(search_results_page.is_results_found(),
                        "No results found.")

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
