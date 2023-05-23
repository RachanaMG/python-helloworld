import unittest
from helloworld import Greeter

class MyTestCase(unittest.TestCase):
    def test_default_greeting_set(self):
        Greeter=Greeter()
        self.assertEqual(Greeter.message, 'Hello world!')

if __name__ == '__main__':
    unittest.main()
