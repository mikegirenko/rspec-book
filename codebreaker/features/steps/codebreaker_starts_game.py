from behave import *
from expects import expect, contain

from codebreaker.codebreaker import Game, Output


@given('I am not yet playing')
def step_impl(context):
    pass


@when('I start a new game')
def step_impl(context):
    context.output = Output()
    context.game = Game(context.output)
    context.game.start()


@then('I should see "{message}"')
def step_impl(context, message):
    expect(context.output.display_messages()).to(contain(message))
