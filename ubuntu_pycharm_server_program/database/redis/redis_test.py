#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import redis

# r = redis.StrictRedis(host='localhost', port=6379)

# write
# pipe = r.pipeline()
# pipe.set('py10', 'hello1')
# pipe.set('py11', 'world')
# pipe.execute()

# read
# temp = r.get('py10')
# print(temp)


class RedisHelper(object):
    """"""
    def __init__(self, host, port):
        self.__redis = redis.StrictRedis(host, port)

    def set(self, key, value):
        self.__redis.set(key, value)

    def get(self, key):
        return self.__redis.get(key)

