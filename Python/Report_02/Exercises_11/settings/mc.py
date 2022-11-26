"""
Script  : mc.py
Author  : John O'Raw
          Copied by Hesham Elhadad for testing and studying purpose
ID      : L00177542
Date    : 25-Oct-22
Purpose : This script demonstrates multicast with python as part of walkthrough_11

Tested  : Python 3.10 on Windows 10 Pro
Rev     : 0
IDE     : PyCharm CE ver 2022

"""
MCSERVER = {
 "MCAST_GROUP": '239.1.1.1',
 "IP_ADDRESS": '127.0.0.1',
 "PORT": 5001
}
MCCLIENT = {
 "MCAST_GROUP": '239.1.1.1',
 "IP_ADDRESS": '127.0.0.1',
 "PORT": 5001
}