# from Pages
class Page:
    def click(self):
        print('Clicking...')

    def verify_text(self):
        print('Verifying...')

    def input_text(self, text):
        print(f'Inputting text, {text}')


class LoginPage(Page):
    # pass
    def login(self):
        self.input_text('email')
        self.input_text('password')
        self.click()


class SignupPage(Page):
    pass


# from Steps
login_page = LoginPage()
login_page.click()
login_page.login()

sign_up_page = SignupPage()
sign_up_page.verify_text()