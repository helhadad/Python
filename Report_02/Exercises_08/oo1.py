"""
Script  : oo1.py
Author  : Hesham Elhadad
ID      : L00177542
Date    : 20-Oct-22
Purpose : This script demonstrates a solution to the exercises of walkthrough_08 and exhibit object oriented programming

Tested  : Python 3.10 on Windows 10 Pro
Rev     : 0
IDE     : PyCharm CE ver 2022

"""

import time


# Create a class
class JORzClass():

    # Constructor, called whenever an instance of the class is created.
    def __init__(self, my_greeting):
        print("Running constructor for JORzClass")
        # Create attributes and set initial values
        self.message = my_greeting

    def my_method(self):
        print(self.message)


# my_class1 = JORzClass("Morning JOR!")
# my_class1.my_method()
# print(type(my_class1))


# Define a class called Monitor to capture and instantiate different instances
class Monitor:

    def __init__(self, size, resolution, year_of_manufacturing):
        self.year_of_manufacturing = year_of_manufacturing
        self.size = size
        self.resolutions = resolution

    # The following method could be used to calculate the monitor age
    def get_monitor_age(self) -> int:
        return time.localtime().tm_year - self.year_of_manufacturing

    # using the previous method, another method can detect if an upgrade is required.
    def need_upgrading(self):
        if self.get_monitor_age() > 5:
            print(f"This monitor is old enough and needs an upgrade")
        else:
            print(f"The monitor is still in service period")


lap_monitor = Monitor(24, "HD", 2020)
print(f"lap_monitor is {lap_monitor.get_monitor_age()} years old")
lap_monitor.need_upgrading()
student_monitor = Monitor(27, "FHD", 2010)
print(f"student_monitor is {lap_monitor.get_monitor_age()} years old")
student_monitor.need_upgrading()
