from multiprocessing import Pool
import os
import random

def worker():
    for i in range(random.randint(1,3)):
        print("---pid = %d---"%os.getpid())
pool = Pool(3)

for i in range(10):
    print("---%d---"%i)
    pool.apply_async(worker)

pool.close()
pool.join()

