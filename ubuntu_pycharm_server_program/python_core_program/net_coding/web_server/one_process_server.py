from socket import *

ser_socket = socket(AF_INET, SOCK_STREAM)

# repeat use bind info
ser_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

local_addr = ("", 7788)

ser_socket.bind(local_addr)

ser_socket.listen(5)

while True:
    print("--- main process, wait client---")
    new_socket, dest_addr = ser_socket.accept()

    print("--- main process, deal data {%s} ---" % str(dest_addr))

    try:
        while True:
            recv_data = new_socket.recv(1024)
            if len(recv_data) > 0:
                print("recv[%s]:%s"%(str(dest_addr, recv_data)))
            else:
                print("[%s] client is already close"%str(dest_addr))
                break
    finally:
        new_socket.close()

ser_socket.close()

