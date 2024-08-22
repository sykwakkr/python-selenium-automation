from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@when('add items in a list in step1')
def add_items_in_list_in_step1(context):
    context.list_step1 = ["step1_a", "step1_b", "step1_c"]
    print(f'{context.list_step1} in step1')

