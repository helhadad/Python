"""
Script  : Test_app_functions.py
Author  : Hesham Elhadad
ID      : L00177542
Date    : 10-Nov-22
Purpose : This script is used to test the functions implemented in app_functions.py
          as part of assignment_01 solution

Tested  : Python 3.10 on Windows 10 Pro
Rev     : 0
IDE     : PyCharm CE ver 2022

"""
import unittest
import sys
import pathlib as pl

# get main project path
proj_path =pl.Path(__file__).parent.parent
# get lib path 
lib_path = str((proj_path / '../Lib').resolve())
# create a list of paths to be added to sys.path
paths_to_lib = [str(proj_path),lib_path]
# Add folders to sys.path
sys.path[:0]=paths_to_lib
print(sys.path)
from Lib.app_functions import get_substring


class TestFunctions(unittest.TestCase):

    # The following test should pass
    def test_get_substring1(self):
        inp_string = "Welcome to Python"
        pos = 2
        result = get_substring(inp_string, pos)
        self.assertEqual(result, "Python")

    # The following test should fail
    def test_get_substring2(self):
        inp_string = "Welcome to Python"
        pos = 1
        result = get_substring(inp_string, pos)
        self.assertEqual(result, "Python")


if __name__ == "__main__":
    unittest.main()
