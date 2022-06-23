#!/usr/bin/env python3

import sys
import socket

Csocket = socket.socket()
host = '192.168.54.4'
port = 8989

print("Waiting for connection.....")

try:
    Csocket.connect((host, port))
except socket.error as e:
    print(str(e))

msg = Csocket.recv(1024)
print(msg.decode('utf-8'))
cmsg = "Connected with client no 1"
Csocket.send(cmsg.encode('utf-8'))

while True:

    print("Please enter a function:")
    print("1. log")
    print("2. square root")
    print("3. exponential")
    print("q. quit")
    option = input('')

    if option == '1' or option == '2' or option == '3':
        value = input("Please enter a number: ")
        option = option + ":" + value
        Csocket.send(str.encode(option))

    elif option == 'q':
        print("Exiting..")
        Csocket.send(str.encode(option))
        sys.exit()
    else:
        print("Exiting..")
        sys.exit()

    msg = Csocket.recv(1024)
    print(msg.decode("utf-8"))

Csocket.close()
