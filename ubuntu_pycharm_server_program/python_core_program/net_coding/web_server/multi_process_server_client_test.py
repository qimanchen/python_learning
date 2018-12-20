from socket import *

for i in range(5):
    client_socket = socket(AF_INET, SOCK_STREAM)
    # connect server
    client_socket.connect(("127.0.0.1", 7788))

    client_socket.send("haha".encode("utf-8"))

    client_socket.close()
