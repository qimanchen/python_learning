import os
import time

ret = os.fork()
if ret==0:
    print("---son process---")
    time.sleep(1)
    print("---son process over---")
else:
    print("---father process---")
    time.sleep(4)

print("---over---")  # This will be execute twice
