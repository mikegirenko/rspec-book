from unittest import TestCase,  main
from expects import equal, expect, contain

from codebreaker.codebreaker import Game, Output


class GameUnitTest(TestCase):

    def test_start_sends_welcome_message(self):
        output_obj = Output()
        game_obj = Game(output_obj)
        game_obj.start()
        expect(output_obj.output_message()).to(contain('Welcome to Codebreaker!'))

    def test_guess_prompts_for_first_guess(self):
        pass