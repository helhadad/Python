"""
Script  : Area_calc.py
By      : Hesham Elhadad
ID      : L00177542
Date    : 23-Oct-22
Purpose : This script demonstrates functions for calculating area of some geometric shapes.
          The script will be tested by unittest

Tested  : Python 3.10 on Windows 10
Rev     : 0
IDE     : PyCharm CE ver 2022
"""
from abc import ABC, abstractmethod


# Creat abstract class to define the base of a geometric figures
# The base class will maintain fixed pi value
class Figure(ABC):
    pi = 3.141592

    def __init__(self):
        super().__ini__()

    @abstractmethod
    def get_area(self):
        pass


# Create circle class to represent circle instances
class Circle(Figure):
    def __init__(self, radius):
        self.raduis = radius

    def get_area(self):
        return self.pi * self.raduis * self.raduis


# Create rectangle class to represent rectangle instances
class Rectangle(Figure):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_area(self):
        return self.length * self.width


# Create square class to represent square instances
class Square(Figure):
    def __init__(self, side_length):
        self.side_length = side_length

    def get_area(self):
        return self.side_length * self.side_length


#
#  Instantiate some instances
#
circle_a = Circle(7)
print("Area of circle A = ", circle_a.get_area())

rectangle_b = Rectangle(10, 5)
print("Area of rectangle b  =", rectangle_b.get_area())

square_c = Square(4)
print("Area of square_c  =", square_c.get_area())
