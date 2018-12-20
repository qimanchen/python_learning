from socket import *
import struct

send_data = struct.pack("!H8sb5sb",1,"test.txt",0,"octet",0)

udp_socket = socket(AF_INET, SOCK_DGRAM)
udp_socket.bind(("",7788))
udp_socket.sendto(send_data, ("10.0.2.7",69))
recv_data = udp_socket.recvfrom(1024)
content, destination = recv_data
result = struct.unpack("!HH", content[:4])
print(destination)
print(content[4:])
print(result)
print(len(content))

udp_socket.close()
