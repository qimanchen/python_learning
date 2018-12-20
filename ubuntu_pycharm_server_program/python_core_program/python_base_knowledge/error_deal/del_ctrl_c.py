import time

try:
    while True:
        print("---Hei Hei---")
        time.sleep(2)
except KeyboardInterrupt:
    print("---man-made quit dead loop---")


