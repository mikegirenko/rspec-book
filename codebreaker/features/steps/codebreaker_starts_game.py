from behave import *
from expects import expect, contain

from codebreaker import Game
from codebreaker import Output


@given('I am not yet playing')
def step_impl(context):
    pass


@when('I start a new game')
def step_impl(context):
    context.output = Output()
    context.game = Game(context.output)
    context.game.start_game('1234')


@then('I should see "{message}"')
def step_impl(context, message):
    expect(context.output.messages_collector()).to(contain(message))
