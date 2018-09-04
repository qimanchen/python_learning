#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import pygame
import sys

# 初始化pygame
pygame.init()

size = width, height = 600, 400
speed = 1
# 图片背景颜色白色
bg = (255, 255, 255) # 填充背景rgb

clock = pygame.time.Clock()

# 创建指定窗口大小 Surface
# Surface 对象 -- 图像
# 每一次呈现出来的是一个图像
"""
flags:
    FULLSCREEN： 全屏模式
    DOUBLEBUF：双缓冲模式
    HWSURFACE: 硬件加速支持（只有全屏模式下使用）
    OPENGL: 使用OpenGL渲染
    RESIZABLE： 使得窗口可调整大小
    NOFRAME:使得窗口没有边框和控制按钮
"""
screen = pygame.display.set_mode(size)

# 设置窗口标题
pygame.display.set_caption("初次见面，请大家多多关照!")

# 加载图片 jpg png gif (支持多动图像格式）
turtle = pygame.image.load("../../fish_file/78/turtle.png")

# 获取图像的位置矩形
position = turtle.get_rect()
# print(position)

# 图像翻转
l_head = turtle
r_head = pygame.transform.flip(turtle, True, False)

# 游戏循环
while True:
    # 监听退出事件的发生
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        # 监测键盘位置移动
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                turtle = l_head
                position.left -= speed
            if event.key == pygame.K_RIGHT:
                turtle = r_head
                position.right += speed
            if event.key == pygame.K_UP:
                position.top -= speed
            if event.key == pygame.K_DOWN:
                position.bottom += speed

    # 移动图像
    # speed(水平，y)
    # position = position.move(speed)

    # 监测边界
    # 左上角为零
    if position.left < 0 or position.right > width:
        # 翻转图像
        # （figure, 水平翻转， 垂直翻转）
        turtle = pygame.transform.flip(turtle, True, False)

        # 反向移动
        speed = -speed

    if position.top < 0 or position.bottom > height:
        speed = -speed

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
    clock.tick(300)
    # pygame.time.delay(10)
    # pygame效率 --- c语言的实现
