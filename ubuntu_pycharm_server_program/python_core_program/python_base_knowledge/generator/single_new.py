class Dog(object):
    __count = None

    def __new__(cls):
        if cls.__count == None:
            cls.__count = object.__new__(cls)
            return cls.__count
        else:
            return cls.__count 


a = Dog()
print(id(a))
b = Dog()
print(id(b))
