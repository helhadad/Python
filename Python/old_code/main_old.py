"""
Script  : main.py
By      : Hesham Elhadad
ID      : L00177542
Date    : 30-Oct-22
Purpose : This script demonstrates 

Tested  : Python 3.10 on Windows 10
Rev     : 0
IDE     : PyCharm CE ver 2022
"""
import re

# sys.path.append("../Source")


import Source as mlog

# Initialize Node Dictionary which will contains final output
nodeDict = dict()
# Initialize mac address data dictionary, which will hold data from mac database.
macData = dict()

# logging.basicConfig(filename='myapp.log', level=logging.WARNING)

# The following regex will capture and memorize mac address, ip and host name if exists.
regex = r"DHCP.+?(\d+.\d+.\d+.\d+).+?([0-9a-f]+:[0-9a-f]+:[0-9a-f]+:[0-9a-f]+:[0-9a-f]+:[0-9a-f]+)\s?(?:\((.*)\))?"

try:
    with open("dhcpd.log", "r") as inpfile:
        for line in inpfile:
            mac_search = re.search(regex, line)
            if mac_search is not None:
                if mac_search.group(3) is None:
                    hostName = ""
                else:
                    hostName = mac_search.group(3)
                if mac_search.group(2) not in nodeDict:
                    nodeDict[mac_search.group(2)] = {"Ip_Address": mac_search.group(1), "Host_Name": hostName}

                    # if get_mac_vendor != '':
                    #     nodeDict[mac_search.group(2)]["Vendor"] = get_mac_vendor
                    # else:
                    #     nodeDict[mac_search.group(2)]["Vendor"] = "No Match"

except Exception as Err:
    print("Error: ", Err)

# macDataAll = json.dumps(macData, indent='\t', separators=(',', ':'))
# with open("MacDataBase.json", "w") as outfile:
#     outfile.write(macDataAll)

# result = client.get_raw_data('b8:27:eb:b4:81:6d', 'json')
# nodeDict["b8:27:eb:b4:81:6d"] = json.load(result)
print(nodeDict)
for k in nodeDict.keys():
    print(k)
mlog.logger.debug("this is a another debug from grabber")
mlog.logger.error("Error from grapper")
