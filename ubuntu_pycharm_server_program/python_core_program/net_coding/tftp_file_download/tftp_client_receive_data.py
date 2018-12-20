from socket import *
import struct
import os

def main():
    # set will receive file
    recv_file = raw_input("please input file name: ")
    len_recv_file = len(recv_file)

    pack_str = "!H%dsb5sb"%len_recv_file
    send_data = struct.pack(pack_str,1,recv_file,0,"octet",0)

    # create a socket
    udp_socket = socket(AF_INET, SOCK_DGRAM)
    udp_socket.bind(("",7788))

    # send request to tftp server
    udp_socket.sendto(send_data, ("10.0.2.7",69))

    # build receive file
    f = open(recv_file, "wb")
    back = ()

    # deal receive data
    while True:
        recv_data = udp_socket.recvfrom(1024)
        content, destination = recv_data
        result = struct.unpack("!HH", content[:4])
        f.write(content[4:])
        back = struct.pack("!HH",4,result[1])
        if result[0] == 5:
            print("%s don't resolve"%recv_file)
            f.close()
            os.remove(recv_file)
            break

        # check the file is all download
        if len(content) == 516:
            udp_socket.sendto(back,(destination[0],destination[1]))
        else:
            f.close()
            break

    udp_socket.close()


if __name__ == "__main__":
    main()
