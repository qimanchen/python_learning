from socekt import *
from time import sleep


# create a tcp socket

tcp_server_socket = socket(AF_INET, SOCK_STREAM)

# bind local info
address = ("", 7788)
tcp_server_socket.bind(address)

conn_num = int(input("please input the max connect num: "))

tcp_server_socket.listen(conn_num)

while True:
    new_socket, client_addr = tcp_server_socket.accept()
    print(client_addr)
    sleep(1)

