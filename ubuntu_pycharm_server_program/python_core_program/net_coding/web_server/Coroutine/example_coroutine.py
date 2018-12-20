import time

def A():
    while True:
        yield "---A---"
        time.sleep(0.5)

def B():
    while True:
        yield "---B---"
        time.sleep(0.5)

a = A()
b = B()

while True:
    print(next(a))
    print(next(b))

