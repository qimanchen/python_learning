from socket import *

udp_socket = socket(AF_INET, SOCK_DGRAM)

dest_ip = input("please input dest ip: ")
dest_port = int(input("please input dest port: "))
send_data = input("please input data sended: ")

udp_socket.sendto(send_data.encode("utf-8"), (dest_ip, dest_port))

# use chinese encode
# udp_socket.sendto(send_data.encode("gb2312"), (dest_ip, dest_port))

