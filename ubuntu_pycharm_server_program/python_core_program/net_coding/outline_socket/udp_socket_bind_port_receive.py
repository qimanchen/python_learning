# -*- coding: utf-8 -*-

from socket import *

udp_socket = socket(AF_INET,SOCK_DGRAM)

# bind local info(ip and port), if not set this info will be random set
bind_addr = ('',7788)  # ip and port, the ip ususal not specific
udp_socket.bind(bind_addr)

# wait recive data from send pc
recv_data = udp_socket.recvfrom(1024) # 1024 is max receive bytes

# print received data
print(recv_data)

# close socket
udp_socket.close()

