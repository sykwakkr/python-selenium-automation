from pages.hw9_target_pages_base import HW9PagesBase
from selenium.webdriver.common.by import By


class HW9PageHelp(HW9PagesBase):
    URL_HELP_TOPIC = 'https://help.target.com/help/SubCategoryArticle?childcat=Returns&parentcat=Returns+%26+Exchanges'
    OPTION_TITLE = (By.CSS_SELECTOR, '#pageTitle h1')

    def open_help_topics_return_page(self):
        self.open_url(self.URL_HELP_TOPIC)

    def select_option_topic(self, value):
        self.dropdown_select().select_by_value(value)

    def verify_correct_option_page(self, title):
        expected_head_title = title
        # for Safari
        self.wait_until_title_is(expected_head_title)
        selected_page_title = self.find_element(*self.OPTION_TITLE).text
        print(f'Selected Page Title: {selected_page_title}')
        assert expected_head_title.strip() == selected_page_title.strip(), f'Expected {expected_head_title} but got {selected_page_title}'



