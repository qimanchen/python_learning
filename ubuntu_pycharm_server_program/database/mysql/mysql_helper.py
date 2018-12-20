#!/usr/bin/env python3


import pymysql


class MysqlHelper(object):
    """"""
    def __init__(self, host, port, user, passwd, db, charset='utf8'):
        self.host = host
        self.port = port
        self.user = user
        self.db = db
        self.password = passwd
        self.charset = charset

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


if __name__ == '__main__':
    pass
