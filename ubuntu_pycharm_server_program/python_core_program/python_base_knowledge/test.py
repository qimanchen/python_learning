from functools import wraps
# create a decorator
def decorator(log):
    def wrapper(func):
        print("---start %s---"%func.__name__)
        return func
    return wrapper

def log(msg):
    def decorator(func):
        @wraps(func)
        def wrapper(*args,**kwargs):
            print("---start %s---"%func.__name__)
            ret = func(*args,**kwargs)
            print("---end %s ---"%func.__name__)
            return ret
        return wrapper
    return decorator

# running function
#@decorator("Hello, I'm a decorator")
@log("Hello, I'm log")
def test(a):
    print("a is %d"%a)


# test code
test(10)

