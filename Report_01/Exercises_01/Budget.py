"""
Script  : Budget.py
By      : Hesham Elhadad
Purpose : This script demonstrates assignment and use of variables in Python with simple calculation

Tested  : Python 3.8 on Windows 10
Rev     : 0

"""
# This program demonstrates basic use of python variables and operators
# The program provides an answer to Walkthroughs-1 "Assignment and Variables" exercise
#
monthly_income = 500
internet_cost = 60
landline_cost = 30
mobile_phone_cost = 40
laptop_cost = 180
stationary = 10
Beverages = 5 * 4 * 4
Fuel = 40 * 4
professional_subscription = 300
# Summing all costs and print them
total_cost = internet_cost + landline_cost + laptop_cost + stationary + mobile_phone_cost + Beverages
print(f"My monthly income           = €{monthly_income}")
print(f"Monthly total expenditures  = €{total_cost}")
# Calculate available cash
available_cash = monthly_income - total_cost
print(f"Monthly available cash      = €{available_cash}")
print("-------------------Budget Report-----------------------")
if available_cash < 100:
    print("You should review your expenses and consider better saving ways")
else:
    print("Your saving plan is good, no action required")
print("-------------------------------------------------------")
