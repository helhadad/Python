"""
Script  : tcp_server.py
Author  : John O'Raw
        Copied by Hesham Elhadad for testing and studying purpose
ID      : L00177542
Date    : 25-Oct-22
Purpose : This script demonstrates a tcp server as per walkthrough_11

Tested  : Python 3.10 on Windows 10 Pro
Rev     : 0
IDE     : PyCharm CE ver 2022

"""
import socket
import settings.tcp as settings

TCP_IP = settings.TCP["SERVER_TCP_IPv4"]
TCP_PORT = settings.TCP["SERVER_PORT"]
BUFFER_SIZE = 1024
print(f'This is the TCP server, it will open a port at {TCP_IP}:{TCP_PORT} and being listening')
print(f'Make sure the actual server IP address matches {TCP_IP} in the settings file')
print('This script has no error handling, by design')
try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((TCP_IP, TCP_PORT))
        print(f'Bound to {TCP_IP}:{TCP_PORT}')
        while True:
            s.listen(1)
            conn, addr = s.accept()
            print(f'Connection address: {addr}')
            data = conn.recv(BUFFER_SIZE).decode()
            print(data)
            conn.send(data.encode())
except socket.error as e:
    print(f'Error: {e}')
