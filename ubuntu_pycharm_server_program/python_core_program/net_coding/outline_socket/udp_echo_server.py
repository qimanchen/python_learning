from socket import *

def main():
    udp_socket = socket(AF_INET, SOCK_DGRAM)

    bind_addr = ("", 7788)
    udp_socket.bind(bind_addr)

    num = 1

    while True:

        recv_data = udp_socket.recvfrom(1024)

        udp_socket.sendto(recv_data[0], recv_data[1])

        print("reveive %d data, content is %s" % (num, recv_data[0].decode("utf-8")))
        num += 1

    udp_socket.close()

if __name__ == "__main__":
    main()

