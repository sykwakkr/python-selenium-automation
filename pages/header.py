from selenium.webdriver.common.by import By
from pages.base_page import Page


class Header(Page):
    CART_BTN = (By.XPATH, '//*[@id="cart"]')
    SEARCH_FILED = (By.ID, 'search')
    SEARCH_BTN = (By.XPATH, '//button[@data-test="@web/Search/SearchButton"]')

    def search(self):
        self.input_text('coffee', *self.SEARCH_FILED)
        self.click(self.SEARCH_BTN)

    def click_cart(self):
        self.click(self.CART_BTN)