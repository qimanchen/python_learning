from socket import *

udp_socket = socket(AF_INET, SOCK_DGRAM)

udp_socket.bing(("", 7788))

recv_data = udp_socket.recvfrom(1024)
# recv_data = (receive content, ("send_ip", send_port))

content, dest_info = recv_data

# decode
print("content is %s" % content.decode("gb2312"))

