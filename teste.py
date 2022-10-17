
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
print(s.getsockname()[0])
print("\n", s)

import ipaddress
IP = s.getsockname()[0]
network = ipaddress.ip_network(addr+'/'+str(network_bits+extra_bits))
MASK = "255.255.0.0"

host = ipaddress.IPv4Address(IP)
net = ipaddress.IPv4Network(IP + '/' + MASK, False)
print('IP:', IP)
print('Mask:', MASK)
print('Subnet:', ipaddress.IPv4Address(int(host) & int(net.netmask)))
print('Host:', ipaddress.IPv4Address(int(host) & int(net.hostmask)))
print('Broadcast:', net.broadcast_address)

# from socket import *
# s=socket(AF_INET, SOCK_DGRAM)
# s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
# s.sendto('this is testing',('255.255.255.255',12345))


# s=socket(AF_INET, SOCK_DGRAM)
# s.bind(('',12345))
# m=s.recvfrom(1024)
# print( m[0])
# s.close()
