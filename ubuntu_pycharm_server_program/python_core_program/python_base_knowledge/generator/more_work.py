def test1():
    while True:
        print("____1____")
        yield None

def test2():
    while True:
        print("____2____")
        yield None

t1 = test1()
t2 = test2()
while True:
    t1.__next__()
    t2.__next__()
