#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def insert_sort(alist):
    """insert sort"""
    n = len(alist)
    for j in range(1, n):
        # i -- the start value
        i = j
        while i > 0:
            # from not order part get a value insert to order part (the list front)
            if alist[i] < alist[i-1]:
                alist[i], alist[i-1] = alist[i-1], alist[i]
                i -= 1
            # avoid not must compare steps -- improve
            else:
                break


if __name__ == '__main__':
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(alist)
    insert_sort(alist)
    print(alist)
