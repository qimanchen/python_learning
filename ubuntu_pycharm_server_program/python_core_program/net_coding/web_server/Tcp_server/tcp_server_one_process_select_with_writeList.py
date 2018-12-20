#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import queue
import select

SERVER_IP = ('', 9999)

# save msg from client and add it to queue
message_queue = {}
input_list = []
output_list = []

if __name__ == "__main__":
    server = socket.socket()
    server.bind(SERVER_IP)
    server.listen(10)

    # set the mode -- not interrupt
    server.setblocking(False)

    # add server to listened list
    input_list.append(server)

    while True:
        # start select listen, listen server in input_list
        stdinput, stdoutput, stderr = select.select(input_list, output_list, [])

        # check the client in? if yes
        for obj in stdinput:
            if obj == server:
                conn, addr = server.accept()
                print("client %s connected! " % str(addr))
                input_list.append(conn)
                message_queue[conn] = queue.Queue()

            else:
                pass
