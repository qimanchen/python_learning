# the first decorator
def make_bold(fn):
    def wrapped():
        print("----1----")
        return "<b>" + fn() + "</b>"
    return wrapped

# the second decorator
def make_italic(fn):
    def warpped():
        print("----2----")
        return "<i>" + fn() +"</i>"
    return warpped

# call on decorator
@make_bold
def test1():
    print("----test1----")
    return "hello world-2"

# call two decorator
@make_bold
@make_italic
def test3():
    print("----3----")
    return "hellow world-3"


# call test3 for test call two decorator
print(test3())

# call test1 for test call on decorator
test1()
