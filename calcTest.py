# To run type "python3 calcTest.py"

import unittest
from calculator import *

class TestCalculatorOps(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2,4), 6)
        self.assertEqual(add(23, 87), 110)
        self.assertEqual(add(-32, -2),-34)
    def test_sub(self):
        self.assertEqual(sub(2,4), -2)
        self.assertEqual(sub(200,50), 150)
        self.assertEqual(sub(20,-10), 30)
    def test_mul(self):
        self.assertEqual(mul(6,10), 60)
        self.assertEqual(mul(6,-10), -60)
        self.assertEqual(mul(20,10), 200)
    def test_div(self):
        self.assertEqual(div(36,6), 6)
        self.assertEqual(div(10000, 5), 2000)
        self.assertEqual(div(-100,10), -10)
        self.assertEqual(div(100,0), "Error!")


if __name__ == "__main__":
    unittest.main()
