#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import socket
import re

from multiprocessing import Process


HTML_ROOT_DIR = "."  # the server root directory


def request_handle(client_socket):
    """handle client request"""
    request_data = client_socket.recv(1024)
    print(request_data)

    request_lines = request_data.splitlines()

    request_start_line = request_lines[0]
    # match / directory
    file_name = re.match(r"\w+ +(/[^ ]*) ", request_start_line.decode("utf-8")).group(1)

    if "/" == file_name:
        file_name = "/first_html.html"
    # open file, read content of file
    try:
        file = open(HTML_ROOT_DIR + file_name, "rb")

    except IOError:
        response_start_line = "HTTP1.1 404 Not Found\r\n"
        response_headers = "Server: My server\r\n"
        response_body = "The file is not found!"
    else:
        # response some info
        file_data = file.read()
        file.close()
        response_start_line = "HTTP1.1 200 OK\r\n"
        response_headers = "Server: My server\r\n"
        response_body = file_data.decode("utf-8")

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
            print("[%s, %s] link the server" % (client_address[0], client_address[1]))

            # client process
            client = Process(target=request_handle, args=(client_socket,))
            client.start()
            client_socket.close()
    finally:
        server_socket.close()


if __name__ == '__main__':
    main()
