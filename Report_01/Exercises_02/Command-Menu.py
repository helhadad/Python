"""
Script  : Command-Menu.py
By      : Hesham Elhadad
Purpose : This script provides a menu of 6 commands, where a user can select any by entering command number
          However, the script has neither validation nor error handling logic, therefore valid input is expected.

Tested  : Python 3.8 on Windows 10
Rev     : 0

"""

print("------------------------------------------------------------")
print("[1] - Command 1               [4] - Command 4 ")
print("[2] - Command 2               [5] - Command 5 ")
print("[3] - Command 3               [6] - Command 6 ")
print("[7] - Command 7               [8] - Command 8 ")
print("[0] - Exit                                                   ")

choice = input("Select command by entering asociated number (i.e. 1 or 2 or 4 etc...) : ")
print("")
while choice != "0":
    if choice == "1":
        print("You have selected command 1")
        # Do something here
        break
    elif choice == "2":
        print("You have selected command 2")
        # Do something here
        break
    elif choice == "3":
        print("You have selected command 3")
        # Do something here
        break
    elif choice == "4":
        print("You have selected command 4")
        # Do something here
        break
    elif choice == "5":
        print("You have selected command 5")
        # Do something here
        break
    elif choice == "6":
        print("You have selected command 6")
        # Do something here
        break
    elif choice == "7":
        print("You have selected command 7")
        # Do something here
        break
    elif choice == "8":
        print("You have selected command 8")
        # Do something here
        break
else:
    print("Good bye .... ")
