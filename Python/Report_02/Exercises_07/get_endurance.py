"""
Script  : Exercise_07.py
Author  : Hesham Elhadad
ID      : L00177542
Date    : 20-Oct-22
Purpose : This script demonstrates a solution to the exercise in walkthrough_07.
          The script will calculate endurance in minutes of a backup diesel generator

Tested  : Python 3.10 on Windows 10 Pro
Rev     : 0
IDE     : PyCharm CE ver 2022

"""


# The following function will read string from input, convert to float and validate that
def get_float_input(message) -> float:
    while True:
        try:
            x = float(input(message))
        except ValueError:
            print("Wrong value entered! please enter a float number ")
        else:
            return x
            # break


# Getting the available fuel from operator
available_fuel = get_float_input("Enter available fuel in litres : ")
# Getting the engine fuel consumption from operator
fuel_consumption = get_float_input("Enter available fuel consumption in litres/min : ")


# The following function will calculate remaining endurance in minutes using available fuel and engine consumption
def get_diesel_generator_endurance(fuel, consumption):
    try:
        endurance = fuel / consumption
    except ZeroDivisionError:
        print("-------------------------------------------------------------------------------------")
        print("It seems your diesel backup engine is idle, the flowmeter cannot calculate fuel flow")
    else:
        print("-------------------------------------------------------------------------------------")
        print(f"Available fuel = {fuel} Lites\nBackup generator consumption = {consumption} Litres/min"
              f"\nEstimated endurance in minutes = {endurance:4.2f} minutes")


get_diesel_generator_endurance(available_fuel, fuel_consumption)
