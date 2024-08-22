from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@then('verify all list items in step3')
def verify(context):
    print(context.list_step1)
    print(context.list_step2)