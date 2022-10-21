# C:\Users\etien\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\python.exe
import ipaddress
import netifaces
from netaddr import IPAddress
from scapy.all import *
import json
import sys
import os

def help():
    print("This program is a network scanner")
    print("You have to run this program as root")
    print("Programm command list:")
    print(" -h          Gives access to the list of commands and their uses.")
    print(" -a          Make a ARP ping request on all the whole network and write result in file")
    print(" -u          Make a UDP request to a specific Ip")
    print(" -t          Make a TCP request to a specific Ip")
    sys.exit()

def askForInterface():
    all_interface = netifaces.interfaces()
    print(all_interface)
    interfaces = str(input())

    while interfaces not in all_interface:
        print("\nYou did not enter a valid interface")
        all_interface = netifaces.interfaces()
        print(all_interface)
        interfaces = str(input())
    return interfaces 

def startFirstScanping(interface):

    IpAddr = netifaces.ifaddresses(interface)[netifaces.AF_INET][0]['addr']
    Netmask = netifaces.ifaddresses(
        interface)[netifaces.AF_INET][0]['netmask']
    NetworkIP = ipaddress.ip_network(
        IpAddr + '/' + str(IPAddress(Netmask).netmask_bits()), strict=False)
    return NetworkIP


def ArpPing(theip):
    ans, unans = arping(theip)
    dict1 = {}
    compt = 0

    for sent, recieved in ans:
        dict1[compt] = recieved.summary()
        compt += 1

    save_value = json.dumps(dict1)
    return save_value


if len(sys.argv) > 2 or "-" not in sys.argv[1] :
    print("Invalid argument")
    sys.exit()

scanInterface = askForInterface()

if sys.argv[1] == "-h":
    help()
elif sys.argv[1] == "-a":
    if os.path.exists(scanInterface + ".json"):
        new_scan =""
        print("A scan of this interface already exists. Do you want to make a new one?  y/n, ")
        new_scan = input()
        if new_scan == "y":
            IpReseauScan = startFirstScanping(scanInterface)
            file = open( scanInterface + ".json", "w")
            test = ArpPing(str(IpReseauScan))
            file.write(test)

            file.close()

            result = open(scanInterface + ".json", "r")
            print(result.read())
            result.close()
        else:
            result = open(scanInterface + ".json", "r")
            print(result.read())
            result.close()
    else:
        IpReseauScan = startFirstScanping(scanInterface)
        file = open( scanInterface + ".json", "w")
        test = ArpPing(str(IpReseauScan))
        file.write(test)

        file.close()

        result = open(scanInterface + ".json", "r")
        print(result.read())
        result.close()
elif sys.argv[1] == "-u":
    print("Enter the Ip")
