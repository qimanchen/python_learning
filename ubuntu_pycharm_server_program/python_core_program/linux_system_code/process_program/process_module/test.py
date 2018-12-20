from multiprocessing import Process
import time

def test():
    # son process just execute this part codes
    while True:
        print("---test---")
        time.sleep(1)

p = Process(target=test)
p.start()  # start son process
# father process will wait son process end
print("---This is main---")

