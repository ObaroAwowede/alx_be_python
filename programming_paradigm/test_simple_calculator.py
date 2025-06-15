import unittest
from simple_calculator import SimpleCalculator

class TestCalculator(unittest.TestCase):
    
    def test_addition(self):
        calculator = SimpleCalculator()
        self.assertEqual(calculator.add(5,2),7,)
        self.assertEqual(calculator.add(0,0),0)
        self.assertEqual(calculator.add(-2,-1),-3)
        self.assertEqual(calculator.add(0,-5),-5)
        
    def test_division(self):
        calculator = SimpleCalculator()
        self.assertEqual(calculator.divide(5,0),"None")
        self.assertEqual(calculator.divide(0,5),0)
        self.assertEqual(calculator.divide(2,2),1)
        self.assertEqual(calculator.divide(7,2),3.5)
        self.assertEqual(calculator.divide(-9,2),-4.5)
        self.assertEqual(calculator.divide(-7,-2),3.5)
       
    def test_multiplication(self):
        calculator = SimpleCalculator()
        self.assertEqual(calculator.multiply(5,0),0)
        self.assertEqual(calculator.multiply(0,5),0)
        self.assertEqual(calculator.multiply(2,5),10)
        self.assertEqual(calculator.multiply(-1,5),-5)
        self.assertEqual(calculator.multiply(-2,-8),16)
    
    def test_subtraction(self):
        calculator = SimpleCalculator()
        self.assertEqual(calculator.subtraction(4,3),1)
        self.assertEqual(calculator.subtraction(2,3),-1)
        self.assertEqual(calculator.subtraction(-2,-5),3)
        self.assertEqual(calculator.subtraction(-4,3),-7)