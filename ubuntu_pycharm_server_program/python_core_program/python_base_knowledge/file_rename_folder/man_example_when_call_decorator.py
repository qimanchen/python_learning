def w1(func):
    print("decorating...")
    def inner():
        print("check invoke permission")
        func()
    return inner

@w1
def f1():
    print("----f1----")

