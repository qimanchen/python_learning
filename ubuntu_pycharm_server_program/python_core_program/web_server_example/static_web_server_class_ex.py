#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import socket

from multiprocessing import Process


HTML_ROOT_DIR = "."  # the server root directory


def request_handle(client_socket):
    """handle client request"""
    request_data = client_socket.recv(1024)
    print(request_data)

    # response some info
    response_start_line = "HTTP1.1 200 OK\r\n"
    response_headers = "Server: My server\r\n"
    response_body = "hello itcast"
    response = response_start_line+response_headers+"\r\n"+response_body
    print(response)

    # send response data to browser
    # client_socket.send(response.encode("utf-8"))
    client_socket.send(bytes(response, "utf-8"))

    # close client socket
    # client_socket.close()


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server_socket.bind(("", 8000))
    server_socket.listen(128)

    # multi process for more client
    try:
        while True:
            client_socket, client_address = server_socket.accept()
            print("[%s, %s] link the server" % client_address)

            # client process
            client = Process(target=request_handle, args=(client_socket,))
            client.start()
            client_socket.close()
    finally:
        server_socket.close()


if __name__ == '__main__':
    main()
