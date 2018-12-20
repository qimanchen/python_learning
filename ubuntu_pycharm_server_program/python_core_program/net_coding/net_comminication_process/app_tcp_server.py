from socket import *

tcp_server_socket = socket(AF_INET, SOCK_STREAM)

# bind local port
address = ("", 7788)
tcp_server_socket(address)

tcp_server_socket.listen(5)

while True:
    new_client_socket, new_clinet_addr = tcp_server_socket.accept()

    while True:
        recv_data = new_client_socket.recv(1024)

        if len(recv_data) > 0:
            print("recv data is %s" % recv_data)
        else:
            break

        send_data = input("send: ")
        new_client_socket.send(send_data)

    new_client_socket.close()

tcp_server_socket.close()

