from unittest import TestCase, main
from expects import equal, expect

from hello.features.steps.greeter_object import Greeter


class GreeterUnitTest(TestCase):

    def test_greeter_speaks(self):
        greeter = Greeter()
        message  = greeter.greeter_speaks()
        expect(message).to(equal("Hello Behave!"))


if __name__ == "__main__":
    main()
