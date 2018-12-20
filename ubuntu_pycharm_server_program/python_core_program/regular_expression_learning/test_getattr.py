#!/usr/bin/env python2
# -*- coding: utf-8 -*-


class Foo(object):
    """"""
    def __init__(self):
        pass

    def __getattr__(self, item):
        print(item, end=" ")
        return self

    def __str__(self):
        return ""

# obj = Foo()
# "think" obj.think
# obj.different


print(Foo().think.differen.itcast)

# output --> think different itcast
