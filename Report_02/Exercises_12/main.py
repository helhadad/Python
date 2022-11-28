"""
Script  : main.py
Author  : John O'Raw
        Copied by Hesham Elhadad for testing and studying purpose
ID      : L00177542
Date    : 25-Oct-22
Purpose : This script demonstrates

Tested  : Python 3.10 on Windows 10 Pro
Rev     : 0
IDE     : PyCharm CE ver 2022

"""
from Source.directory_utilities import detect_os, detect_working_directory

print(detect_os())
print(detect_working_directory())
