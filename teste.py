# C:\Users\etien\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\python.exe
from scapy.all import ICMP, sr, IP, srloop


ip = input()

def pingpong(theip):
    ans, unans  = sr(IP(dst="10.3.2.0/24")/ICMP(), timeout=3)
    srloop(ans, unans)
    return 

pingpong(ip)