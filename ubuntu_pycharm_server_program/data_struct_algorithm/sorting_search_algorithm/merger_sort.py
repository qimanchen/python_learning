#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def merger_sort(alist):
    """merger sort"""
    n = len(alist)
    if n <= 1:
        return alist
    mid = n//2
    # alist[:mid],alist[mid:] split this two part
    left_li = merger_sort(alist[:mid])

    # right this means one new son list of alist
    right_li = merger_sort(alist[mid:])

    # combine two son list to one list
    # merger(left, right)
    left_pointer, right_pointer = 0, 0
    result = []

    while left_pointer < len(left_li) and right_pointer < len(right_li):

        if left_li[left_pointer] < right_li[right_pointer]:
            result.append(left_li[left_pointer])
            left_pointer += 1
        else:
            result.append(right_li[right_pointer])
            right_pointer += 1

    result += left_li[left_pointer:]
    result += right_li[right_pointer:]

    return result


if __name__ == '__main__':
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(alist)
    sorted_li = merger_sort(alist)
    print(alist)
    print(sorted_li)
