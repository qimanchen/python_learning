#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import pygame
import sys
from pygame.locals import *

# 初始化pygame
pygame.init()

size = width, height = 600, 400

bg = (255, 255, 255) # 填充背景rgb

speed = [5, 0]

clock = pygame.time.Clock()

# 创建指定窗口大小 Surface
# Surface 对象 -- 图像
# 每一次呈现出来的是一个图像
screen = pygame.display.set_mode(size)

# 设置窗口标题
pygame.display.set_caption("初次见面，请大家多多关照!")

# 加载图片 jpg png gif (支持多动图像格式）
turtle = pygame.image.load("../fish_file/78/turtle.png")

turtle_right = pygame.transform.rotate(turtle, 90)
turtle_top = pygame.transform.rotate(turtle, 180)
turtle_left = pygame.transform.rotate(turtle, 270)
turtle_bottom = turtle

turtle = turtle_top

# 获取图像的位置矩形
position = turtle.get_rect()

# 图像翻转
l_head = turtle
r_head = pygame.transform.flip(turtle, True, False)

# 游戏循环
while True:
    # 监听退出事件的发生
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()

        # 监测键盘位置移动
        if event.type == KEYDOWN:
            pass

    # 移动图像
    # speed(水平，y)
    position = position.move(speed)

    # 监测边界
    # 左上角为零
    if position.right > width:
        turtle = turtle_right
        position = turtle_rect = turtle.get_rect()
        position.left = width - turtle_rect.width
        speed = [0, 5]

    if position.bottom > height:
        turtle = turtle_bottom
        position = turtle_rect = turtle.get_rect()
        position.left = width - turtle_rect.width
        position.top = height - turtle_rect.height
        speed = [-5, 0]

    if position.left < 0:
        turtle = turtle_left
        position = turtle_rect = turtle.get_rect()
        position.top = height - turtle_rect.height
        speed = [0, -5]

    if position.top < 0:
        turtle = turtle_top
        position = turtle_rect = turtle.get_rect()
        speed = [5, 0]

    # 填充背景
    screen.fill(bg)

    # 更新图像
    # 将背景的图像的改变图像素
    screen.blit(turtle, position)
    # 更新界面
    pygame.display.flip()
    # 延迟10ms
    # 如何控制游戏的运行速度 --- 帧率控制
    # 设置帧率
    clock.tick(100)
    # pygame.time.delay(10)
    # pygame效率 --- c语言的实现
