#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def func(file_name):

    with open(file_name) as juf:
        data = juf.readline()
        julie = data.strip().split(',')
    return julie


julie = func(file_name="julie.txt")

print(julie)
