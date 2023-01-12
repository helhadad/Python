"""
Script  : directory_utilities.py
Author  : John O'Raw
        Copied by Hesham Elhadad for testing and studying purpose
ID      : L00177542
Date    : 25-Oct-22
Purpose : This script demonstrates how to build socket and establish communication 

Tested  : Python 3.10 on Windows 10 Pro
Rev     : 0
IDE     : PyCharm CE ver 2022

"""
import os, platform, sys

# Define global variables
current_working_directory = None


def detect_os() -> str:
    # Detect the OS in use
    return platform.system()


def detect_working_directory() -> str:
    # Returns the directory this script was run from
    return os.getcwd()


if (__name__ == '__main__'):
    print(f"This module executes as a standalone script")

    # Check the OS in use, lower case
    my_os = detect_os()
    my_os = my_os.lower()
    # Parse the response, only check for Windows and Linux
    if my_os == "windows":
        print("Your system is Windows")
    elif my_os == "linux":
        print("Your system is Linux")
    else:
        print(f"Cannot continue, unidentified system = {my_os}")
    sys.exit()
    # Get the current working directory
    current_working_directory = detect_working_directory()
    print(f"You are coding in: {current_working_directory}")
else:
    print(f"This module is called {__name__} and is being called by another script")
