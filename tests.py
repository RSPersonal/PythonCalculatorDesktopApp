import unittest
from math_operations import MathOperations

class TestMathOperations(unittest.TestCase):
    """Class for testing all the math operations"""

    def test_addition(self):
        """Testing the add function"""
        function = MathOperations.addition(MathOperations, 1, 2)
        self.assertEqual(function, 3)

    def test_substract(self):
        """Testing the substract function"""
        function = MathOperations.subtraction(MathOperations, 10, 5)
        self.assertEqual(function, 5.0)

    def test_check_if_input_empty_or_none(self):
        """Testing for error message"""
        function = MathOperations.check_for_correct_input(MathOperations, '', None)
        self.assertEqual(function, 'Input is empty or NONE')

if __name__ == '__main__':
    unittest.main()
