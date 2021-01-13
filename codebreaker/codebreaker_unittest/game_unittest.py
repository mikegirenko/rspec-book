from unittest import TestCase
from expects import equal, expect, contain

from codebreaker.codebreaker import Game


class GameUnitTest(TestCase):

    def test_start_game_sends_welcome_message(self):
        game_obj = Game()
        game_obj.start_game()
        expect(game_obj.message).to(contain('Welcome to Codebreaker!'))
