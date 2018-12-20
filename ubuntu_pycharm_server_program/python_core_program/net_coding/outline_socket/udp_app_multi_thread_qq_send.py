from threading import Thread
from socket import *

# 1. receive data
def recv_data():
    while True:
        recv_info = udp_socket.recvfrom(1024)
        print(">> %s: %s" % (str(recv_info[1]), recv_info[0]))

# 2. send data
def send_data():
    while True:
        send_info = input("<< ")
        udp_socket.sendto(send_info.encode("utf-8"),(dest_ip, dest_port))


udp_socket = None
dest_ip = ""
dest_port = 0

def main():
    global udp_socket
    global dest_ip
    global dest_port
    dest_ip = input("receive ip: ")
    dest_port = int(input("receive port: "))
    
    udp_socket = socket(AF_INET, SOCK_DGRAM)
    udp_socket.bind(("", 7789))

    tr = Thread(target=recv_data)
    ts = Thread(target=send_data)

    tr.start()
    ts.start()

    tr.join()
    ts.join()


if __name__ == "__main__":
    main()


