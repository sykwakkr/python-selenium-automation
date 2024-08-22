from behave import given, when, then


@given('HW11 Click to Skip onboarding')
def click_to_skip(context):
    context.hw11app.hw11_page_onboard.click_to_skip()
