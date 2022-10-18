from scapy.all import ICMP, sr, IP, srloop

#conf.use_pcap = True

IP = input()
packet = sr(IP(dst=IP)/ICMP(), timeout=3)
srloop(packet)
