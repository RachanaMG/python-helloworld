import unittest
import sys
from io import StringIO

class TestHelloWorld(unittest.TestCase):
def test_print_output(self):
expected_output = "Hello world\n"

# Redirect stdout to a StringIO object
stdout = sys.stdout
sys.stdout = StringIO()

# Run the code that prints "Hello world"
exec(open("your_script.py").read())

# Get the printed output
actual_output = sys.stdout.getvalue()

# Restore stdout
sys.stdout = stdout

# Compare the expected and actual outputs
self.assertEqual(actual_output, expected_output)

if __name__ == '__main__':
unittest.main()
