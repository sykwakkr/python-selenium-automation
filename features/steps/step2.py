from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when('add items in a list in step2')
def add_items_in_list_in_step2(context):
    context.list_step2 = ["step2_a", "step2_b", "step2_c"]
    print(f'{context.list_step2} in step2')


@when('add step1_items in step2_list')
def add_step1_items_in_step2(context):
    context.list_step1.extend(context.list_step2)
    print(f'{context.list_step2} in extend in step2')
    print(f'{context.list_step1} in extend in step2')
