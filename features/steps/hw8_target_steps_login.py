from behave import given, when, then
from time import time


@given('HW8 Open sign in page')
def open_sing_in_page(context):
    context.hw8app.hw8_page_login.open_target_sign_login_page()
    # context.hw8app.hw8_page_base.pause_sleep(10)


@when('HW8 Store original window')
def store_original_window(context):
    context.original_window = context.hw8app.hw8_page_base.get_current_window()
    print(f'Original Window: {context.original_window}')


@when('HW8 Click on Target terms and conditions link')
def click_tc_link(context):
    context.hw8app.hw8_page_login.click_tc_link()


@when('HW8 Switch to the newly opened window')
def switch_to_new_window(context):
    context.hw8app.hw8_page_base.switch_to_window()


@then('HW8 Verify Terms and Conditions page is opened')
def verify_tc_opened(context):
    context.hw8app.hw8_page_base.verify_partial_url('/terms-conditions')


@then('HW8 User can close new window and switch back to original')
def close_and_switch_to_original_window(context):
    context.hw8app.hw8_page_base.close_window()
    context.hw8app.hw8_page_base.switch_to_window_by_id(context.original_window)
    context.hw8app.hw8_page_base.verify_partial_url('/login')


# @then('HW8 User can close new window and switch back to original')
# def close_and_switch_to_original_window(context):
#     context.hw8app.hw8_page_login.switch_to_original_window(context.original_window)
