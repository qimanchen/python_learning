import functools

def note(func):
    "note function"
    # use wraps avoid function doc contents is error(test don't point to wrapper)
    @functools.wraps(func)
    def wrapper():
        "wrapper function"
        print('note something')
        return func()
    return wrapper

@note
def test():
    "test function"
    print('I am test')


test()
print(test.__doc__)
# Actually, the test function is point to wrapper
