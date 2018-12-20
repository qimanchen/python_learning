#!/usr/bin/env
# -*- coding: utf-8 -*-


# from . import single_linked_list as sll


class Node(object):
    """ node"""

    def __init__(self, item):
        self.elem = item
        self.next = None
        self.prev = None


class DoubleLinkList(object):
    """double direction link"""

    def __init__(self, node=None):
        """ initial a empty """
        self.__head = node

    def is_empty(self):
        return self.__head is None

    def length(self):
        """ calculate link list nodes num"""
        # cur: point current node
        cur = self.__head
        # count record node num
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """ traversing all link list"""
        cur = self.__head
        while cur is not None:
            print(cur.elem, end=" ")
            cur = cur.next
        print()

    def add(self, item):
        """ add new node from the link list head"""
        node = Node(item)
        # 1. new node.next -> p
        node.next = self.__head
        # 2. head -> new node
        self.__head = node
        # 3. node.next
        node.next.prev = node

    def append(self, item):
        """ add new node from the link list end"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next is not None:
                cur = cur.next
            cur.next = node
            node.prev = cur

    def insert(self, pos, item):
        """
        add new node from the link list any address
        param:
            pos -- start 0
        """
        if pos <= 0:
            self.add(item)
        elif pos > (self.length() - 1):
            self.append(item)
        else:
            cur = self.__head
            count = 0
            while count < pos:
                count += 1
                cur = cur.next
            # when break loop, pre point the pos-1 location
            node = Node(item)
            node.next = cur
            node.prev = cur.prev
            cur.prev.next = node
            cur.prev = node

    def remove(self, item):
        """ delete special node(data)"""
        cur = self.__head
        while cur is not None:
            if cur.elem == item:
                # check: if this node is head node
                if cur == self.__head:
                    self.__head = cur.next
                    if cur.next:
                        # check this link list has only one node
                        cur.next.prev = None
                else:
                    cur.prev.next = cur.next
                    if cur.next:
                        # check cur is this link list end node
                        cur.next.prev = cur.prev
                break
            else:
                cur = cur.next

    def search(self, item):

        cur = self.__head
        while cur is not None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False


if __name__ == '__main__':
    dll = DoubleLinkList()
    print(dll.is_empty())
    print(dll.length())

    dll.append(1)
    print(dll.is_empty())
    print(dll.length())

    dll.append(2)
    dll.add(8)
    dll.insert(-1, 9)
    dll.append(3)
    dll.append(4)
    dll.append(5)
    dll.append(6)

    dll.insert(2, 100)
    dll.insert(10, 200)

    dll.remove(100)
    dll.insert(1, 100)

    dll.travel()

    print(dll.search(200))