from simple_calculator import SimpleCalculator
import unittest

class TestCalculator(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(SimpleCalculator.add(5, 9), 14)
        self.assertEqual(SimpleCalculator.add(-8, 9), 1)
        self.assertEqual(SimpleCalculator.add(12558, 95236), 12558 + 95236)

    def test_divide(self):
        self.assertEqual(SimpleCalculator.divide(12, 2), 6)
        # Check if SimpleCalculator handles division by zero correctly
        with self.assertRaises(ZeroDivisionError):
            SimpleCalculator.divide(9, 0)

if __name__ == '_main_':
    unittest.main()