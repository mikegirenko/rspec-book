class Game:
    def __init__(self):
        self.output_obj = Output()

    def start(self):
        message = "Welcome to Codebreaker!"
        self.output_obj.add_message(message)
        print("printing here", self.output_obj.return_message())

    def guess(self):
        pass


class Output:
    def __init__(self):
        self.messages = []

    def add_message(self, message):
        self.messages.append(message)

    def return_message(self):
        print(("printing within return", self.messages))
        return self.messages
