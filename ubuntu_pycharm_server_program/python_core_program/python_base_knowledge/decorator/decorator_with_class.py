def message(param1, param2):
    def wrapper(wrapped):
        class WrappedClass(wrapped):
            def __init__(self):
                self.param1 = param1
                self.param2 = param2
                super(WrappedClass, self).__init__()

            def get_message(self):
                return "message %s %s" % (self.param1, self.param2)

        return WrappedClass
    return wrapper

@message("param1","param2")
class Pizza(object):
    def __init__(self):
        pass

pizza_with_message = Pizza()

print(pizza_with_message.get_message())

