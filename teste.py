# C:\Users\etien\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\python.exe
import ipaddress
from tkinter import END
import netifaces
from netaddr import IPAddress
from scapy.all import *
import json
import sys

def startping():
    all_interface = netifaces.interfaces()
    print(all_interface)
    interfaces = str(input())

    while interfaces not in all_interface:
        print("\nYou did not enter a valid interface")
        all_interface = netifaces.interfaces()
        print(all_interface)
        interfaces = str(input())
    
    IpAddr = netifaces.ifaddresses(interfaces)[netifaces.AF_INET][0]['addr']
    Netmask = netifaces.ifaddresses(interfaces)[netifaces.AF_INET][0]['netmask']
    NetworkIP = ipaddress.ip_network(IpAddr + '/' + str(IPAddress(Netmask).netmask_bits()), strict=False)
    return NetworkIP



def pingpong(theip):
    ans, unans = arping(theip)
    dict1 = {}
    compt = 0

    for sent, recieved in ans:
        dict1[compt] = recieved.summary()
        compt += 1

    save_value = json.dumps(dict1)
    return save_value

if sys.argv.len > 2:
    sys.exit()

IpReseauScan = startping()

file = open("resultscan.json", "w")

test = pingpong(str(IpReseauScan))
file.write(test)

file.close()

result = open("resultscan.json", "r")
print(result.read())
result.close()
