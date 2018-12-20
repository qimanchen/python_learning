from socket import *
from multiprocessing import Process

def client_server(new_socket, dest_addr):
    try:
        while True:
            recv_data = new_socket.recv(1024)
            if len(recv_data) > 0:
                print("recv[%s]:%s"%(str(dest_addr), recv_data))
            else:
                print("[%s] client is already close"%str(dest_addr))
                break
    finally:
        new_socket.close()
    print("client end")
    return False

def main():
    ser_socket = socket(AF_INET, SOCK_STREAM)

    # repeat use bind info
    ser_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

    local_addr = ("", 7788)

    ser_socket.bind(local_addr)

    ser_socket.listen(5)

    client_num = 0
    try:
        while True:
            print("--- main process, wait client---")
            new_socket, dest_addr = ser_socket.accept()

            client_num = client_num + 1
            print("--- main process, deal data {%s} ---" % str(dest_addr))
            client = Process(target=client_server, args=(new_socket, dest_addr))
            client.start()
            print(client_num)
    finally:
        ser_socket.close()


if __name__ == "__main__":
    main()

