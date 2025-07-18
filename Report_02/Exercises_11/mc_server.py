"""
Script  : mc_server.py
Author  : John O'Raw
        Copied by Hesham Elhadad for testing and studying purpose
ID      : L00177542
Date    : 25-Oct-22
Purpose : This script demonstrates a multicast server as explained in walkthrough_11

Tested  : Python 3.10 on Windows 10 Pro
Rev     : 0
IDE     : PyCharm CE ver 2022

"""
import socket
import settings.mc as settings

# Set multicast information
MCAST_GRP = settings.MCSERVER["MCAST_GROUP"]
SERVER_ADDRESS = ('', settings.MCSERVER["PORT"])
MCAST_IF_IP = settings.MCSERVER["IP_ADDRESS"]
print('This is the server.')
print(f'Make sure its IP address matches {MCAST_IF_IP} in settings.')
print(f'This selects which interface is used to listen for multicast as {MCAST_GRP}.')
print('This script has no error handling, by design.')
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind(SERVER_ADDRESS)
    # inet_aton converts IPv4 from the a dotted decimal string to 32 bit packed binary format
    s.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, socket.inet_aton(MCAST_GRP) +
                 socket.inet_aton(MCAST_IF_IP))
    while True:
        print('Waiting to receive message')
        data, address = s.recvfrom(1024)
        print(f'received {len(data)} bytes from {address}')
        print(data)
