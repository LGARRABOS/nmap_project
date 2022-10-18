# C:\Users\etien\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\python.exe
from scapy.all import ICMP, sr, IP, srloop, send



def pingpong(theip):
    sr(IP(dst=theip, src="10.3.2.1")/ICMP(), timeout=5)
    return


pingpong("10.3.2.12")
