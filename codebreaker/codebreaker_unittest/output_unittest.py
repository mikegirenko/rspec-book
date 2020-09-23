from unittest import TestCase, main
from expects import expect, equal, contain

from codebreaker.codebreaker import Output

class OutputUnitTests(TestCase):

    def test_messages_returns_message(self):

        expected_message = "Welcome to Codebreaker!"
        output_obj = Output()

        output_obj.puts(expected_message)
        actual_message = output_obj.messages()

        expect(actual_message).to(contain(expected_message))


if __name__ == "__main__":
    main()
