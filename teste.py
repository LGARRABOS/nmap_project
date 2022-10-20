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
    save_value = json.dumps(dict1)
    return save_value

file = open("resultscan.json", "w")

all_interface = netifaces.interfaces()
print(all_interface)
interfaces = str(input())
IpAddr = netifaces.ifaddresses(interfaces)[netifaces.AF_INET][0]['addr']
Netmask = netifaces.ifaddresses(interfaces)[netifaces.AF_INET][0]['netmask']
NetworkIP = ipaddress.ip_network(
    IpAddr + '/' + str(IPAddress(Netmask).netmask_bits()), strict=False)
print(NetworkIP)
test = pingpong(str(NetworkIP))
file.write(test)

file.close()

result = open("resultscan.json", "r")
print(result.read())
result.close()
