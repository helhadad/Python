"""
Script  : Flow_Control.py
By      : Hesham Elhadad
Date    : 30-Sep-22
Purpose : This script illustrates Python flow control and provides answers to Walkthrougs-4 exercises

Tested  : Python 3.8 on Windows 10
Rev     : 0
IDE     : PyCharm CE ver 2022
"""
# if ...elif... else block is used to branch script execution according to logic provided in each section
# Exercise 1
#  All is True
a = True
b = True
c = True
if a:
    print("a was True")
elif b:
    print("b was True")
elif c:
    print("c was True")
else:
    print("None of our boolean variables were True")
#  A is False
a = False
b = True
c = True
if a:
    print("a was True")
elif b:
    print("b was True")
elif c:
    print("c was True")
else:
    print("None of our boolean variables were True")
# C is True
a = False
b = False
c = True
if a:
    print("a was True")
elif b:
    print("b was True")
elif c:
    print("c was True")
else:
    print("None of our boolean variables were True")
# --------------------------------------- L O O P S ------------------------------------------------------
#  for loop is used to run over items in collections or range
for x in range(0, 11):
    if x == 6:
        continue
    print(x)

fruits = ['Apple', 'Orange', 'Banana', 'Mango', 'Pears']
for x in fruits:
    if x == "Mango":
        break
    print(x)

scan = {"192.168.3.10": "80", "192.168.3.11": "443", "192.168.3.55": "22"}
for ipv4, port in scan.items():
    print(f"Found a service on {ipv4} at {port}")

# -------------------------------- L I S T  C O M P R E H E N S I I O N --------------------------
# Answer to exercise
# Creating a list of 10 Kelvin degrees
Kelvin = list(range(0, 100, 10))
# Using list comprehension to create a list of relevant Celsius degrees
Celsius = [k - 273.15 for k in Kelvin]
# Using list comprehension to create a list of relevant Fahrenheit degrees
Fahrenheit = [((k - 273.15) * 1.8) + 32 for k in Kelvin]
# Adding the three degrees lists in a Zip object
temp = zip(Kelvin, Celsius, Fahrenheit)

print("-----------------------------------")
print("Kelvin  |  Celsius  |  Fahrenheit")
print("-----------------------------------")
for k, c, h in temp:
    print(f"{k:5.2f}K° | {c:5.2f}C° | {h:5.2f}F°")
