#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Queue(object):
    """Queue"""

    def __init__(self):
        self.__list = []

    def enqueue(self, item):
        """ add new item to queue"""
        self.__list.append(item)

    def dequeue(self):
        """ remove a item from queue head"""
        return self.__list.pop(0)

    def is_empty(self):
        """ check this queue is or empty"""
        return self.__list == []

    def size(self):
        """ return queue size"""
        return len(self.__list)


if __name__ == '__main__':
    s = Queue()
    s.enqueue(1)
    s.enqueue(2)
    s.enqueue(3)
    s.enqueue(4)

    print(s.dequeue())
    print(s.dequeue())
    print(s.dequeue())
    print(s.dequeue())
