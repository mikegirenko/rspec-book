from behave import *
from codebreaker import Game, Output


@given('I am not yet playing')
def step_impl(context):
    pass

@when('I start a new game')
def step_impl(context):
    context.game = Game().start()


@then('I should see {message}')
def step_impl(context, message):
    context.message = Output().message()





