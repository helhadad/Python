"""
Script  : main.py
By      : Hesham Elhadad
ID      : L00177542
Date    : 22-Oct-22
Purpose : This script demonstrates a solution to exercises of walkthrough_08

Tested  : Python 3.10 on Windows 10
Rev     : 0
IDE     : PyCharm CE ver 2022
"""
from devices import Firewall
from devices import Switch
from devices import LoadBalancer

# Create a firewall instance
firewall27 = Firewall("firewall27")
# Configure it
firewall27.configure_firewall()

# Create a firewall instance
firewall28 = Firewall("firewall28")
# Verify a CRC
firewall28.calculate_crc("dummy data")
"""
The following is the student code 
"""
# Create a 16 port switch instance
print("---------------------------------------------------------------------------")
print("                       Creating and configuring a 16 port switch")
print("---------------------------------------------------------------------------")
switch_16 = Switch("Room_01", 16, 3)
# Configure the switch
switch_16.configure_switch()
# Verify a CRC
switch_16.calculate_crc("test")
print("this is to confirm the access of the abstract class (Devices) attribute pi = ", switch_16.pi)

# Create a load balancer instance
print("---------------------------------------------------------------------------")
print("                       Creating and configuring a load balancer")
print("---------------------------------------------------------------------------")
load_balancer_01 = LoadBalancer("LB_01", "1st Tier", 7)
# Configure the switch
load_balancer_01.configure_loadbalancer()
# Verify a CRC
load_balancer_01.calculate_crc("test")
print("this is to confirm the access of the abstract class (Devices) attribute pi = ", switch_16.pi)
