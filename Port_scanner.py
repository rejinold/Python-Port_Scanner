#!/usr/bin/python3

from socket import *

target_IP = str(input("\n Enter the target IP address: "))
ip_address = target_IP

print("\n [*]Performing Port Scan for %s \n" % ip_address)

for port in range(1, 5000):

    try:
        s = socket(AF_INET, SOCK_STREAM)
        conn = s.connect_ex((ip_address, port))

    except OverflowError as error:
        print("\n Port overflow occurs!")
        print("PORT: %d CLOSED" % port)        
    
    if (conn == 0):
        print("PORT: %d OPEN" % (port,) )
        s.close()







