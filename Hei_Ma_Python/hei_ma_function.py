#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def multi_9_9_function():
    """print multi 9 9 table"""
    row = 1
    while row <= 9:
        col = 1
        while col <= row:
            print("%d * %d = %d" % (row, col, row * col), end="\t")
            col += 1
        print("")
        row += 1
    return "success"


def str_to_float(string):
    """
    将字符串 string 转成 float型数字
    """

    str_mid = string.split(".")
    # 检测字符串中是否存在字母
    for i in range(len(str_mid)):
        if not str_mid[i].isdigit():
            return "非正常输入"
    result = 0
    if len(str_mid) > 1:
        for i in range(len(str_mid)):
            if i != 0:
                result += int(str_mid[i]) * (10**(-i))
            else:
                result += int(str_mid[i])
    else:
        result = int(string)
    return result


def sum_2_num():
    """对两个数求和"""
    # 参数的输入
    num1 = input("请输入相加的第一个参数: ")
    num2 = input("请输入相加的第二个参数: ")

    if len(num1.split(".")) > 1 or len(num2.split(".")) > 1:
        num1 = str_to_float(num1)
        num2 = str_to_float(num2)
        # print("%.2f + %.2f = %.2f" % (num1, num2, num1 + num2))
    else:
        num1 = int(num1)
        num2 = int(num2)
        # print("%d + %d = %d" % (num1, num2, num1 + num2))
    return num1 + num2


def print_line(char, times):
    """
    打印单行分割线
    :param char: 分割线中的字符
    :param times: 分割线中字符的个数
    """
    print(char * times)


def print_lines(in_char, num, num_lines):
    """
    打印多行分割线
    :param in_char: 分割线使用的字符
    :param num: 分割符打印的次数
    :param num_lines: 打印的行数
    """
    row = 0
    while row < num_lines:
        print_line(in_char, num)
        row += 1


if __name__ == "__main__":
    print_lines("+", 30, 3)
