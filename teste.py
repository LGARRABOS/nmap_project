
import socket

import ipaddress

IP = input()

net = ipaddress.ip_address(IP)
print('IP:', IP)
print('Broadcast:', net.broadcast_address)

