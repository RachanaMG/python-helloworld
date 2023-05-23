import unittest
import sys
from io import StringIO

def hello_world():
    print('Hello world')

class TestHelloWorld(unittest.TestCase):
    def setUp(self):
# Redirect stdout to a StringIO object
        self.stdout = sys.stdout
        sys.stdout = StringIO()

    def tearDown(self):
# Restore stdout
        sys.stdout = self.stdout

    def test_print_output(self):
        expected_output = "Hello world\n"

# Run the code that prints "Hello world"
        hello_world()

# Get the printed output
        actual_output = sys.stdout.getvalue()

# Compare the expected and actual outputs
        self.assertEqual(actual_output, expected_output)

if __name__ == '__main__':
    unittest.main()
