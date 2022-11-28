"""
Script  : Datastructure.py
By      : Hesham Elhadad
Purpose : This script illustrates examples of Python data structure and their uses.

Tested  : Python 3.8 on Windows 10
Rev     : 0
IDE     : PyCharm CE ver 2022
"""
# The following data structure will be tested :
# 1-Lists
# 2-Tuples
# 3-Sets
# 4-Dictionaries

# ---------------------------------------------------- L I S T S -----------------------------------------------
# A List is an ordered mutable collection of items of any data types
#  a is a list comprises integers.
a = [1, 2, 3, 4, 5, 6]

print(a)
print(len(a))
#  Another integer list
b = [7, 8, 9]
print(b)
#  Lists can be concatenated same like strings using + operator
#  Lists may comprise heterogeneous types however it is uncommon practice
c = a + b
print(c)
#  List comprehension is one of the pythonic way to create lists
#  The following list comprehension produces a list of elements found in range (5)
d_list = [x for x in range(5)]
print(d_list)

# ---------------------------------------------------- T U P L E S -----------------------------------------------
# A tuple is an immutable collection of items and shares some of the list properties
# tuple can be created by many ways :
# tuple by comma separated values
tupa = 1, 2, 3
# tuple by series of items between round brackets
tup_b = ('a', 'b', 'c', 'd', 'e', 'c')
# tuple by converting iterable using built-in tuple(iterable) function
tup_c = tuple(d_list)
print(tup_c)
v = tup_c.count(a)
# Unlike lists tuples have only two methods
# Retrieve the first index of an element in a tuple
tup_b_index = tup_b.index('c')
print(f"First index of 'c' in tup_b =  {tup_b_index}")
# Retrieving element in tup by its index (like list)
print(f"tup_b[2]  = {tup_b[2]}")

# the following try/exception block is to verify that tuples are immutable
try:
    tup_b[2] = 'v'
    print(f"Reading the new value of tup_b[2]  = {tup_b[2]}")

except TypeError:
    print("--------------------")
    print("Type errors happened because tuples are immutable")
    print("--------------------")
# Count the occurrence of an element in a tuple
freq_of_c_in_tup_b = tup_b.count('c')
print(f"Count of 'c' in tup_b = {freq_of_c_in_tup_b}")

# ---------------------------------------------------- D I C T I O N A R I E S-----------------------------------------
# A Dictionary is another type of collection of key, value pairs. Dictionaries are similar to hash tables and maps
# in other languages.

# A dictionary can be created by assigning key-value paris between curly brackets to a variable
dict_a = {"First": 1, "Second": 2, "Third": 3}
# Unlike lists, strings, and tuples, dictionaries are accessed by key not index.
print(f'Read the value of dict_a["First"] =  {dict_a["First"]}')  # to be able to use f-string, different quotes is must

# List of a dictionary will generate a list of the dictionary keys
dic_a_keys = list(dict_a)
print(dic_a_keys)
# A dictionary can also be created by using dict() built-in function
dict_b = dict([("Fourth", 4), ("Fifth", 5), ("Sixths", 6)])
# items method will return dictionary key,value pairs
for k, v in dict_a.items():
    print(f'dict_a[{k}]={v}')
# ----------------------------------------------------SETS-------------------------------------------------
#  Sets are another type of items collections, however, it maintains unique items only.
#  Set created by collection of items between curly bracket
set_1 = {1, 2, 3, 4, 5}
print(type(set_1))
# Set can be also be created by using built-in function set(iterable), which will ignore duplicates
list_1 = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6]
# converting list to set will eliminate duplicate elements
listSet = set(list_1)
print(listSet)
