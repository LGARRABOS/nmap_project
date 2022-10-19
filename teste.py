# C:\Users\etien\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\python.exe
from scapy.all import ICMP, sr, IP, srloop, send, arping

print("Entrez le réseau que vous voulez scannez sous la forme 00.00.00.00/00")
reseauscan = input()



def pingpong(theip):
    arping(theip)
    return


pingpong(reseauscan)
