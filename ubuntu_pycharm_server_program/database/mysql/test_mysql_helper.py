#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# import sys
# sys.path.insert(0, '/home/odl/python-E/python_heima/database/mysql')
from mysql_helper import MysqlHelper


if __name__ == '__main__':

    # modify
    name = input("请输入学生姓名：")
    id1 = input("请输入学生编号：")

    sql = 'update students set name=%s where id=%s'
    params = [name, id1]

    sql_helper = MysqlHelper('192.169.56.2', 3306, 'root', 'odlodl', 'exercise_1')
    sql_helper.cud(sql, params)

    # search
    # sql = 'select id, name from students where id<5'
    # sql_helper = MysqlHelper('192.169.56.2', 3306, 'root', 'odlodl', 'exercise_1')

    # result = sql_helper.all(sql)
    # print(result)
