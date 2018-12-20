#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import pymongo


# 获得客服端，建立连接
client = pymongo.MongoClient('mongodb://10.0.2.32:27018/py3')

db = client.py3
stu = db.stu

# insert
s1 = stu.insert_one({'name': '张三丰'})

# 修改
stu.update_one({'name': '张三丰'}, {'$set': {'name': 'abc'}})

# 删除
stu.delete_one({'name': 'abc'})

# 查询
cursor = stu.find({'age': {'$gt': 20}})
for s in cursor:
    print(s['name'])


