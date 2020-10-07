from unittest import TestCase,  main
from expects import equal, expect, contain

from codebreaker.codebreaker import Game

class GameUnitTest(TestCase):

    def test_start(self):
        output = "blah"
        game_obj = Game(output)

        #expect(game_obj.start()).to(contain("Game started"))


if __name__ == "__main__":
    main()
