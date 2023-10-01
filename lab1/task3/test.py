import unittest

from main import SquareCalculator


class TestTask3(unittest.TestCase):
    def setUp(self):
        self.calculator = SquareCalculator()

    def test_calculate_square(self):
        self.assertEqual(self.calculator.calculate(1.2, 1.3), 1.56)

    def test_invalid_values(self):
        with self.assertRaises(ValueError) as context:
            self.calculator.calculate('', 1)
        self.assertEqual(str(context.exception), 'Invalid height argument')

        with self.assertRaises(ValueError) as context:
            self.calculator.calculate(1, '')
        self.assertEqual(str(context.exception), 'Invalid width argument')

        with self.assertRaises(ValueError) as context:
            self.calculator.calculate(1, -1)
        self.assertEqual(str(context.exception), 'Invalid width argument')


