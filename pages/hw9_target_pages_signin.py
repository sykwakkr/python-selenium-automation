from selenium.webdriver.common.by import By
from pages.hw9_target_pages_base import HW9PagesBase


class HW9PageSignIn(HW9PagesBase):
    URL_LOGIN = 'https://www.target.com/account/login'
    LOC_USERNAME = (By.ID, 'username')
    LOC_PASSWORD = (By.ID, 'password')
    LOC_SIGNIN = (By.ID, 'login')
    LOC_ALERT = (By.CSS_SELECTOR, '[data-test="authAlertDisplay"]')
    TITLE_LOGIN = 'Login: Target'

    def open_sign_in_page(self):
        self.open_url(self.URL_LOGIN)

    def enter_incorrect_email_and_password(self):
        # For Safari
        self.wait_until_title_is(self.TITLE_LOGIN)
        incorrect_email = 'X' + self.EMAIL
        incorrect_password = self.PASSWORD + 'X'
        self.input_text(incorrect_email, *self.LOC_USERNAME)
        self.input_text(incorrect_password, *self.LOC_PASSWORD)

    def click_sign_in_button(self):
        self.find_element_and_click(*self.LOC_SIGNIN)

    def verify_signin_alert_message(self, alert):
        expected_alert = alert
        alert_message = self.find_element(*self.LOC_ALERT).text
        print(f'Alert Message: {alert_message}')
        assert alert_message == expected_alert, f'Expected alert message {expected_alert} but got {alert_message}'