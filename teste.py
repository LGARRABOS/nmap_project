# C:\Users\etien\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\python.exe
import ipaddress
import json
import netifaces
from netaddr import IPAddress
from scapy.all import *
from datetime import datetime
import json


def pingpong(theip):
    ans, unans = sr(IP(dst="192.168.236.1",proto=(0,255))/"SCAPY",retry=2)
    dict1 = {}
    compt = 0
    for sent, recieved in ans:
        dict1[compt] = recieved
        compt += 1
    out_file = open("resultscan.txt", "w")
    print(json.dump(dict1, sort_keys=True, indent = 4))
    return ""


test = open("resultscan.txt", "w")

all_interface = netifaces.interfaces()
print(all_interface)
interfaces = str(input())
IpAddr = netifaces.ifaddresses(interfaces)[netifaces.AF_INET][0]['addr']
Netmask = netifaces.ifaddresses(interfaces)[netifaces.AF_INET][0]['netmask']
NetworkIP = ipaddress.ip_network(IpAddr + '/' + str(IPAddress(Netmask).netmask_bits()), strict=False)
print(NetworkIP)
print(pingpong(str(NetworkIP)))

test.close()

result = open("resultscan.txt", "r")
print(result.read())
result.close()
