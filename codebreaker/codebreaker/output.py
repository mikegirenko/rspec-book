class Output:
    def __init__(self):
        self._messages = []

    def messages_collector(self):
        return self._messages

    def write(self, message):
        if message != '\n':
            self._messages.append(message)
