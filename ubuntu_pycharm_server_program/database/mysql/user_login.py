#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from mysql_helper import MysqlHelper
from hashlib import sha1


if __name__ == '__main__':
    # receive user input
    name = input("请输入用户名：")
    pwd = input("请输入密码：")

    # code for password
    s1 = sha1()
    s1.update(pwd.encode('utf-8'))
    pwd2 = s1.hexdigest()

    # search code by user name
    sql = 'select passwd from users where name=%s'
    helper = MysqlHelper('192.169.56.2', 3306, 'root', 'odlodl', 'exercise_1')

    result = helper.all(sql, [name])
    if len(result) == 0:
        print('User name is error!')
    elif result[0][0] == pwd2:
        print("Log in success!")
    else:
        print("Password error!")
