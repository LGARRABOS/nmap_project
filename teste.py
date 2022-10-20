# C:\Users\etien\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\python.exe
import ipaddress
import json
import netifaces
from netaddr import IPAddress
from scapy.all import *
from datetime import datetime
import json


def pingpong(theip):
    ans, unans = arping(theip)
    dict1 = {}
    compt = 0
    for sent, recieved in ans:
        dict1[compt] = recieved.summary()
        compt += 1
        print(recieved.summary())
    test = json.dump(dict1)
    print(test)
    return dict1


test = open("resultscan.txt", "w")

all_interface = netifaces.interfaces()
print(all_interface)
interfaces = str(input())
IpAddr = netifaces.ifaddresses(interfaces)[netifaces.AF_INET][0]['addr']
Netmask = netifaces.ifaddresses(interfaces)[netifaces.AF_INET][0]['netmask']
NetworkIP = ipaddress.ip_network(
    IpAddr + '/' + str(IPAddress(Netmask).netmask_bits()), strict=False)
print(NetworkIP)
print(str(pingpong(str(NetworkIP))))

test.close()

result = open("resultscan.txt", "r")
print(result.read())
result.close()
