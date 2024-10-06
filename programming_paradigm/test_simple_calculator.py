from simple_calculator import SimpleCalculator
import unittest
class test_calculator(unittest.TestCase):
    def test_addation(self):
        self.assertEqual(SimpleCalculator.add(5,9),14)
        self.assertEqual(SimpleCalculator.add(-8,9),1)
        self.assertEqual(SimpleCalculator.add(12558,95236),12558+ 95236)
    def test_divide(self):
        self.assertEqual(SimpleCalculator.divide(12,2),6)
        self.assertEqual(SimpleCalculator.divide(9,0),None)    
