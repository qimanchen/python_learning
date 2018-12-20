class Dog(object):
    def __init__(self):
        print("---init---")

    def __del__(self):
        print("---del---")
    
    def __str__(self):
        print("---str---")
        return "discription for Dog"

    def __new__(cls):
        print("---new---")
        super(cls,Dog).__new__(cls)

t = Dog()
