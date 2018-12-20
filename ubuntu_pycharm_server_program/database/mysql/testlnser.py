#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import pymysql
# import MySQLdb -- python2


def main():
    try:
        conn = pymysql.connect(host='192.169.56.2', port=3306,
                               user='root', passwd='odlodl',
                               db='exercise_1', charset='utf8')
        cursor1 = conn.cursor()

        # execute command -- like mysql command line sentence
        sql = 'insert into students(name) values("尘世")'
        cursor1.execute(sql)

        conn.commit()

        # close connection
        cursor1.close()
        conn.close()
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
