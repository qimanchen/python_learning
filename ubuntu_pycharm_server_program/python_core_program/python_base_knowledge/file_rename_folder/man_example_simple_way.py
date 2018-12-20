def w1(func):
    def inner():
        print("check invoke permission")
        func()
    return inner
@w1
def f1():
    print("----f1----")

def f2():
    print("----f2----")

#inner_func = w1(f1)
#inner_func()

# f1 = w1(f1)
f1()

inner_func = w1(f2)
inner_func()
