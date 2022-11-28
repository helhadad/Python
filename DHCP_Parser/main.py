"""
Script  : main.py
By      : Hesham Elhadad
ID      : L00177542
Date    : 30-Oct-22
Purpose : This script demonstrates a solution to the code problem of assignment-01

Tested  : Python 3.10 on Windows 10
Rev     : 0
IDE     : PyCharm CE ver 2022
"""
import json
import os
import os.path as op
import re
import csv
import logging
from Lib.app_functions import get_path_input, get_path_output
from Lib.mylog import con_handler, file_handler

# Define main module logger and record application start
logger = logging.getLogger('main_app')
# Add console handler
logger.addHandler(con_handler)
# Add file handler
logger.addHandler(file_handler)
# Start application and logging the start
logger.info("Application starts")
# Initialize Node Dictionary which will contains final output
nodeDict = dict()
logger.debug('Initialize node dictionary')
# Initialize mac address data dictionary, which will hold data from mac database.
macData = dict()
logger.debug('Initialize mac-address data dictionary')
# Getting the current dir of the script
current_dir = op.dirname(__file__)
# Preparing the path to the mac database
mac_data_path = op.join(current_dir, 'Lib\\MacDataBase.json')
# Loading json file into Dictionary
try:
    logger.debug("Opening mac data file: %s", mac_data_path)
    with open(mac_data_path, "r") as mac_file:
        macData = json.load(mac_file)
except Exception as e:
    logger.critical("Error opening mac data file, application exits : %s", e)
    logging.shutdown()
    exit(1)
# The following regex will capture and memorize mac address, ip and host name if exists.
regex = r"DHCP.+?(\d+.\d+.\d+.\d+).+?([0-9a-f]+:[0-9a-f]+:[0-9a-f]+:[0-9a-f]+:[0-9a-f]+:[0-9a-f]+)\s?(?:\((.*)\))?"
# Node name prefix (i.e., Node-1, Node-2, )
pref = 1
# Get Log file from the user
dhcp_log_file_path = get_path_input("Enter DHCP Log file path (no quotes) : ")
try:
    logger.debug("Opening DHCP log file for parsing data", )
    with open(dhcp_log_file_path, "r") as inp_file:
        for pos, line in enumerate(inp_file):
            mac_search = re.search(regex, line)
            if mac_search is not None:
                if mac_search.group(3) is None:
                    hostName = ""
                else:
                    hostName = mac_search.group(3)
                if mac_search.group(2) not in nodeDict:
                    nodeDict[mac_search.group(2)] = {"Node": "Node-" + str(pref), "Mac_Address": mac_search.group(2),
                                                     "Ip_Address": mac_search.group(1),
                                                     "Host_Name": hostName}
                    if mac_search.group(2) in macData:
                        if macData[mac_search.group(2)] is not None and macData[mac_search.group(2)] != "":
                            nodeDict[mac_search.group(2)]["Vendor"] = macData[mac_search.group(2)]
                        else:
                            nodeDict[mac_search.group(2)]["Vendor"] = "Not Found"
                    pref += 1
except Exception as Err:
    logger.critical("Error opening DHCP log file: %s", Err)
    logging.shutdown()
    exit(1)
logger.debug("Processing DHCP log file is completed successfully")
# Preparing CSV data
logger.debug("Preparing CSV data")

csv_data = list(nodeDict.values())
# Prepare CSV fields names
fields = list(csv_data[0].keys())
logger.debug("Opening CSV file for writing CSV data")
# Get the CSV output path from the user
csv_file_path = get_path_output("Enter the desired CSV folder (no quotes) : ")
csv_file_name = op.join(csv_file_path,"app_out.csv")
try:
    with open(csv_file_name, 'w', newline='') as outfile:
        csv_writer = csv.DictWriter(outfile, fieldnames=fields)
        csv_writer.writeheader()
        for row in csv_data:
            csv_writer.writerow(row)
except Exception as e:
    logger.critical("Error writing CSV file: %s", Err)
    logging.shutdown()
    exit(1)
logger.info("App completes its work successfully")
