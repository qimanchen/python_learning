from socket import *

# create tcp socket
server_socket = socket(AF_INET, SOCK_STREAM)

# bind port
server_socket.bind(("", 8890))

# listen
server_socket.listen(5)

client_socket, client_info = server_socket.accept()
# client_socket --> new client
# client_socket --> new client ip and port

recv_data = client_socket.recv(1024)

print("%s:%s"%(str(client_info), recv_data))

client_socket.close()
server_socket.close()

