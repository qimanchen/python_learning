def func(function_name):
    print("---func---1---")
    def func_in():
        print("---func_in---2---")
        func_return = function_name()
        print("---func_in---3---")
        return func_return

    print("---func---2---")
    return func_in

@func
def test():
    print("---test---")
    return "test return values"

ret = test()
print("test return value is %s" % ret)
