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
    single link list example
    link list using:
        single_obj = SingleLinkList()
        single_obj.travel()
    """

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
        node.next = self.__head
        self.__head = node

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
            while pos-1 != 0:
                pre = pre.next
                pos -= 1
            # when break loop, pre point the pos-1 location
            node = Node(item)
            node.next = pre.next
            pre.next = node

    def remove(self, item):
        """ delete special node(data)"""
        cur = self.__head
        pre = None
        while cur is not None:
            if cur.elem == item:
                # check: if this node is head node
                if cur == self.__head:
                    self.__head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = pre.next
        
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
        cur = self.__head
        while cur is not None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
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
