from behave import given, when, then


@given('HW9 Open Return & Exchange help topic page')
def open_return_and_exchange_help_topic(context):
    context.hw9app.hw9_page_help.open_help_topics_return_page()


@when('HW9 Select "{option}" topic page')
def select_orders_purchases_topic(context, option):
    context.hw9app.hw9_page_help.select_option_topic(option)


@then('HW9 Verify the correct "{option}" page opened')
def verify_correct_option_page(context, option):
    context.hw9app.hw9_page_help.verify_correct_option_page(option)
