class Game:
    def __init__(self, output):
        self.output = output

    def start(self):
        print("Welcome to Codebreaker!")
        print("Enter guess:")


class Output():
    def __init__(self):
        self._messages = []

    def write_message(self, message):
        self._messages.append(message)

    def display_messages(self):
        return self._messages
