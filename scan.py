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
    print(" -t          Gives from a list of ports the services that listen behind.")
    print(" -os         Make a TCP request to a specific Ip")
    print(" -p          Print Save of specific interfaces")
    sys.exit()


def askForInterface():
    all_interface = netifaces.interfaces()
    try:
        sys.argv[2]
    except:
        print(all_interface)
        interfaces = str(input())

        while interfaces not in all_interface:
            print("\nYou did not enter a valid interface")
            all_interface = netifaces.interfaces()
            print(all_interface)
            interfaces = str(input())
        return interfaces
    if sys.argv[2] not in all_interface:
        print("Wrong interface")
        sys.exit()
    return (sys.argv[2])


def TestForScanping(interfaceScan):
    if os.path.exists(interfaceScan + ".json"):
        new_scan = ""
        while new_scan != "y" and new_scan != "n":
            print(
                "A scan of this interface already exists. Do you want to make a new one?  y/n, ")
            new_scan = input()
        if new_scan == "y":
            IpReseauScan = startFirstScanping(interfaceScan)
            file = open(interfaceScan + ".json", "w")
            test = ArpPing(str(IpReseauScan))
            file.write(test)
            file.close()
        else:
            result = open(interfaceScan + ".json", "r")
            print(result.read())
            result.close()
    else:
        IpReseauScan = startFirstScanping(interfaceScan)
        file = open(interfaceScan + ".json", "w")
        test = ArpPing(str(IpReseauScan))
        file.write(test)
        file.close()


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


def TestIpPingTCP():
    count = 0
    stay = True
    try:
        sys.argv[2]
    except:
        print("Enter the Ip")
        IpPingTCP = input()
        TryIp = IpPingTCP.split(".")
        while len(TryIp) != 4 or "/" in IpPingTCP:
            print("Enter valid Ip")
            IpPingTCP = input()
            TryIp = IpPingTCP.split(".")
        while stay == True:
            for value in TryIp:
                if int(value) < 255 and int(value) > 0:
                    count += 1
            if count == 4:
                stay = False
                count = 0
            else:
                print("Enter valid Ip")
                IpPingTCP = input()
                TryIp = IpPingTCP.split(".")
                count = 0
        return IpPingTCP
    if len(sys.argv[2].split(".")) != 4 or "/" in sys.argv[2]:
        print("Wrong Ip")
        sys.exit()
    for value in sys.argv[2].split("."):
        if int(value) > 255:
            print("Wrong Ip")
            sys.exit()
    return sys.argv[2]
    

def TCPPing(Ip):
    print("Enter the port you want to scan.(22,75,490)(Max 7)")
    Port = input()
    Port = Port.split(",")
    while len(Port) > 7:
        print("Enter the port you want to scan.(22,75,490)(Max 7)")
        Port = input()
        Port = Port.split(",")
    for value in Port:
        print("\n"+ value + ":")
        ans, unans = sr( IP(dst=Ip)/TCP(dport=int(value), flags="S") )
        for sent, recieved in ans:
            print(recieved.summary())


def TargetOs():
    count = 0
    stay = True
    try:
        sys.argv[2]
    except:
        print("Enter the Ip address:")
        target = input()
        TryIp = target.split(".")
        while len(TryIp) != 4 or "/" in target: 
            print("Enter valid Ip")
            target = input()
            TryIp = target.split(".")
        while stay == True:
            for value in TryIp:
                if int(value) < 255 and int(value) > 0:
                    count += 1
            if count == 4:
                stay = False
                count = 0
            else:
                print("Enter valid Ip")
                target = input()
                TryIp = target.split(".")
                count = 0
        return target
    for value in sys.argv[2].split("."):
        if int(value) > 255:
            print("Wrong Ip")
            sys.exit()
    return sys.argv[2]

def FindOs(myTarget):
    pack = IP(dst=myTarget)/ICMP()
    resp = sr1(pack, timeout=3)
    if resp:
        if IP in resp:
            ttl = resp.getlayer(IP).ttl
            if ttl == 64: 
                os = "Linux"
            elif ttl == 128:
                os = "Windows"
            elif ttl == 255:
                os = "Cisco Routeur"
            else:
                print("Not Found")
            print(f'\n\nTTL = {ttl} \n*{os}* Operating System is Detected \n\n')


def TryTargetInterface():
    all_interface = netifaces.interfaces()
    try:
        sys.argv[2]
    except:
        print(all_interface)
        interfaces = str(input())

        while interfaces not in all_interface:
            print("\nYou did not enter a valid interface")
            all_interface = netifaces.interfaces()
            print(all_interface)
            interfaces = str(input())
        return interfaces
    if sys.argv[2] not in all_interface:
        print("Wrong interface")
        sys.exit()
    return (sys.argv[2])


def PrintInterfaceFile(interface):
    try:
        result = open(interface + ".json", "r")
    except:
        print("This file did not exist try sudo python scan.py -a " + interface)
        sys.exit()
    print(result.read())
    result.close()


if len(sys.argv)  == 1:
    print("Invalid command")
    help()

if "-" not in sys.argv[1] and len(sys.argv) > 3 :
    print("Invalid argument")
    help()

if sys.argv[1] == "-h" and len(sys.argv) < 2:
    help()

elif sys.argv[1] == "-a" :
    TestForScanping(askForInterface())
     
elif sys.argv[1] == "-t":
    TCPPing(TestIpPingTCP())

elif sys.argv[1] == "-os":
    FindOs(TargetOs())

elif sys.argv[1] == "-p":
    PrintInterfaceFile(TryTargetInterface())
else:
    print("Invalid command")
    help()