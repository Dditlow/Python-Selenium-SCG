# Libraries to import
from importlib.resources import path
import unittest
from selenium import webdriver
import page
# Test #1


class TCGPlayercomSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.tcgplayer.com")

    def test_print_in_tcgplayer_com(self):
        # Load mainpage
        main_page = page.MainPage(self.driver)
        print("Test")
        
    def test_title_search_in_tscgplayer_com():    
        # Checks if the word "TCGplayer: Online Store for Collectible Trading Card Games" is in title
        self.assertTrue(main_page.is_title_matches(
        ), "TCGplayer: Online Store for Collectible Trading Card Games")
        print(driver.main_page.title)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
