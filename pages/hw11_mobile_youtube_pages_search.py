from appium.webdriver.common.appiumby import AppiumBy
from pages.hw11_mobile_wiki_pages_base import HW11MobilePagesBase
from time import sleep


class HW11MobileYoutubePagesSearch(HW11MobilePagesBase):
    SEARCH_EDIT_TEXT = (AppiumBy.ID, 'com.google.android.youtube:id/search_edit_text')
    SEARCH_TEXT = (AppiumBy.ID, 'com.google.android.youtube:id/text')

    def search_youtube_for(self, watch_input):
        self.input(watch_input, *self.SEARCH_EDIT_TEXT)
        self.click(*self.SEARCH_TEXT)
        sleep(5)
