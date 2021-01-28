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


class Output:
    def __init__(self):
        self._messages_collector = []

    def messages(self):
        return self._messages_collector

    def write(self, message):
        if message != '\n':
            self._messages_collector.append(message)
