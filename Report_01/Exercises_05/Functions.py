"""
Script  : Functions.py
By      : Hesham Elhadad
Date    : 10/1/2022
Purpose : This script illustrates Python flow control and provides answers to Walkthrougs-4 exercises

Tested  : Python 3.8 on Windows 10
Rev     : 0
IDE     : PyCharm CE ver 2022
"""


# ------------------------------------- E x e r c i s e   A n s w e rs--------------------------------------------------

# A function which test if an integer is divisible by another integer
def divisible(numerator: int, denominator: int) -> bool:
    # Check if there is no left over after integer division, hence the numerator is divisible by the denominator
    return numerator % denominator == 0


# By dividing 30 by 5, the remaining == 0
print(divisible(30, 5))


# A function which return True if it finds numer in a list of numbers
def find_num(number_list: list, number: int) -> bool:
    # Loop for every item in the number_list
    for iterate_number in number_list:
        if iterate_number == number:
            return True
        else:
            pass  # There is no return statement in the else branch, hence the function will return None.


# Calling find_num with arguments which return None
result = find_num([1, 2, 3, 4, 5, 6, 7, 8], 9)
# The function will return None as this is the initial value of iterate_number
print("Searching for 9 in [1,2,3,4,5,6,7,8] returns --> ", result)

# Calling find_num with arguments which return True
result = find_num([1, 2, 3, 4, 5, 6, 7, 8], 5)
# The function will return None as this is the initial value of iterate_number
print("Searching for 5 in [1,2,3,4,5,6,7,8] returns -->", result)


#  Another version of find_num which returns False in case number is not found
def find_num_mod(number_list: list, number: int) -> bool:
    found = False
    for iterate_number in number_list:
        if iterate_number == number:
            found = True
        else:
            pass
    return found


print()
print("-------------------------------------------------------------------------------------------------")
print("Calling the modified version of find_num, which will return False instead of None")
print("-------------------------------------------------------------------------------------------------")
# Calling find_num_mod with arguments which return False instead of None
result = find_num_mod([1, 2, 3, 4, 5, 6, 7, 8], 9)
print("Searching for 9 in [1,2,3,4,5,6,7,8] returns --> ", result)
# The function will return None as this is the initial value of iterate_number


# Calling find_num
result = find_num_mod([1, 2, 3, 4, 5, 6, 7, 8], 5)
# The function will return None as this is the initial value of iterate_number
print("Searching for 5 in [1,2,3,4,5,6,7,8] returns -->", result)

print()
print("-------------------------------------------------------------------------------------------------")
print("Calling of find_even, which will return True if a list has even number and False if has not")
print("-------------------------------------------------------------------------------------------------")


def find_even(number_list: list) -> bool:
    found = False
    for iterate_number in number_list:
        if iterate_number % 2 == 0:
            found = True
        else:
            pass
    return found


# Test of find_even
result = find_even([1, 2, 3, 4, 4, 5, 6, 7, 8, 9, 10])
print("Searching for even number in [1,2,3,4,4,5,6,7,8,9,10] returns --> ", result)
result = find_even([1, 3, 5, 7, 9, 11, 13, 15, 7, 19])
print("Searching for even number in [1, 3, 5, 7, 9, 11, 13, 15, 7, 19] returns --> ", result)


print()
print("-------------------------------------------------------------------------------------------------")
print("A lambda function to calculate the volume of a cylinder : ")
print("cylinder_volume = lambda r, h: 3.14 * (r ** 2) * h")
print("-------------------------------------------------------------------------------------------------")

# A lambda function to calculate cylinder volume
cylinder_volume = lambda r, h: 3.14 * (r ** 2) * h
print(f"The Volume of a cylinder of 4 cm radius and 5 cm height = {cylinder_volume(4, 5):6.3f} cm³")
