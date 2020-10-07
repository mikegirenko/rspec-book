class Game:
    def __init__(self, output):
        self._output = output

    def start(self):
        self.print('Welcome to Codebreaker!')
        self.print('Enter guess:')

    def print(self, output):
        print(output)