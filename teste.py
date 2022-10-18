#!C:\Users\etien\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\python.exe

from scapy.all import ICMP, sr, IP

#conf.use_pcap = True

IP = input()
packet = sr(IP(dst=IP)/ICMP(), timeout=3)
srloop(packet)
