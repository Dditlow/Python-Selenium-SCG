from element import BasePageElement
from locator import MainPageLocators

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

class MainPage(BasePage):
    #search_text_element = SearchTextElement()

    def is_title_matches(self):
        return "TCGplayer: Online Store for Collectible Trading Card Games" in self.driver.title

    def click_go_button(self):
        """Triggers the search"""

        element = self.driver.find_element(*MainPageLocators.GO_BUTTON)
        element.click()

class SearchResultsPage(BasePage):
    """Search results page action methods come here"""

    def is_results_found(self):

        return "No results found." not in self.driver.page_source