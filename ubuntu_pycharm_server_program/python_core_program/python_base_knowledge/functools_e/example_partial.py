import functools

def show_arg(*args,**kwargs):
    print(args)
    print(kwargs)


p1 = functools.partial(show_arg, 1,2,3)
p1()
p1(4,5,6)
p1(a='python', b='itcast')

p2 = functools.partial(show_arg, a=3,b='linux')
p2()
p2(1,2)
p2(a='python',b='itcast')

