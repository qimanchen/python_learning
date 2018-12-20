from socket import *
import struct

# open need send file
f = open("timg.jpeg","rb")

# send request to tftp server
send_data = struct.pack("!H9sb5sb",2,"timg.jpeg",0,"octet",0)

udp_socket = socket(AF_INET, SOCK_DGRAM)
udp_socket.bind(("",7788))
udp_socket.sendto(send_data, ("10.0.2.7",69))

# send file
while True:
    recv_info = udp_socket.recvfrom(1024)
    constent, dest = recv_info

    get_back = struct.unpack("!HH",constent[:4])

    send_file_data = f.read(512)
    if send_file_data == "":
        break
    send_file_data_len = len(send_file_data)
    send_pack_str = "!HH%ds"%send_file_data_len

    pack_send_data = struct.pack(send_pack_str,3,get_back[1]+1,send_file_data)

    udp_socket.sendto(pack_send_data,(dest[0],dest[1]))


udp_socket.close()


f.close()
