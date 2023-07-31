import unittest
from calc import Calc

class TestCalc(unittest.TestCase):

    def setUp(self):
        self.calc = Calc()

    def test_add(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-5, 10), 5)
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(-2, -3), -5)
        self.assertEqual(self.calc.add(100, -50), 50)

    def test_sub(self):
        self.assertEqual(self.calc.sub(2, 3), -1)
        self.assertEqual(self.calc.sub(10, 5), 5)
        self.assertEqual(self.calc.sub(0, 0), 0)
        self.assertEqual(self.calc.sub(10, 20), -10)
        self.assertEqual(self.calc.sub(-5, -2), -3)

    def test_mul(self):
        self.assertEqual(self.calc.mul(2, 3), 6)
        self.assertEqual(self.calc.mul(-5, 10), -50)
        self.assertEqual(self.calc.mul(0, 5), 0)
        self.assertEqual(self.calc.mul(-2, -3), 6)
        self.assertEqual(self.calc.mul(3, 0), 0)

    def test_div(self):
        self.assertEqual(self.calc.div(6, 2), 3)
        self.assertEqual(self.calc.div(10, 5), 2)
        self.assertEqual(self.calc.div(3, 1), 3)
        self.assertEqual(self.calc.div(10, 0), "Error: Cannot divide by zero")
        self.assertEqual(self.calc.div(7, 3), 2.3333333333333335)

    def test_power(self):
        self.assertEqual(self.calc.power(2, 3), 8)
        self.assertEqual(self.calc.power(5, 0), 1)
        self.assertEqual(self.calc.power(-2, 3), -8)
        self.assertEqual(self.calc.power(2, -2), 0.25)
        self.assertEqual(self.calc.power(0, 5), 0)

    def test_factorial(self):
        self.assertEqual(self.calc.factorial(5), 120)
        self.assertEqual(self.calc.factorial(0), 1)
        self.assertEqual(self.calc.factorial(1), 1)
        self.assertEqual(self.calc.factorial(-5), "Error: Factorial is not defined for negative numbers")
        self.assertEqual(self.calc.factorial(10), 3628800)

    def test_sqrt(self):
        self.assertEqual(self.calc.sqrt(9), 3)
        self.assertEqual(self.calc.sqrt(25), 5)
        self.assertEqual(self.calc.sqrt(0), 0)
        self.assertEqual(self.calc.sqrt(-9), "Error: Square root is not defined for negative numbers")
        self.assertEqual(self.calc.sqrt(16), 4)

if __name__ == '__main__':
    unittest.main()
