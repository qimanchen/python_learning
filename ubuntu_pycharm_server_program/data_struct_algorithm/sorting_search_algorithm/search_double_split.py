#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def search(alist, value, first, end):
    """binary search"""
    first_index, last_index = first, end
    mid = first_index + (last_index - first_index) // 2
    if (last_index - first_index) != 0:
        if alist[mid] == value:
            return mid
        elif alist[mid] > value:
            first_index = first
            last_index = mid
        else:
            first_index = mid + 1
            last_index = end
        return search(alist, value, first_index, last_index)
    return False


def binary_search(alist, item):
    """"""
    n = len(alist)
    mid = n//2
    if n > 0:
        if alist[mid] == item:
            return True
        elif item < alist[mid]:
            return binary_search(alist[:mid], item)
        else:
            return binary_search(alist[mid+1:], item)
    return False


def binary_search_2(alist, item):
    """"""

    n = len(alist)
    first = 0
    last = n - 1
    while first <= last:
        mid = (last + first) // 2

        if alist[mid] == item:
            return True
        elif item < alist[mid]:
            last = mid - 1
        else:
            first = mid + 1
    return False


if __name__ == '__main__':
    test_list = [1, 3, 5, 7, 11, 13, 16, 23]
    index = binary_search_2(test_list, 16)
    print(index)
