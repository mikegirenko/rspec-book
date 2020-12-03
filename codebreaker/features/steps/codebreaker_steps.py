from behave import *
from expects import expect, contain

from codebreaker import Game, Output


@given('I am not yet playing')
def step_impl(context):
    game_obj = Game()
    game_obj.start_game()

@when('I start a new game')
def step_impl(context):
    pass