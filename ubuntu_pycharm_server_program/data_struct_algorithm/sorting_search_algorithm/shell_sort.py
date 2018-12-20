#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def shell_sort(alist):
    """shell sort"""
    # n = 9
    n = len(alist)
    # gap = 4
    gap = n // 2
    # i = gap
    # gap change
    while gap >= 1:
        # the gap is difference for insert sort
        for j in range(gap, n):
            # j = [gap+1, gap+2, gap+3, gap+4, ... , n-1]
            i = j
            while i > 0:
                if alist[i] < alist[i-gap]:
                    alist[i], alist[i-gap] = alist[i-gap], alist[i]
                    # the interval
                    i -= gap
                else:
                    break
        # decrease gap step length
        gap //= 2


if __name__ == '__main__':
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(alist)
    shell_sort(alist)
    print(alist)
