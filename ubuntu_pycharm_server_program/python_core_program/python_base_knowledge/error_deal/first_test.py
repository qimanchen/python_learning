# -*- coding: utf-8 -*-

try:
    2/1
    num = 4
    print(num)
except ZeroDivisionError,NameError:
    print("---get specific error---")
except Exception as error_info:
    print(error_info)
    
