import unittest
from simple_calculator import SimpleCalculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator() 
    
    def test_addition(self):
        self.assertEqual(self.calc.add(5,2),7,)
        self.assertEqual(self.calc.add(0,0),0)
        self.assertEqual(self.calc.add(-2,-1),-3)
        self.assertEqual(self.calc.add(0,-5),-5)
        
    def test_subtraction(self):
        calc = SimpleCalculator()
        self.assertEqual(self.calc.subtraction(4,3),1)
        self.assertEqual(self.calc.subtraction(2,3),-1)
        self.assertEqual(self.calc.subtraction(-2,-5),3)
        self.assertEqual(self.calc.subtraction(-4,3),-7)
        
    def test_division(self):
        self.assertEqual(self.calc.divide(5,0),"None")
        self.assertEqual(self.calc.divide(0,5),0)
        self.assertEqual(self.calc.divide(2,2),1)
        self.assertEqual(self.calc.divide(7,2),3.5)
        self.assertEqual(self.calc.divide(-9,2),-4.5)
        self.assertEqual(self.calc.divide(-7,-2),3.5)
       
    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(5,0),0)
        self.assertEqual(self.calc.multiply(0,5),0)
        self.assertEqual(self.calc.multiply(2,5),10)
        self.assertEqual(self.calc.multiply(-1,5),-5)
        self.assertEqual(self.calc.multiply(-2,-8),16)
    