from behave import *


@given('greeter exists')
def step_impl(context):
    pass


@when('greeter receives greet() message')
def step_impl(context):
    assert True is not False


@then('greeter says Hello')
def step_impl(context):
    print("Hello!")