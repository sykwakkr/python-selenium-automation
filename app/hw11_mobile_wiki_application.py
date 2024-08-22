from pages.hw11_mobile_wiki_pages_base import HW11MobilePagesBase
from pages.hw11_mobile_wiki_pages_onboard import HW11MobilePagesOnboard
from pages.hw11_mobile_wiki_pages_main import HW11MobilePagesMain
from pages.hw11_mobile_youtube_pages_root import HW11MobileYoutubePagesRoot
from pages.hw11_mobile_youtube_pages_search import HW11MobileYoutubePagesSearch
from pages.hw11_mobile_youtube_pages_view import HW11MobileYoutubePagesView


class HW11MobileApplication:
    def __init__(self, driver):
        self.driver = driver
        self.hw11_page_base = HW11MobilePagesBase(self.driver)
        self.hw11_page_onboard = HW11MobilePagesOnboard(self.driver)
        self.hw11_page_main = HW11MobilePagesMain(self.driver)
        self.hw11_youtube_page_root = HW11MobileYoutubePagesRoot(self.driver)
        self.hw11_youtube_page_search = HW11MobileYoutubePagesSearch(self.driver)
        self.hw11_youtube_page_view = HW11MobileYoutubePagesView(self.driver)

