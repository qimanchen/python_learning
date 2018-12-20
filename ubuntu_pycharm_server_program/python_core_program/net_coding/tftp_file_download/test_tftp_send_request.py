from socket import *
import struct

send_data = struct.pack("!H8sb5sb",1,"test.txt",0,"octet",0)

udp_socket = socket(AF_INET, SOCK_DGRAM)
udp_socket.bind(("",7788))
udp_socket.sendto(send_data, ("10.0.2.7",69))

udp_socket.close()
