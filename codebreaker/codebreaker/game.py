from codebreaker.codebreaker import output

class Game:
    def __init__(self):
        self.output_obj = output.Output()

    def start(self):
        message = "Welcome to Codebreaker!"
        self.output_obj.add_message(message)
        self.output_obj.output_message()

    def guess(self):
        pass