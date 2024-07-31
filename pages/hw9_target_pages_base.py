from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert


class HW9PagesBase:
    EMAIL = 'ilvys@putameda.com'
    PASSWORD = 'SeleAuto'

    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        self.driver.get(url)

    def dropdown_select(self):
        select = Select(self.driver.find_element(By.TAG_NAME, 'select'))
        return select

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_element_and_click(self, *locator):
        self.driver.find_element(*locator).click()

    def input_text(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)

    def wait_until_visible(self, *locator):
        self.driver.wait.until(EC.visibility_of_all_elements_located(locator))

    def wait_until_title_is(self, title):
        self.driver.wait.until(EC.title_is(title))

    def get_alert_text(self):
        alert = Alert(self.driver)
        return alert.text
