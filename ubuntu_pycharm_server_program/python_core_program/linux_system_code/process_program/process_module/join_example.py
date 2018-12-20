from multiprocessing import Process
import time
import random

def test():
    # son process just execute this part codes
    for i in range(random.randint(1,5)):
        print("---test---")
        time.sleep(1)

p = Process(target=test)
p.start()  # start son process

p.join()  # wait son process finish

print("---main---")
