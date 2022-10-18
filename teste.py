
import socket

import ipaddress
from xml.etree.ElementTree import tostring

IP = input()
tabipmask = IP.split("/")
theIp = ipaddress.IPv4Address(tabipmask[0])
net = ipaddress.IPv4Interface(IP)
broad = ipaddress.IPv4Network(net.network,  False)
print('IP: ', IP)
print('Reseau: ', net.network)
print('Broadcast: ', broad.broadcast_address)
# savenetadress = net.network

# partreseau = tostring(savenetadress).split(".")
# partBroad = broad.broadcast_address.split(".")

# nonmutableparip =  []

# for i in range(len(partBroad)):
#     if (partBroad[i] == partreseau[i]):
#         nonmutableparip.append(partBroad[i])

# print(nonmutableparip)

nbip = 32 - int(tabipmask[1])
i = 1
for i in range(2**nbip - 2):
    print(i)
