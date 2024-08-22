from appium.webdriver.common.appiumby import AppiumBy
from pages.hw11_mobile_wiki_pages_base import HW11MobilePagesBase


class HW11MobilePagesMain(HW11MobilePagesBase):
    SEARCH_FIELD = (AppiumBy.XPATH, '//android.widget.TextView[@text="Search Wikipedia"]')
    SEARCH_INPUT = (AppiumBy.ID, 'org.wikipedia:id/search_src_text')
    SEARCH_RESULT = (AppiumBy.ID, 'org.wikipedia:id/page_list_item_title')

    def click_on_search_field(self):
        self.click(*self.SEARCH_FIELD)

    def search_for(self, search_input):
        self.input(search_input, *self.SEARCH_INPUT)

    def verify_first_result(self, search_input):
        self.verify_text(search_input, *self.SEARCH_RESULT)

