from sys import stdout

from codebreaker.codebreaker.game import Game


class PlayCodeBreaker:
    game_object = Game(stdout)
    game_object.start_game("1234")
