# C:\Users\etien\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\python.exe
import ipaddress
import netifaces
from netaddr import IPAddress
from scapy.all import ICMP, sr, IP, srloop, send, arping


def pingpong(theip):
    arping(theip)
    return

all_interface=netifaces.interfaces()
print(all_interface)
interfaces = str(input())
IpAddr = netifaces.ifaddresses(interfaces)[netifaces.AF_INET][0]['addr']
Netmask = netifaces.ifaddresses(interfaces)[netifaces.AF_INET][0]['netmask']
NetworkAdresse = ipaddress.ip_network(IpAddr + '/'+str(IPAddress(Netmask).netmask_bits()), strict=False)
print(NetworkAdresse )
pingpong(str(NetworkAdresse ))
ans, unans = sr(IP(dst="192.168.1.0/24")/ICMP(), timeout=3)
ans.summary(lambda s,r: r.sprintf("%IP.src% is alive") )