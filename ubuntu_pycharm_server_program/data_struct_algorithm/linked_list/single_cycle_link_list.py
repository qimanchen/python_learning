#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Node(object):
    """
    single linked list node example by python coding
    Node using:
    node = Node(data, next_link_addr)
    """

    def __init__(self, elem):
        self.elem = elem
        self.next = None


class SingleLinkList(object):
    """
    single cycle link list example
    link list using:
        single_obj = SingleLinkList()
        single_obj.travel()
    """

    def __init__(self, node=None):
        """ initial a empty """
        self.__head = node
        if node:
            node.next = node

    def is_empty(self):
        return self.__head is None

    def length(self):
        """ calculate link list nodes num"""
        if self.is_empty():
            return 0
        # cur: point current node
        cur = self.__head
        # count record node num
        count = 1
        while cur.next != self.__head:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """ traversing all link list"""
        if self.is_empty():
            return
        cur = self.__head
        while cur.next != self.__head:
            print(cur.elem, end=" ")
            cur = cur.next
        print(cur.elem)

    def add(self, item):
        """ add new node from the link list head"""
        node = Node(item)

        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            # cur point the link list end_point
            node.next = self.__head
            self.__head = node
            cur.next = node

    def append(self, item):
        """ add new node from the link list end"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            node.next = cur.next
            cur.next = node

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
            pre = self.__head
            while pos - 1 != 0:
                pre = pre.next
                pos -= 1
            # when break loop, pre point the pos-1 location
            node = Node(item)
            node.next = pre.next
            pre.next = node

    def remove(self, item):
        """ delete special node(data)"""
        if self.is_empty():
            return
        cur = self.__head
        pre = None
        while cur.next != self.__head:
            if cur.elem == item:
                # check: if this node is head node
                if cur == self.__head:
                    # head node
                    rear = self.__head
                    while rear.next != self.__head:
                        rear = rear.next
                    self.__head = cur.next
                    rear.next = self.__head
                else:
                    # middle node
                    pre.next = cur.next
                # all steps is finish
                return
            else:
                pre = cur
                cur = pre.next
        # end node
        if cur.elem == item:
            if cur == self.__head:
                # link list has only one node
                self.__head = None
            else:
                pre.next = cur.next
                # pre.next = self.__head

    def search(self, item):
        # cur = self.__head
        # count = self.length()
        # while count != 0:
        #     if cur.elem == item:
        #         print(item)
        #         break
        #     cur = cur.next
        #     count -= 1
        # if count == 0:
        #     print("%s is not exist" % item)
        if self.is_empty():
            return False

        cur = self.__head
        while cur.next != self.__head:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        # the last node
        if cur.elem == item:
            return True
        return False


if __name__ == '__main__':
    ll = SingleLinkList()
    print(ll.is_empty())
    print(ll.length())

    ll.append(1)
    print(ll.is_empty())
    print(ll.length())

    ll.append(2)
    ll.add(8)
    ll.insert(-1, 9)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)

    ll.insert(2, 100)
    ll.insert(10, 200)

    ll.remove(100)
    ll.insert(1, 100)

    ll.travel()

    print(ll.search(200))
