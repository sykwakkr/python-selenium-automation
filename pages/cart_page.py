from selenium.webdriver.common.by import By
from pages.base_page import Page


class CartPage(Page):
    CART_EMPTY_MSG = (By.CSS_SELECTOR, '.message')

    # def verify_cart_empty(self):
    #     expected_text = 'Y'
    #     actual_text = ''