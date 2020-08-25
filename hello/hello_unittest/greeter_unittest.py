from unittest import TestCase, main
from expects import equal

from hello.features.steps.greeter_object import Greeter

class GreeterUnitTest(TestCase):
    def test_my_test(self):
        greeter = Greeter()
        print(greeter.greeter_speaks())


if __name__ == "__main__":
    main()
