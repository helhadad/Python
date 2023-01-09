# DHCP LOG PARSER

![Parser_Application](Documentation/Python_Parser.jpg?raw=true "Title")

## 1 - Introduction
The application will process a DHCP log file to search and parse the following information from the file:

1. Mac-address of node
2. IP-address of node
3. Host name of node if exist

The application will match the finiding mac-adresses from the log file with another mac-database which contains venodr details.

After completing the parsing, the application will output the reseult to a CSV file with the following style:



| Node | Mac_Address | Ip_Address | Host_Name | Vendor |
| :---: | :---: | :---: | :---: | :---: |
| Node-1|c8:4b:d6:0a:77:2d|192.168.5.168|A-76MRRL3|Dell Inc

***

## 2 - Method
The application uses the following Python modules:

1. <a href="https://docs.python.org/3.10/library/re.html" > re</a>
2. <a href= "https://docs.python.org/3.10/library/json.html" >json</a>
3. <a href = "https://docs.python.org/3.10/library/csv.html">csv </a>
4. <a href = "https://docs.python.org/3.10/library/os.html">os</a>
5. <a href="https://docs.python.org/3.10/library/os.path.html" >os.path</a>
6. <a href = "https://docs.python.org/3.10/library/logging.html">logging </a>

The DHCP log file will be searched line by line with a regex expression which parses and extracts the required information.

The collected info will be added to a dictionary for further procssing.

Mac data, which is a json file, is opened and loaded into another dictionary (i.e, Output).

Both dictionaries are used to generate the csv output file.

## 3 - Logging
The application makes use of the Python logging module, which allows different levels of logging and using of multiple handlers.
The application uses the following handlers:

1. con_handler - for displaying Info on console
2. file_handlr - for logging more debug and errors in a log file (../Logs/App_log.txt)

## 4 - Usage
The application is interactive, requires inputs for DHCP logging file, and a folder path to the output CSV file.
To run the application, run "main.py" file only as follows:

``` Python main.py ```


The application will then prompt the user to enter a full path to the DHCP log file. The application will validate the path 
entered as valid file (i.e, not a folder) and the file exists.

Later, the application will prompt the user again for a path to the csv out file, The application
will validate the path as an existing folder.

Example as follows:

```Enter DHCP Log file path (no quotes) : DHCP_Parser\Input\dhcpd.log```

```Enter the desired CSV folder (no quotes) : DHCP_Parser\Output```
