# define general decorator
def func(function_name):
    def func_in(*args,**kwargs):
        print("---call %s---"%function_name.__name__)
        ret = function_name(*args,**kwargs)
        return ret
    return func_in

# define a function 
@func
def no_return():
    pass
@func
def need_return():
    return "test function with return value"

@func
def with_argus(a,b):
    print("---a=%d,b=%d---"%(a,b))


# call all test function
no_return()
need_return()
with_argus(10,12)

