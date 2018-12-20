from socket import *

client_socket = socket(AF_INET, SOCK_STREAM)
# connect server
client_socket.connect(("169.254.0.3", 8899))

client_socket.send("haha".encode("utf-8"))

recv_data = client_socket.recv(1024)

print("recv_data:%s" % recv_data)

client_socket.close()
