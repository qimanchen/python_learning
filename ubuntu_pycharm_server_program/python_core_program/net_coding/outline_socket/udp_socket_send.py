from socket import *

#1. create a socket -- UDP
udp_socket = socket(AF_INET, SOCK_DGRAM)

#2. set receive ip and port
send_addr = ('10.0.2.32', 7788)

#3. get date that will be send from keyboard
#send_data = input("please input data send: ")

#4. send data to specifical computer
udp_socket.sendto(b"haha", send_addr)

#5. close udp socket
udp_socket.close()


