# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import easygui as g
from random import randint


def apple_sale_app():
    g.msgbox(msg="欢迎使用 man-man 苹果售卖系统", title="系统开始界面", image="apple.gif")
    # 1.输入苹果的单价
    price_str = g.enterbox(msg="请输入苹果的价格", title="价格输入界面")

    # 2.输入苹果的重量
    weight_str = g.enterbox(msg="请输入苹果的重量", title="重量输入界面")
    # 3. 计算支付的总金额
    money = float(price_str) * float(weight_str)
    # 4. 输出苹果总价
    g.msgbox(msg="您购买的苹果总价是:%.3f元" % money, title="苹果结算界面")
    # 5. 退出当前系统
    g.msgbox(msg="谢谢您的光临，欢迎下次再来！", title="系统退出提示界面")


# if 语句的使用
def net_age_sys():
    g.msgbox(msg="欢迎来到***** 黑马网吧 *****", title="网吧欢迎界面")
    age = g.enterbox(msg="请问您的年龄是:", title="年龄验证界面")

    if int(age) >= 18:
        g.msgbox(msg="哦哦，您可以进去海皮", title="欢迎界面")
    else:
        g.msgbox(msg="不好意思，您还未成年", title="验证提示")


def score_test():
    python_score = g.enterbox(msg="请输入您的python成绩", title="python成绩输入")
    c_score = g.enterbox(msg="请输入您的c语言成绩", title="c成绩输入")

    if int(python_score) >= 60 or int(c_score) >= 60:
        g.msgbox(msg="恭喜您程序设计课程通过", title="成绩通过")
    else:
        g.msgbox(msg="请继续努力", title="未通过")


def train_check():
    has_ticket = True

    knife_length = 30
    # 是否有车票
    if has_ticket:
        print("车票检查通过，准备开始安检")
        # 是否有刀
        if knife_length > 20:
            print("大哥你的刀 (%d 厘米) 太长了，公安局这边走" % knife_length)
        else:
            print("大哥，祝您旅途愉快")
    else:
        print("大哥请先买票")


def first_game():
    # 请双方出拳
    list_rule = [" ", "石头", "剪刀", "布"]
    computer_input = randint(1, 3)

    player_input = int(g.enterbox(msg="请您出拳!", title="Game"))
    # 显示出拳信息
    print("您的出拳是 %s - 电脑出拳是 %s" % (list_rule[player_input], list_rule[computer_input]))
    # 电脑输了
    if ((player_input == 1 and computer_input == 2)
            or (player_input == 2 and computer_input == 3)
            or (player_input == 3 and computer_input == 1)):
        print("欧耶，电脑sb了")
    # 平局
    elif player_input == computer_input:
        print("真是心有灵犀一点通，再来一盘")
    # 电脑获胜
    else:
        print("不服气，我们决战到天明")


# 打印阶梯形状的*
def print_stars():
    # 初始化行数和列数
    row = 1
    # 打印*的循环
    while row <= 5:
        # 每一行打印的*与行号的数量相同
        col = 1
        while col <= row:
            print("*", end="")
            col += 1
        print("")
        row += 1


def print_99multi_table():
    row = 1
    while row <= 9:
        col = 1
        while col <= row:
            print("%d * %d = %d" % (col, row, col * row), end="\t")
            col += 1
        print("")
        row += 1


# 测试模块
if __name__ == '__main__':
    print_99multi_table()
