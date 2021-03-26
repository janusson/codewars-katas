# basicUnitTest.py
# below is a unit test template for a sample function, circleArea.py


import unittest
from math import pi

# circleArea.py
# sample function to calculate area of a circle of radius 'r'


def circleArea(r):
    # 'fixes' based on TestCircleArea tests
    # if type(r) not in [int, float]:
    #     raise TypeError('The radius must be a real number.')
    # if r < 0:
    #     raise TypeError('The radius must be greater than zero.')
    from math import pi as pi
    return pi * (r**2)
    radii = [2, 0, -3, 2 + 5j, True, 'radius']

    for r in radii:
        A = circleArea(r)
        print(f'Area of circle with radius r={r} has area A={A}.')


# circleArea_test.py
# Unit test file for a function to calculate circle area, circleArea.py.
# include libraries:
    # import unittest

class TestCircleArea(unittest.TestCase):
    # create a class module that is a subclass of the 'TestCase' class
    # from _.py import _functionName_
    # from math import pi
    # each test method must start with 'test'
    def testArea(self):
        # Test areas when radius >=0
        self.assertAlmostEqual(circleArea(1), pi)
        self.assertAlmostEqual(circleArea(0), 0)
        self.assertAlmostEqual(circleArea(2.1), pi * (2.1**2))

    def testValues(self):
        # check that an exception is raised for Value Errors
        self.assertRaises(ValueError, circleArea, -2)
        # assertRaises(exception class to raise, function, and args for func)

    def testTypes(self):
        # check for type errors
        self.assertRaises(TypeError, circleArea,  3 + 5j)
        self.assertRaises(TypeError, circleArea,  True)
        self.assertRaises(TypeError, circleArea,  'radius')

        # many other assert methods possible!
        # try: import unittest | help(unittest.TestCase.assertSetEqual)
