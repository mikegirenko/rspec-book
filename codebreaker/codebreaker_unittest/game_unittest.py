from unittest import TestCase,  main
from expects import equal, expect

from codebreaker.codebreaker import Game

class GameUnitTest(TestCase):

    def test_game(self):
        game = Game().start()

        expect(game).to(equal("Game started"))


if __name__ == "__main__":
    main()
