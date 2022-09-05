# Libraries to import
from importlib.resources import path
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import page
# Test #1


class TCGPlayercomSearch(unittest.TestCase):
    """A sample test class to show how page object works"""

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.tcgplayer.com")
        self.driver.implicitly_wait(10)

    def test_search_in_tcgplayer_com(self):
        # Load mainpage
        main_page = MainPage(self.driver)
        # Checks if the word "Python" is in title
        self.assertTrue(main_page.is_title_matches(
        ), "TCGplayer: Online Store for Collectible Trading Card Games")
        print("Testing")

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
