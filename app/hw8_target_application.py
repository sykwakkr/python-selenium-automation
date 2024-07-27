from pages.hw8_target_pages_basic import HW8PageBase
from pages.hw8_target_pages_login import HW8PageLogin


class HW8Application:
    def __init__(self, driver):
        self.driver = driver
        self.hw8_page_base = HW8PageBase(self.driver)
        self.hw8_page_login = HW8PageLogin(self.driver)