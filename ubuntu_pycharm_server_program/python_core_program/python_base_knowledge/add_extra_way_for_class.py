#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import types
class Persion(object):

    def __init__(self, new_name):
        self.name = new_name


first_persion = Persion("First Man")

# add a extral class way
def run(self):
    print("----%s is running----"%self.name)

first_persion.run = types.MethodType(run, first_persion)

first_persion.run()
