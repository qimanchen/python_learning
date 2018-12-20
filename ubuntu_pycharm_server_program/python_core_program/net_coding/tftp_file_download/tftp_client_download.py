from socket import *


def main():
    # create a socket for download
    udp_socket = socket(AF_INET, SOCK_DGRAM)

    # bind port
    udp_socket.bind(("",7788))

    # set transfer ip an port
    dest_ip = "10.0.2.32"
    dest_port = 69

    # creat a new file
    download_file_name = input("please input need download fileName: ")

    f = open(download_file_name,"bw")

    # write data to the new file
    while True:
        recv_data = udp_socket.recvfrom(1024)

    # close the file
    f.close()
