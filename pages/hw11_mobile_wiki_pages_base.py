from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

class HW11MobilePagesBase:
    def __init__(self, driver):
        self.driver = driver

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def input(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)

    def input_and_enter(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text + Keys.ENTER)

    def input_and_click(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text).click(0)

    def verify_text(self, expected_text, *locator):
        actual_text = self.driver.find_element(*locator).text
        assert actual_text == expected_text, f'Expected: {expected_text}, Actual: {actual_text}'

    def verify_partial_text(self, expected_text, *locator):
        actual_text = self.driver.find_element(*locator)
        assert actual_text in expected_text, f'Expected: {expected_text}, Actual: {actual_text}'

    def get_attribute(self, value, *locator):
        return self.driver.find_element(*locator).get_attribute('value')

    def find_element(self, *locator):
        return self.driver.find_elements(*locator)