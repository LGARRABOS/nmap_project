from scapy.all import ICMP, sr, IP, srloop


IP = input()

packet = svr(IP(dst=IP)/ICMP(), timeout=3)
srloop(packet)
