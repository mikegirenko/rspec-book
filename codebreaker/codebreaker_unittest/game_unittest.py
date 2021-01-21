from unittest import TestCase
from expects import equal, expect, contain

from codebreaker.codebreaker import Game, Output


class GameUnitTest(TestCase):

    def test_start_game_sends_welcome_message(self):
        message = 'Welcome to Codebreaker!'
        output_obj = Output()
        game_obj = Game(output_obj.write_message(message))
        game_obj.start()
        expect(game_obj.output).to(contain(message))

    # def test_start_game_prompts_for_first_guess(self):
    #     message = 'Enter guess:'
    #     game_obj = Game(message)
    #     game_obj.start()
    #     expect(game_obj.output).to(contain(message))
