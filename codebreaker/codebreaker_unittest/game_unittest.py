from unittest import TestCase
from expects import equal, expect, contain

from codebreaker.codebreaker import Game, Output


class GameUnitTest(TestCase):

    def test_start_sends_welcome_message(self):
        output_obj = Output()
        game_obj = Game()
        game_obj.start()
        print("printing", output_obj.return_message())
        #expect(output_obj.messages).to(contain('Welcome to Codebreaker!'))
