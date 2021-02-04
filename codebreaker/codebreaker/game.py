class Game:
    def __init__(self, output):
        self._output_file = output
        self.secret = None

    def start_game(self, secret):
        self.secret = secret
        self.print_message('Welcome to Codebreaker!')
        self.print_message('Enter guess:')

    def print_message(self, output):
           print(output, file=self._output_file)
