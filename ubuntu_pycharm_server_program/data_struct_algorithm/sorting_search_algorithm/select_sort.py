#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def select_sort(alist):
    len_alist = len(alist)
    min_num = 0
    while len_alist:
        for i in range(min_num + 1, len_alist):
            if alist[min_num] > alist[i]:
                alist[min_num], alist[i] = alist[i], alist[min_num]
        len_alist -= 1
        min_num += 1
    print(alist)


def select_sort_1(alist):
    """select sort"""
    n = len(alist)

    for j in range(n-1):
        min_num = j
        for i in range(min_num + 1, n):
            if alist[min_num] > alist[i]:
                min_num = i
        alist[j], alist[min_num] = alist[min_num], alist[j]


def select_sort_max(alist):
    """insertion sort"""
    n = len(alist)

    while n - 1:
        max_index = n - 1
        for i in range(max_index):
            if alist[max_index] < alist[i]:
                max_index = i
        alist[n-1], alist[max_index] = alist[max_index], alist[n-1]
        n -= 1


if __name__ == '__main__':
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(alist)
    select_sort_max(alist)
    print(alist)
