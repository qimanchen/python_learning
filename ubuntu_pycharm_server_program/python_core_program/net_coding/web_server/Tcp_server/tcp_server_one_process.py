from socket import *

ser_socket = socket(AF_INET, SOCK_STREAM)

# 2. bind local ip and port
local_addr = ("", 7788)
ser_socket.bind(local_addr)

ser_socket.setblocking(False)

# 3. listen
ser_socket.listen(100)

# save all already line client info
client_addr_list = []
while True:

    # wait new client (finish three hello)
    try:
        new_socket, client_addr = ser_socket.accept()
    except:
        pass
    else:
        print("one new client coming: %s"% str(client_addr))
        new_socket.setblocking(False)
        client_addr_list.append((new_socket, client_addr))

    for client_socket, client_addr in client_addr_list:
        try:
            recv_data = client_socket.recv(1024)
        except:
            pass
        else:
            if len(recv_data) > 0:
                print("%s:%s"%(str(client_addr),recv_data))
            else:
                client_socket.close()
                client_addr_list.remove((client_socket, client_addr))
                print("%s log out" %str(client_addr))

