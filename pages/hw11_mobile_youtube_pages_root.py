from appium.webdriver.common.appiumby import AppiumBy
from pages.hw11_mobile_wiki_pages_base import HW11MobilePagesBase


class HW11MobileYoutubePagesRoot(HW11MobilePagesBase):
    SEARCH_YOUTUBE = (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="Search YouTube"]')

    def click_search_field_for_watch(self):
        self.click(*self.SEARCH_YOUTUBE)

