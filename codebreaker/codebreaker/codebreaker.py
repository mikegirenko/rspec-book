class Game:
    def __init__(self, output):
        self.output = output

    def start_game(self):
        message = "Welcome to Codebreaker!"
        self.message = message
        print(self.message)


class Output():
    def __init__(self):
        self.messages = []

    def write_message(self, message):
        self.messages.append(message)

    def display_message(self):
        output_obj = Output()
        print(output_obj.messages)