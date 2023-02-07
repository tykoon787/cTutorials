import unittest
from circles import circle_area
from math import pi

# Create a Class that is a subclass that is a subclass of the testcase class
class TestCircleArea(unittest.TestCase):
    def def_area(self):
        # Test the Output of the Function with Correct values
        self.assertAlmostEqual(circle_area(1), pi)
        self.assertAlmostEqual(circle_area(0), 0)
        self.assertAlmostEqual(circle_area(2.1), pi * 2.1**2)