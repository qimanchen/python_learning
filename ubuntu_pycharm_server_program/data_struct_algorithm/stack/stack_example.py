#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Stack(object):
    """stack example by python list"""
    def __init__(self):
        self.__list = []

    def push(self, item):
        """add new item to stack top"""
        self.__list.append(item)
        # self.__list.insert(0, item)

    def pop(self):
        """get stack top item"""
        return self.__list.pop()
        # self.__list.pop()

    def peek(self):
        """"""
        if self.__list:
            return self.__list[-1]
        else:
            return None

    def is_empty(self):
        """"""
        return not self.__list
        # return self.__list == []

    def size(self):
        """"""
        return len(self.__list)


if __name__ == '__main__':
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)

    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())
