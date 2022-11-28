"""
Script  : square.py
By      : Hesham Elhadad
Date    : 10/2/2022

Purpose : This script illustrates Python modules and package usability.
          This module comprises only one function

Tested  : Python 3.8 on Windows 10s
Rev     : 0
IDE     : PyCharm CE ver 2022
"""


def square(x):
    return x * x

#  The following code will be executed only if the module is run directly (standalone script)
#  and will be ignored if the module is called by another script by using import
if __name__ == '__main__':
    print("square of (2) = ", square(2))
