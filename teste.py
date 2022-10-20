# C:\Users\etien\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\python.exe
import ipaddress
import netifaces
from netaddr import IPAddress
from scapy.all import *
from datetime import datetime


def pingpong(theip, myinterface):
    ans, unans = arping(theip)
    for sent, recieved in ans:
        test.write(recieved.summary() + "\n")
    return ""

date = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

test = open("resultscan.txt", "a")
test.write("\n" + dt_string)

all_interface = netifaces.interfaces()
print(all_interface)
interfaces = str(input())
IpAddr = netifaces.ifaddresses(interfaces)[netifaces.AF_INET][0]['addr']
Netmask = netifaces.ifaddresses(interfaces)[netifaces.AF_INET][0]['netmask']
NetworkAdresse = ipaddress.ip_network(
    IpAddr + '/' + str(IPAddress(Netmask).netmask_bits()), strict=False)
print(NetworkAdresse)
print(pingpong(str(NetworkAdresse), str(interfaces)))

test.close()

result = open("resultscan.txt", "r")
print(result.read())
result.close()
