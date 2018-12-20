# define a decorator it need a arguments
def log(info):
    def decorator(func):
        def wrapped(*args,**kwargs):
            if info == "test1":
                ret = func(*args,**kwargs)
            else:
                print("print log info %s" % info)
                ret = func(*args,**kwargs)
            return ret
        return wrapped
    return decorator


# define test function
@log("test1")
def test1():
    print("---excute test1---")

@log("test2")
def test2():
    print("---excute test2---")

# call test function
test1()
test2()
