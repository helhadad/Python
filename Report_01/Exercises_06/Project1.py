"""
Script  : Project1.py
By      : Hesham Elhadad
Date    : 10/2/2022
Purpose : This script illustrates Python modules and package import

Tested  : Python 3.8 on Windows 10
Rev     : 0
IDE     : PyCharm CE ver 2022
"""
import mylib.square as mysquare
import mylib.cube as mycube

print("Calling square (3) from mylib.square  = ", mysquare.square(3))
print("Calling cube (2) from mylib.square  = ", mycube.cube(2))
