import os
import time

ret = os.fork()
if ret==0:
    # son
    print("---1---")
else:
    # father
    print("---2---")
# son and father
ret = os.fork()
if ret==0:
    # father - second son
    # son - son(grandson for father)
    print("---11---")
else:
    # son
    # father
    print("---22---")

