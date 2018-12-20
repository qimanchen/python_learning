def func(function_name):
    print("---func---1---")
    def func_in(*args, **kwargs):
        print("---func_in---2---")
        function_name(*args,**kwargs)
        print("---func_in---3---")

    print("---func---2---")
    return func_in
@func
def test(a,b):
    print("---test-a=%d,b=%d---"%(a,b))

#test = func(test)
test(10,12)
test(20,30)
