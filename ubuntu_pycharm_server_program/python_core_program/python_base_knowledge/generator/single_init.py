class Dog(object):
    __count = None
    __name = None

    def __new__(cls,name):
        if cls.__count == None:
            cls.__count = object.__new__(cls)
            return cls.__count
        else:
            return cls.__count
    def __init__(self, name):
        if Dog.__name == None:
            Dog.__name = name
            self.name = name
        else:
            self.name = Dog.__name

a = Dog("wang")
print(id(a))
print(a.name)
b = Dog("Xiao")
print(id(b))
print(b.name)
