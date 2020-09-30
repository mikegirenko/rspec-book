class Output:

    def __init__(self):
        self._messages = []

    def puts(self, message):
        self._messages.append(message)

    def output(self):
        return self._messages
