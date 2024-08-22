from appium.webdriver.common.appiumby import AppiumBy
from pages.hw11_mobile_wiki_pages_base import HW11MobilePagesBase


class HW11MobileYoutubePagesView(HW11MobilePagesBase):
    VIEW_RESULTS = (AppiumBy.ACCESSIBILITY_ID, "Jinny's Kitchen Season 2 | Official Teaser | Prime Video - 55 seconds - Go to channel - Prime Video AU & NZ - 316K views - 2 months ago - play video")

    def verify_watch_input(self, watch_input):
        watch_result = self.find_element(*self.VIEW_RESULTS)[0].get_attribute("content-desc") + "a"
        assert watch_input in watch_result, f'{watch_input} not found in {self.VIEW_RESULTS}'

