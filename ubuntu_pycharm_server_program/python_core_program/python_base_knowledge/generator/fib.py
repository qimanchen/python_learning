#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# normal - list
def fib_list():
    a,b = 0,1
    for i in range(5):
        print(b)
        a,b = b, a+b

def fib_generator():
    a,b = 0,1
    print("------1------")
    for i in range(5):
        print("------2------")
        yield b
        print("-----3-----")
        a,b = b, a+b

def fib(n):
    if n<=0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

if __name__ == '__main__':
    fib_list()
    fib_generator()
