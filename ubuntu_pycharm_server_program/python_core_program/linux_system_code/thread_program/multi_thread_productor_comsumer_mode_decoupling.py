# -*- coding: utf-8 -*-

import threading
import time
# in python2
# from Queue import Queue

# in python3
from queue import Queue

class Producer(threading.Thread):
    def run(self):
        global queue
        count = 0
        while True:
            if queue.qsize() < 1000:
                for i in range(100):
                    count = count + 1
                    msg = "product goods" + str(count)
                    queue.put(msg)
                    print(msg)
            time.sleep(0.5)


class Consumer(threading.Thread):
    def run(self):
        global queue
        while True:
            if queue.qsize() > 100:
                for i in range(3):
                    msg = self.name + "cost" + queue.get()
                    print(msg)
            time.sleep(1)


if __name__ == "__main__":
    queue = Queue()

    for i in range(500):
        queue.put("start produce" + str(i))

    for i in range(2):
        p = Producer()
        p.start()

    for i in range(5):
        c = Consumer()
        c.start()

