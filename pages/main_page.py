from pages.base_page import Page


class MainPage(Page):
    OPEN_URL = 'https://www.target.com/'

    def open(self):
        self.open_url('https://www.target.com/')
