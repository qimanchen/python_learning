#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time


def application(env, start_response):
    """"""
    print(env)
    status = "200 OK"
    headers = [
        ("Content-Type", "text/plain")
    ]
    start_response(status, headers)
    return time.ctime()
