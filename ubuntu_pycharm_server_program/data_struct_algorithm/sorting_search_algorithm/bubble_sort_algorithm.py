#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import time


def bubble_sort(a_list):
    """ Bubble sort achieve"""
    list_len = len(a_list)

    while list_len - 1:
        for i in range(list_len-1):

            if a_list[i] > a_list[i+1]:
                a_list[i], a_list[i+1] = a_list[i+1], a_list[i]
        print(a_list)
        list_len -= 1
    return a_list


def bubble_sort_improve(a_list):
    """ Bubble sort achieve"""
    list_len = len(a_list)

    while list_len - 1:
        count = 0
        for i in range(list_len - 1):
            if a_list[i] > a_list[i + 1]:
                a_list[i], a_list[i + 1] = a_list[i + 1], a_list[i]
                count += 1
        if count == 0:
            break
        list_len -= 1
    return a_list


def bubble_sort_example(a_list):
    """ Bubble sort achieve"""
    list_len = len(a_list)

    for j in range(list_len - 1):
        for i in range(list_len - 1 - j):

            if a_list[i] > a_list[i + 1]:
                a_list[i], a_list[i + 1] = a_list[i + 1], a_list[i]
        # print(a_list)
        list_len -= 1
    return a_list


if __name__ == "__main__":
    a_list = [54, 26, 93, 17, 77, 1000, 31, 44, 55, 20, 40]
    start_time = time.time()
    print(bubble_sort_improve(a_list))
    end_time = time.time()
    print(end_time - start_time)
