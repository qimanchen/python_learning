#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Node(object):
    """"""
    def __init__(self, item):
        self.elem = item
        self.lchild = None
        self.rchild = None


class Tree(object):
    """binary treee"""
    def __init__(self):
        self.root = None

    def add(self, item):
        node = Node(item)
        if self.root is None:
            self.root = node
            return
        queue = [self.root]

        while queue:
            cur_node = queue.pop(0)
            if cur_node.lchild is None:
                cur_node.lchild = node
                return
            else:
                queue.append(cur_node.lchild)

            if cur_node.rchild is None:
                cur_node.rchild = node
                return
            else:
                queue.append(cur_node.rchild)

    def breadth_travel(self):
        """ breadth treavel"""
        if self.root is None:
            return
        queue = [self.root]

        while queue:
            cur_node = queue.pop(0)
            print(cur_node.elem)
            if cur_node.lchild is not None:
                queue.append(cur_node.lchild)
            if cur_node.rchild is not None:
                queue.append(cur_node.rchild)

    def pre_order(self, node):
        """"""
        if node is None:
            return
        print(node.elem, end=" ")

        self.pre_order(node.lchild)
        self.pre_order(node.rchild)

    def mid_order(self, node):
        """middle order"""
        if node is None:
            return
        self.mid_order(node.lchild)
        print(node.elem, end=" ")
        self.mid_order(node.rchild)

    def post_order(self, node):
        """post order"""
        if node is None:
            return
        self.post_order(node.lchild)
        self.post_order(node.rchild)
        print(node.elem, end=" ")


if __name__ == '__main__':
    tree = Tree()
    tree.add(0)
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.add(8)
    tree.add(9)

    tree.breadth_travel()
    print("------")
    tree.pre_order(tree.root)
    print("------")
    tree.mid_order(tree.root)
    print(" ")
    tree.post_order(tree.root)
