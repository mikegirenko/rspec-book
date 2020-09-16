class Output:

    def __init__(self):
        self._messages = []
        self._output = []

    def messages(self):
        return self._messages

    def puts(self, message):
        self._messages.append(message)

    def output(self, output):
        self._output.append(output)
