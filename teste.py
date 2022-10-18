
import socket

import ipaddress

IP = input()
tabipmask = IP.split("/")
theIp = ipaddress.IPv4Address(tabipmask[0])
net = ipaddress.IPv4Interface(IP)
broad = ipaddress.IPv4Network(net.network,  False)
print('IP: ', IP)
print('Reseau: ', net.network)
print('Broadcast: ', broad.broadcast_address)


