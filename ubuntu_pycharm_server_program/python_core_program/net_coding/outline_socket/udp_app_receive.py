from socket import *

def main():
    # receive info
    # create a sockte
    udp_socket = socket(AF_INET, SOCK_DGRAM)

    # bind port
    udp_socket.bind(("", 7788))

    while True:
        # receive info
        recv_data = udp_socket.recvfrom(1024)

        content, resource = recv_data

        print("receive content is %s"%content.decode("utf-8"))

if __name__ == "__main__":
    main()

