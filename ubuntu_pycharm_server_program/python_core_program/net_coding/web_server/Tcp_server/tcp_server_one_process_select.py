import select
import socket
import sys

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind("", 7788)
server.listen(5)

inputs = [server, sys.stdin]

running = True

while True:

    # call select function, waiting inputs
    readable, writeable, exceptional = select.select(inputs, [], [])

    # data coming, loop
    for sock in readable:

        # The new link listened
        if sock == server:
            conn, addr = server.accept()
            # select listen socket
            inputs.append(conn)
        # check keyboard input?
        elif sock == sys.stdin:
            cmd = sys.stdin.readline()
            running = False
            break
        else:
            # read client data
            data = sock.recv(1024)
            if data:
                sock.send(data)
            else:
                # remove select listen socket
                inputs.remove(sock)
                sock.close()

    # if the keyboard have input, quit the server
    if not running:
        break

# close server socket
server.close()

