from socket import *

conn_num = input("please input the max client num: ")

for client_num in range(int(conn_num)):
    s = socket(AF_INET, SOCK_STREAM)
    s.connect(("127.0.0.1", 7788))
    print(client_num)

