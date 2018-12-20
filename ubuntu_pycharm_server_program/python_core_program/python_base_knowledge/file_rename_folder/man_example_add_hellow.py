import sys
import inspect
def add_hello(func):
    def wrapped():
        print("Hello "+func.__name__)
        func()
    return wrapped

@add_hello
def test_func():
    print("call test_func...")


test_func()
