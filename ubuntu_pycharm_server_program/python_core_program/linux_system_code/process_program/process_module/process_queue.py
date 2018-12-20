from multiprocessing import Process, Queue
import os
import time
import random

# write process
def write(q):
    for value in ['A','B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())

# read process
def read(q):
    while True:
        if not q.empty():
            value = q.get(True)
            print('get %s from queue.' % value)
            time.sleep(random.random())
        else:
            break

# test
if __name__ == '__main__':
    # father process crete Queue and send to all son process
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # start pw, writing:
    pw.start()
    # wait pw end
    pw.join()

    # start pr, reading:
    pr.start()
    pr.join()

    print('')
    print('all data is writed.')
