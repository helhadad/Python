"""
Script  : mytime.py
By      : Hesham Elhadad
ID      : L00177542
Date    : 23-Oct-22
Purpose : This script demonstrates how time is handled in python via modules and functions.
          The script represents solutions to exercises in walkthrough_10

Tested  : Python 3.10 on Windows 10
Rev     : 0
IDE     : PyCharm CE ver 2022
"""
from datetime import datetime as dt

# Get the current time, returns a value like 2022-10-09 17:46:45.151666
today = dt.now()
print(today)
# Get Unix time, returns a value like 1665566809.057217
unix_epoch_time = dt.timestamp(today)
print(unix_epoch_time)

print("-------------------------------------------------------------")
print("Today is", today.strftime("%A"), today.strftime("%d"), "of", today.strftime("%B"), today.strftime("%Y"))
print("Time now is " + today.strftime("%I") + ":" + today.strftime("%M") + ":" + today.strftime("%S"),
      today.strftime("%p"))
