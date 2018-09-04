#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import pygame
import sys

# 初始化pygame
pygame.init()

size = width, height = 600, 400
screen = pygame.display.set_mode(size)
pygame.display.set_caption("初次见面，请大家多多关照!")

# 打开文件
f = open("event_save.txt", "+w")
# 游戏循环
while True:
    # 监听退出事件的发生
    for event in pygame.event.get():
        # 显示文件
        f.write(str(event) + '\n')
        if event.type == pygame.QUIT:
            f.close()
            sys.exit()
