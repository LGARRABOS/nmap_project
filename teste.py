# C:\Users\etien\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\python.exe
from scapy.all import ICMP, sr, IP, srloop, send, arping

reseauscan = Input("Entrez le réseau que vous voulez scannez sous la forme 00.00.00.00/00")

def pingpong(theip):


    # sr(IP(dst=theip, src="192.168.236.8")/ICMP(), timeout=5)
    arping("192.168.236.1/24")
    return


pingpong(reseauscan)
