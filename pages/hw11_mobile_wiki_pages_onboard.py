from appium.webdriver.common.appiumby import AppiumBy
from pages.hw11_mobile_wiki_pages_base import HW11MobilePagesBase


class HW11MobilePagesOnboard(HW11MobilePagesBase):
    ONBOARDING_SKIP_BUTTON = (AppiumBy.ID, 'org.wikipedia:id/fragment_onboarding_skip_button')

    def click_to_skip(self):
        self.click(*self.ONBOARDING_SKIP_BUTTON)