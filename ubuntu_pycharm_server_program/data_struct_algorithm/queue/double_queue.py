#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Deque(object):
    """Queue"""

    def __init__(self):
        self.__list = []

    def add_front(self, item):
        """ add new item to queue from queue head"""
        self.__list.insert(0, item)

    def add_rear(self, item):
        """ add new item to queue from queue end"""
        self.__list.append(item)

    def pop_front(self):
        """ remove a item from queue head"""
        return self.__list.pop(0)

    def pop_rear(self):
        """ remove a item from queue end"""
        return self.__list.pop()

    def is_empty(self):
        """ check this queue is or empty"""
        return self.__list == []

    def size(self):
        """ return queue size"""
        return len(self.__list)


if __name__ == '__main__':
    s = Deque()
