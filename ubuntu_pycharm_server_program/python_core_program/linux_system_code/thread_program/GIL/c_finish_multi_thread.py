from ctypes import *
from threading import Thread

# load flexible library
lib = cdll.LoadLibrary("./libdead_loop.so")

# create a son thread, run c code, it's a dead loop
t = Thread(targer=lib.DeadLoop)
t.start()

# main thread, also call c code which is dead loop.
lib.DeadLoop()

