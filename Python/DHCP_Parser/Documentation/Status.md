# DHCP Parser Project

## Introduction

DHCP server is commonly used in computer network, especially those that provides services to multiple users with 
various devices (i.e., Computers, Cameras, Printers, Scanner,...etc.)

Most of DHCP server has a logging capability and generate log files. Processing those files, provide a wealth of information to the network administrator and users alike.

## Project Details

It was required to process a DHCP log file and extract the following information from the file:

1 -MAC address of any devices served by the DHCP.

2- IP address assigned to the connected devices.

3- Node name of the connected devices.

Moreover, by using the available MAC address and Organisational Unique Identifier (OUI), it was required to get the manufacturer
details of the NIC of the examined node.

## Limitation

The available log file is limited to 100 lines of log only, to smiplify the project.

The project doesn't require any online processing, therefore a connection with OUI site via API was not established or coded.

## Application

The Python Parser application is a simple parser application utilize a regular expression term to parse the most important 
lines of the DHCP log file.

The Parser then convert the extracted information into a Python dictionary.

The (OUI) data is captured in a Json file, which will be loaded into another Python dictionary.

By processing the two dictionaries, a CSV file with the required output is generated and saved.

For more information about the Parser application, refer to <a src="ReadMe.md">ReadMe.MD</a>

