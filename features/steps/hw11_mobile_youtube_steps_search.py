from behave import given, when, then


@when('HW11 Search YouTube for "{watch_input}"')
def search_youtube_for(context, watch_input):
    context.hw11app.hw11_youtube_page_search.search_youtube_for(watch_input)
