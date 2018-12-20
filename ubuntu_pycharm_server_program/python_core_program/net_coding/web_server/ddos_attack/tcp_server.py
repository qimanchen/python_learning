import socket
import argparse
from threading import Thread

socket_list = []
# command type "#-H xxx.xxx.xxx.xxx -p xxxx -c <start|stop>"

# send msg command
def send_cmd(cmd):
    print("Send command...")
    for sock in socket_list:
        sock.send(cmd.encode("utf-8"))

# wait connect
def wait_connect(s):
    while True:
        sock, addr = s.accept()
        if sock not in socket_list:
            socket_list.append(sock)

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("0.0.0.0", 58868))
    s.listen(1024)
    t = Thread(target=wait_connect, args=(s,))
    t.start()

    print("Wait at least a client connection!")
    while not len(socket_list):
        pass
    print("It has benn a client connection!")

    while True:
        print("=" * 50)
        print("The command format:'#-H xxx.xxx.xxx.xxx -p xxxx -c <start>'")
        # wait input command
        cmd_str = input("please input cmd:")
        if len(cmd_str):
            if cmd_str[0] == "#":
                send_cmd(cmd_str)
    s.close()

if __name__ == "__main__":
    main()

