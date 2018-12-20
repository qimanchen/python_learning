from socket import *

def main():
    udp_socket = socket(AF_INET, SOCK_DGRAM)

    send_addr = ("10.0.2.32", 7788)

    while True:
        send_data = input("please input send content")
        udp_socket.sendto(send_data.encode("utf-8"), send_addr)

if __name__ == "__main__":
    main()

