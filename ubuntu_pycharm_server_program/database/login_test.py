#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pymysql
import redis
from hashlib import sha1


class MysqlHelper(object):
    """"""
    def __init__(self, host, port, user, passwd, db, charset='utf8'):
        self.host = host
        self.port = port
        self.user = user
        self.db = db
        self.password = passwd
        self.charset = charset
        self.conn = None
        self.cursor = None

    def open(self):
        self.conn = pymysql.connect(host=self.host, port=self.port,
                                    user=self.user, passwd=self.password,
                                    db=self.db, charset=self.charset)
        self.cursor = self.conn.cursor()

    def close(self):
        self.cursor.close()
        self.conn.close()

    def cud(self, sql, params):
        try:
            self.open()

            self.cursor.execute(sql, params)
            self.conn.commit()

            self.close()

            print('OK')
        except Exception as e:
            print(e)

    def all(self, sql, params=[]):
        try:
            self.open()
            self.cursor.execute(sql, params)

            result = self.cursor.fetchall()

            self.close()
            return result
        except Exception as e:
            print(e)

    def one(self, sql, params=[]):
        try:
            self.open()

            self.cursor.execute(sql, params)
            result = self.cursor.fetchone()

            self.close()
            return result
        except Exception as e:
            print(e)


class RedisHelper(object):
    """"""
    def __init__(self, host, port):
        self.__redis = redis.StrictRedis(host, port)

    def set(self, key, value):
        self.__redis.set(key, value)

    def get(self, key):
        return self.__redis.get(key)


if __name__ == '__main__':
    # 接受收入
    name = input("请输入用户名：")
    pwd1 = input("请输入密码：")

    # 加密
    s1 = sha1()
    s1.update(pwd1.encode("utf-8"))
    pwd2 = s1.hexdigest()

    # 查询redis中是否存在此用户
    r = RedisHelper('localhost', 6379)
    m = MysqlHelper('localhost', 3306, 'root', 'odlodl', 'exercise_1')
    # 判断redis是否存储了此用户
    if r.get(name) is None:
        sql = 'select passwd from users where name=%s'
        pwd3 = m.one(sql, [name])

        if pwd3 is None:
            print("用户名错误")
        else:
            # 只要从mysql中查到数据就存到redis中
            r.set(name, pwd3[0])
            # check password
            if pwd3[0] == pwd2:
                print("成功")
            else:
                print("密码错误")
    else:
        if r.get(name) == pwd2:
            print("成功")
        else:
            print("密码错误")
