from unittest import TestCase
from expects import expect, contain

from codebreaker.codebreaker.game import Game
from codebreaker.codebreaker.output import Output


class TestGame(TestCase):
    def setUp(self) -> None:
        self.output_obj = Output()
        self.game_obj = Game(self.output_obj)

    def test_start_sends_welcome_message(self):
        expected_message = 'Welcome to Codebreaker!'
        self.game_obj.start_game("1234")
        expect(self.output_obj.messages()).to(contain(expected_message))

    def test_start_prompts_for_first_guess(self):
        expected_message = 'Enter guess:'
        self.game_obj.start_game("4321")
        expect(self.output_obj.messages()).to(contain(expected_message))
