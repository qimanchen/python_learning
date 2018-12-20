import os
import time

# father
ret = os.fork()

if ret==0:
    # son
    print("---1---")
else:
    # father
    print("---2---")

    ret = os.fork()
    if ret==0:
        # second son
        print("---11---")
    else:
        # father
        print("---22---")
