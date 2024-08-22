from behave import given, when, then


@then('HW11 Verify "{watch_input}" is found')
def verify_watch_input(context, watch_input):
    context.hw11app.hw11_youtube_page_view.verify_watch_input(watch_input)