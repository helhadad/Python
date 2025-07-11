"""
Script  : udp_server.py
Author  : John O'Raw
        Copied by Hesham Elhadad for testing and studying purpose
ID      : L00177542
Date    : 25-Oct-22
Purpose : This script demonstrates a udp_server as a solution to walkthrough_11

Tested  : Python 3.10 on Windows 10 Pro
Rev     : 0
IDE     : PyCharm CE ver 2022

"""
import socket
import settings.udp as settings

UDP_IP = settings.UDP["SERVER_UDP_IPv4"]
UDP_PORT = settings.UDP["SERVER_PORT"]
BUFFER_SIZE = 1024

print(f'This is the UDP server, it will open a port at {UDP_IP}:{UDP_PORT} and being listening')
print(f'Make sure the actual server IP address matches {UDP_IP} in the settings file')
print('This script has no error handling, by design')
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    s.bind((UDP_IP, UDP_PORT))
    print('Listening on', UDP_IP)
    while True:
        data, addr = s.recvfrom(BUFFER_SIZE)
        data = data.decode()
        print(addr, data)
