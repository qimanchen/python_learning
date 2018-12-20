#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def quick_sort(alist, first, last):
    """quick sort"""

    if first >= last:
        return alist
    mid_value = alist[first]
    low = first
    high = last

    while low < high:
        # high running -- move to left
        # This equal is for all same date in the list same side
        while low < high and alist[high] >= mid_value:
            high -= 1
        # start low loop
        alist[low] = alist[high]
        # low += 1
        # low running -- move to right
        while low < high and alist[low] < mid_value:
            low += 1
        alist[high] = alist[low]
        # high -= 1
    # from loop quit low == high
    alist[low] = mid_value
    # for continue run quick sort to any part
    # for list in low left sort
    quick_sort(alist, first, low-1)
    # for list in low right sort
    quick_sort(alist, low+1, last)


def quick_sort_learning(alist):
    pass


if __name__ == '__main__':
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    n = len(alist)
    print(alist)
    quick_sort(alist, 0, n-1)
    print(alist)
