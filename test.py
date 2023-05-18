import unittest

class TestSum(unittest.TestCase):
    def test_sum(self):
        num1 = 5
        num2 = 10
        expected_sum = num1 + num2
        actual_sum = num1 + num2
        self.assertEqual(expected_sum, actual_sum)
        
if __name__ == '__main__':
    unittest.main()
