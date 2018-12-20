#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import socket
from multiprocessing import Process


def client_server(cli_socket):
    # read request_type
    with open("test.txt", "+w") as request_file:
        request_data = cli_socket.recv(1024).decode("utf-8")
        request_file.write(request_data)
        request_file.seek(0)
        request_detail = request_file.readline()
    # parse http request detail info
    request_type = request_detail.split()[0]
    request_content = request_detail.split()[1]
    http_protocol_version = request_detail.split()[2]

    HTML_ROOT_DIR = "."

    send_path = HTML_ROOT_DIR+request_content
    if request_content != "/":
        try:
            with open(send_path) as f:
                send_data = f.read()
        except:
            send_data = "HTTP1.1 404 Not Found\r\n\r\nnot found"
    else:
        send_data = "HTTP1.1 200 OK\r\n\r\nhello firefox"
    # return info to browser
    cli_socket.send(send_data.encode("utf-8"))


def main():
    # tcp socket server
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(("", 8000))
    server_socket.listen(5)

    try:
        while True:
            print("--- main program for wait client come in ---")
            cli_socket, addr = server_socket.accept()
            client = Process(target=client_server, args=(cli_socket,))
            client.start()
            # must close client at here
            cli_socket.close()
    finally:
        server_socket.close()


if __name__ == "__main__":
    main()
