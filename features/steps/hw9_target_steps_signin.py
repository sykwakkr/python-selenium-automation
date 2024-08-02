from behave import given, when, then


@given('HW9 Open Target sign in page')
def open_target_sign_in_page(context):
    context.hw9app.hw9_page_signin.open_sign_in_page()


@when('HW9 Enter incorrect email and password combination')
def enter_incorrect_email_and_password(context):
    context.hw9app.hw9_page_signin.enter_incorrect_email_and_password()


@when('HW9 Click login button')
def click_login_button(context):
    context.hw9app.hw9_page_signin.click_sign_in_button()


@then("HW9 Verify that '{alert}' alert message is shown")
def verify_login_alert_message(context, alert):
    context.hw9app.hw9_page_signin.verify_signin_alert_message(alert)
