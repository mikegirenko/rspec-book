from unittest import TestCase, main
from expects import expect, equal, be_empty, contain

from codebreaker.codebreaker import Output

class OutputUnitTests(TestCase):

    def test_class_returns_empty_messages_when_nothing_to_return(self):

        returned_message  = Output().output()
        expect(returned_message).to(be_empty)

    def test_messages_returns_message(self):

        expected_message = "Welcome to Codebreaker!"
        output_obj = Output()

        output_obj.puts(expected_message)
        actual_message = output_obj.output()

        expect(actual_message).to(contain(expected_message))


if __name__ == "__main__":
    main()
