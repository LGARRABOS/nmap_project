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
    #print(" -u          Make a UDP request to a specific Ip"), 
    print(" -t          Make a TCP request to a specific Ip")
    print(" -os          Make a TCP request to a specific Ip")
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

def TCPPing(Ip):
    try:
        ans, unans = sr( IP(dst=Ip)/TCP(dport=[20, 21, 22, 25, 35, 38, 57, 80, 143, 161, 162, 427, 548, 631, 647, 706, 853, 989, 990], flags="S") )
    except socket.gaierror:
        raise ValueError('Hostname {} could not be resolved.'.format(Ip))
    ans, _ = sr(sync, timeout=2, retry = 1)
    for sent, recieved in ans:
        print(recieved.summary())

    




if len(sys.argv)  == 1:
    print("Invalid command")
    help()


if len(sys.argv) > 2 or "-" not in sys.argv[1] :
    print("Invalid argument")
    help()

scanInterface = askForInterface()

if sys.argv[1] == "-h":
    help()
elif sys.argv[1] == "-a":
    if os.path.exists(scanInterface + ".json"):
        new_scan =""
        print("A scan of this interface already exists. Do you want to make a new one?  y/n, ")
        new_scan = input()
        while new_scan != "y" and new_scan != "n":
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
elif sys.argv[1] == "-t":
    print("Enter the Ip")
    IpPingTCP = input()
    TryIp = IpPingTCP.split(".")
    while len(TryIp) != 4 or "/" in IpPingTCP: 
        print("Enter valid Ip")
        IpPingTCP = input()
        TryIp = IpPingTCP.split(".")
    TCPPing(IpPingTCP)

elif sys.argv[1] == "-os":
    os = ''
    target = input("Enter the Ip address:")
    pack = IP(dst=target)/ICMP()
    resp = sr1(pack, timeout=3)
    if resp:
        if IP in resp:
            ttl = resp.getlayer(IP).ttl
            if ttl <= 64: 
                os = 'Linux'
            elif ttl > 64:
                os = 'Windows'
            else:
                print('Not Found')
            print(f'\n\nTTL = {ttl} \n*{os}* Operating System is Detected \n\n')

