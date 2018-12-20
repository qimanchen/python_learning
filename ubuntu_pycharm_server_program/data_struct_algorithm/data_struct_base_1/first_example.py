#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import time


"""
The problem description:
    if a+b+c=1000 and a^2+b^2=c^2, How get all possible set for all a,b and c value
"""


def way_1():
    """The first way for resolve this problem"""
    loop_range = range(0, 1001)

    for a in loop_range:
        for b in loop_range:
            for c in loop_range:
                condition_1 = a+b+c
                condition_2 = a**2+b**2
                if 1000 == condition_1 and c**2 == condition_2:
                    print(a, b, c)


def way_2():
    """
    The first way for resolve this problem
    Thinks:
        c = 1000 - (a +b)
    """
    start_time = time.time()
    loop_range = range(0, 1001)

    for a in loop_range:
        for b in loop_range:
            c = 1000 - a - b
            condition_1 = a+b+c
            condition_2 = a**2+b**2
            if 1000 == condition_1 and c**2 == condition_2:
                print("a, b, c: %s %s %s" % (a, b, c))
    end_time = time.time()
    print("This way running time is: %s" % (end_time-start_time))


if __name__ == '__main__':
    way_2()
