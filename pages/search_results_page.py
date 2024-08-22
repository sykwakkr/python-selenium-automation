from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import Page


class SearchResultsPage(Page):
    SEARCH_RESULTS_TXT = (By.CSS_SELECTOR, '[data-test="resultsHeading"]>span')

    def verify_text(self):
        actual_text = self.driver.find_element(*self.SEARCH_RESULTS_TXT)
        assert 'coffee' in actual_text.text

    def verify_url(self):
        url = self.driver.current_url
        assert 'coffee' in url
