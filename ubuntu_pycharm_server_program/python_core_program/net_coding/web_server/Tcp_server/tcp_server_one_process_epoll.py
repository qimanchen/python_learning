import socket
import select


def main():
    # create server_socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # set reuse bind info(port)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # bind local port
    server_socket.bind(('', 7788))

    # Passive monitoring
    server_socket.listen(5)

    # create a epoll object
    epoll = select.epoll()

    # add server_socket to epoll event listen list
    epoll.register(server_socket.fileno(), select.EPOLLIN | select.EPOLLET)

    connections = {}
    addresses = {}

    # loop for waiting client coming or send msg to here(server)
    while True:
        epoll_list = epoll .poll()

        # event judge and handle
        for fd, events in epoll_list:
            # server_socket trigger
            if fd == server_socket.fileno():
                conn, addr = server_socket.accept()
                print("new client %s" % str(addr))

                # save conn and addr info
                connections[conn.fileno()] = conn
                addresses[conn.fileno()] = addr
                # register new client socket to epoll
                epoll.register(conn.fileno(), select.EPOLLIN | select.EPOLLET)

            elif events == select.EPOLLIN:
                # from trigger fd receive data
                recv_data = connections[fd].recv(1024)

                if len(recv_data) > 0:
                    print('recv:%s' % recv_data)
                else:
                    # client socket quit, remove the socket from epoll
                    epoll.unregister(fd)

                    # close client socket
                    connections[fd].close()

                    print("%s---offline---"% str(addresses[fd]))

