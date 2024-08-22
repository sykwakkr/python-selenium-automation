from behave import given, when, then


@when('HW11 Click on search field')
def click_on_search_field(context):
    context.hw11app.hw11_page_main.click_on_search_field()


@when('HW11 Search for {search_input}')
def search_for(context, search_input):
    context.hw11app.hw11_page_main.search_for(search_input)


@then('HW11 Verify first result is {search_input}')
def verify_first_result(context, search_input):
    context.hw11app.hw11_page_main.verify_first_result(search_input)