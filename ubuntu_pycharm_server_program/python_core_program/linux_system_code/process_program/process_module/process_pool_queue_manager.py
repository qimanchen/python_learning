from multiprocessing import Manager,Pool
import os
import time
import random

def reader(q):
    print("reader start(%s),father process is(%s)" % (os.getpid(),os.getppid()))
    for i in range(q.qsize()):
        print("reader from Queue get message: %s" % q.get(True))

def writer(q):
    print("writer start(%s),father process is (%s)" % (os.getpid(),os.getppid()))
    for i in "dongGe":
        q.put(i)

# test
if __name__ == "__main__":
    print("(%s) start" % os.getpid())
    # use Queue from Manager initial
    q = Manager().Queue()
    po = Pool()
    # use one module create process which don't using all loop in function reader
    po.apply(writer,(q,))
    po.apply(reader,(q,))
    po.close()
    po.join()
    print("(%s) End" % os.getpid())
