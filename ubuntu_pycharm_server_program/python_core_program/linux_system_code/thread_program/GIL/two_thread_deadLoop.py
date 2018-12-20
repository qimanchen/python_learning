import threading

# son thread dead loop
def test():
    while True:
        pass


t1 = threading.Thread(target=test)
t1.start()

# main thread dead loop
while True:
    pass

