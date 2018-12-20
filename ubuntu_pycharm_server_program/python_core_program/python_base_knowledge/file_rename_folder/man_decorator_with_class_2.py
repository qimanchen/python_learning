def message(param1, param2):
    def decorator(cls):
        def wrapper(*args,**kwargs):
            print("message %s %s" % (param1,param2))
            cls(*args,**kwargs)
        return wrapper
    return decorator

@message("param1","param2")
class Pizza(object):
    def __init__(self):
        pass

Pizza_with_message = Pizza()
