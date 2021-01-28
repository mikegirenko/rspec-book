class Output:
    def __init__(self):
        self._messages_collector = []

    def messages(self):
        return self._messages_collector

    def write(self, message):
        if message != '\n':
            self._messages_collector.append(message)
