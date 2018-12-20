import os
import time

ret = os.fork()
reb = os.fork()

if ret==0:
    if reb==0:
        while True:
            print("---1---")
            time.sleep(3)
    else:
        while True:
            print("---2---")
            time.sleep(3)
else:
    if reb==0:
        while True:
            print("---3---")
            time.sleep(3)
    else:
        while True:
            print("---4---")
            time.sleep(3)
