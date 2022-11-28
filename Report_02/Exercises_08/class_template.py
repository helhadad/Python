"""
Script  : class_template.py
By      : Hesham Elhadad
ID      : L00177542
Date    : 22-Oct-22
Purpose : This script demonstrates a personal class template to be used in other scripts

Tested  : Python 3.10 on Windows 10
Rev     : 0
IDE     : PyCharm CE ver 2022
"""


class BaseClass:
    # Define global attributes of the all objects
    const1 = None
    const2 = None

    # define instance attributes including private ones
    def __init__(self):
        self.attr1 = None
        self.attr2 = None
        self.attr3 = None
        self._hidden_attr = None

    def get_hidden_attr(self):
        return self._hidden_attr

    def set_hidden_attr(self, value):
        self._hidden_attr = value


# Test instantiating base class
myObject_1 = BaseClass()
# Test attr1 of class instance
print(f"Instance attribute attr1 value  = {myObject_1.attr1}")
print(f"Instance private attribute value  = {myObject_1.get_hidden_attr()}")
# Test setting class private attribute
myObject_1.set_hidden_attr(23)
print(f"Instance private attribute updated value  = {myObject_1.get_hidden_attr()}")

