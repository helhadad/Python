"""
Script  : test_import.py
Author  : Hesham Elhadad
ID      : L00177542
Date    : 05-Nov-22
Purpose : This script demonstrates

Tested  : Python 3.10 on Windows 10 Pro
Rev     : 0
IDE     : PyCharm CE ver 2022

"""

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