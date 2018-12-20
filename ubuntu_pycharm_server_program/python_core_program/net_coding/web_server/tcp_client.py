from socket import *

# create a client socket
client_socket = socket(AF_INET, SOCK_STREAM)

# connect server
client_socket.connect(("192.169.3.200", 5025))

while True:
    # send_msg = input("please input your want to send msg <<")

    client_socket.send(r":syst:comm:netw:addr?".encode("utf-8"))
    client_socket.send(r"\r\n".encode("utf-8"))

    result = client_socket.recv(1024)
    print(result.decode("utf-8"))

client_socket.close()
