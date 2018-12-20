#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from hashlib import sha1
from mysql_helper import MysqlHelper


def register(user_name, passwd):

    sql = 'insert into users(name, passwd) values(%s, %s)'
    helper = MysqlHelper('192.169.56.2', 3306, 'root', 'odlodl', 'exercise_1')

    helper.cud(sql, [user_name, pwd2])


def test():

    sql = 'select name from users'
    sql_helper = MysqlHelper('192.169.56.2', 3306, 'root', 'odlodl', 'exercise_1')

    result = sql_helper.all(sql)
    print(result)


def check_name(in_name):
    sql = 'select name from users'
    sql_helper = MysqlHelper('192.169.56.2', 3306, 'root', 'odlodl', 'exercise_1')

    name_list = sql_helper.all(sql)
    for usr_name in name_list:
        if in_name == usr_name[0]:
            return False
    else:
        return True


if __name__ == '__main__':
    name = input("请输入注册名：")

    if check_name(name):
        pwd = input("请输入密码：")
        s1 = sha1()
        s1.update(pwd.encode('utf-8'))
        pwd2 = s1.hexdigest()
        register(name, pwd2)
    else:
        print("该用户名已存在！")
