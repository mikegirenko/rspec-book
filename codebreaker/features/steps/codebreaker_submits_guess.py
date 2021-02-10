from behave import *
from expects import expect, contain

from codebreaker import Game
from codebreaker import Output


@given('the secret code is "{secret}"')
def step_impl(context, secret):
    context.output = Output()
    context.game = Game(context.output)
    context.game.start_game(secret)


@when('I guess "{guess}"')
def step_impl(context, guess):
    context.game.guess(guess)


@then('the mark should be "{mark}"')
def step_impl(context, mark):
    expect(context.output.messages()).to(contain(mark))
