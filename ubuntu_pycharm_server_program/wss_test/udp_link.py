#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import socket


def client():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    send_addr = ("192.169.3.200", 5025)
    recv_addr = ("", 7788)
    udp_socket.bind(recv_addr)

    # send msg to wss
    while True:
        send_data = input("please input send content: > ")

        # code the send msg
        udp_socket.sendto(send_data.encode("utf-8"), send_addr)

        # receive msg from wss
        recv_data = udp_socket.recvfrom(1024)

        content, destination = recv_data
        print(recv_data)


if __name__ == '__main__':
    client()
