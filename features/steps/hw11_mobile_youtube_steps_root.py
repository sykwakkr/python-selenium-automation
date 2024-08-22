from behave import given, when, then


@given('HW11 Click search field for watch')
def click_search_field_for_watch(context):
    context.hw11app.hw11_youtube_page_root.click_search_field_for_watch()