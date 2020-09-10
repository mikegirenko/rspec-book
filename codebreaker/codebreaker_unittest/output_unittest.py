from unittest import TestCase, main
from expects import expect, equal

from codebreaker.codebreaker import Output

class OutputUnitTests(TestCase):

    def test_output(self):

        output = Output().message()

        expect(output).to(equal("Welcome to Codebreaker!"))
