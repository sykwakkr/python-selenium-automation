from pages.hw9_target_pages_base import HW9PagesBase
from pages.hw9_target_pages_help import HW9PageHelp
from pages.hw9_target_pages_signin import HW9PageSignIn


class HW9Application:
    def __init__(self, driver):
        self.driver = driver
        self.hw9_page_base = HW9PagesBase(self.driver)
        self.hw9_page_help = HW9PageHelp(self.driver)
        self.hw9_page_signin = HW9PageSignIn(self.driver)