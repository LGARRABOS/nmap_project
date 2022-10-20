# C:\Users\etien\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\python.exe
import ipaddress
import json
import netifaces
from netaddr import IPAddress
from scapy.all import *
from datetime import datetime
import json


def pingpong(theip, scaninterface):
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    arp = ARP(pdst = theip)
    ans, unanswered = srp(ether/arp, timeout = 2, iface = scaninterface, inter = 0.1)
    # ans, unans = arping(theip)
    dict1 = {}
    compt = 0
    for sent, recieved in ans:
        # dict1[compt] = recieved
        # compt += 1
        print(recieved.summary())
    # out_file = open("resultscan.txt", "w")
    # print(json.dump(dict1, sort_keys=True, indent = 4))
    return ""


test = open("resultscan.txt", "w")

all_interface = netifaces.interfaces()
print(all_interface)
interfaces = str(input())
IpAddr = netifaces.ifaddresses(interfaces)[netifaces.AF_INET][0]['addr']
Netmask = netifaces.ifaddresses(interfaces)[netifaces.AF_INET][0]['netmask']
NetworkIP = ipaddress.ip_network(IpAddr + '/' + str(IPAddress(Netmask).netmask_bits()), strict=False)
print(NetworkIP)
print(pingpong(str(NetworkIP), str(interfaces)))

test.close()

result = open("resultscan.txt", "r")
print(result.read())
result.close()
