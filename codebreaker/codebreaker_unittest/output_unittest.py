from unittest import TestCase, main
from expects import expect, equal

from codebreaker.codebreaker import Output

class OutputUnitTests(TestCase):

    def test_messages(self):

        output = Output().messages()

        expect(output).to(equal("Welcome to Codebreaker!"))


if __name__ == "__main__":
    main()
