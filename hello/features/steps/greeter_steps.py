from behave import *
from expects import equal, expect

from hello.features.steps.greeter_object import Greeter


@given('a greeter')
def step_impl(context):
    context.greeter = Greeter()


@when("I send it the greet message")
def step_impl(context):
    context.message = context.greeter.greeter_speaks()


@then('I should see Hello Behave')
def step_impl(context):
    context.message  = context.greeter.greeter_speaks()
    expect(context.message).to(equal("Hello Behave!"))
