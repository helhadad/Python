"""
Script  : create_directory.py
By      : Hesham Elhadad
ID      : L00177542
Date    : 22-Oct-22
Purpose : This script demonstrates a sample code to create a directory with
          error handling

Tested  : Python 3.10 on Windows 10
Rev     : 0
IDE     : PyCharm CE ver 2022
"""

import os


def create_directory(directory_name: str) -> bool:
    # Use try/except to catch errors
    try:
        # Create the directory
        os.mkdir(directory_name)
        # If this worked, return True
        return True
    except Exception as e:
        # Give an explicit error message
        print(f"Error creating directory {directory_name}, because of {e}")
        # If this did not work, return False
        return False


# The following is an update to create_directory function that return integer instead
# of string to allow better error messaging.
def create_directory_int(directory_name: str) -> int:
    # Check to see if the directory already exists
    if os.path.isdir(directory_name):
        # The directory already exists
        return 2
    else:
        # Use try/except to catch errors
        try:
            # Create the directory
            os.mkdir(directory_name)
            # If this worked, return True
            return 0
        except:
            # Give an explicit error message
            print(f"Error creating directory {directory_name}")
            # If this did not work, return False
            return 1


# if create_directory("JOR"):
#     print("Creating a directory worked")
#     # Do other stuff
# else:
#     print("You couldn't create a directory!")
#     # Do other stuff

if create_directory_int("JOR") == 0:
    print("Creating a directory worked")
    # Do other stuff
elif create_directory_int("JOR") == 1:
    print("You couldn't create a directory!")
    # Do other stuff
elif create_directory_int("JOR") == 2:
    print("Directory already existed!")
    # Do other stuff
