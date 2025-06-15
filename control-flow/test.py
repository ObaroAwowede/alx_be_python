import unittest

def div(x,num):
    for i in range(0,num):
        product = x ** num
    print("The answer is ", product) 
    
myfile = open("/Users/mac/Desktop/alx_be_python/control-flow/bp.txt")
print(myfile.read())
div(6,3)
    
class TestPower(unittest.TestCase):
    def TestPowerPositive(self):
        answer = div(3,3)
        self.assertEqual(answer,27)
        
    def TestPowerNegative(self):
        answer = div(2,-2)
        self.assertEqual(answer,0.25)
        
