from socket import socket
from socket import AF_INET, SOCK_DGRAM
from socket import SOL_SOCKET, SO_BROADCAST
import sys

dest = ('<broadcast>', 7788)

# create udp socket
udp_socket = socket(AF_INET, SOCK_DGRAM)

# set for broadcast
udp_socket.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

# send msg
udp_socket.sendto("Hi", dest)

print("Wait receive")

while True:
    buf, address = udp_socket.recvfrom(2048)
    print("Received from %s: %s" % (address, buf))

