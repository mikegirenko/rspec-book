class Output:
    def __init__(self):
        self.messages = []

    def output_message(self):
        return self.messages

    def add_message(self, message):
        self.messages.append(message)


