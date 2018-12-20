def w1(func):
    print("---docorating 1---")
    def inner():
        print("---checking 1---")
        func()
    return inner

def w2(func):
    print("---docorating 2---")
    def inner():
        print("---checking 2---")
        func()
    return inner

@w1
@w2
def f1():
    print("---f1---")

f1()
