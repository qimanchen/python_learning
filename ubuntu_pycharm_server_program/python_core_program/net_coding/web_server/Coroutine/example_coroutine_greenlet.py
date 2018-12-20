import greenlet
import time


def test1():
    while True:
        print("---A---")
        gr2.switch()
        time.sleep(0.5)

def test2():
    while True:
        print("---B---")
        gr3.switch()
        time.sleep(0.5)

def test3():
    while True:
        print("---C---")
        gr1.switch()
        time.sleep(0.5)


if __name__ == "__main__":
    gr1 = greenlet.greenlet(test1)
    gr2 = greenlet.greenlet(test2)
    gr3 = greenlet.greenlet(test3)

    gr1.switch()

