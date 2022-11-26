"""
Script  : test_Area_calc.py
By      : Hesham Elhadad
ID      : L00177542
Date    : 23-Oct-22
Purpose : This script demonstrates the ability of using unittest as shown in walkthrough_9

Tested  : Python 3.10 on Windows 10
Rev     : 0
IDE     : PyCharm CE ver 2022
"""
import unittest
import Area_calc


class Testget_area(unittest.TestCase):
    def test_square(self):
        side = 5
        result = Area_calc.Square(side).get_area()
        self.assertEqual(result, 25)

    def test_rectangle(self):
        length = 10
        width = 4
        result = Area_calc.Rectangle(length, width).get_area()
        self.assertEqual(result, 40)

    # As circle area is bases on pi which is an approximate number, assertAlmostEqual is required for just one place
    def test_circle(self):
        radius = 10
        result = Area_calc.Circle(radius).get_area()
        self.assertAlmostEqual(result, 314.15, places=1)


if __name__ == "__main__":
    unittest.main()
