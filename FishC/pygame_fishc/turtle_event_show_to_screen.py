#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import pygame
import sys
from pygame.locals import *

# 初始化pygame
pygame.init()

size = width, height = 600, 400
screen = pygame.display.set_mode(size)
pygame.display.set_caption("FishC Demo")
bg = (0, 0, 0)

# 实例化一个font对象
# 字体， 大小
font = pygame.font.Font(None, 20)
# 填充背景
screen.fill(bg)
position = 0
# 设置文本单行的行高
line_height = font.get_linesize()

# 游戏循环
while True:
    # 监听退出事件的发生
    for event in pygame.event.get():
        if event.type == QUIT:
            # release pygame all modules
            pygame.quit()
            sys.exit()
        # render（文本，是否消除锯齿，字体颜色）
        # blit（字体加在到背景图像上，位置）
        screen.blit(font.render(str(event), True, (0, 255, 0)), (0, position))
        # 更新位置到下一行
        position += line_height

        # 行数大于整个屏幕的高度
        if position > height:
            # 清屏
            position = 0
            screen.fill(bg)

    # 屏幕的更新
    pygame.display.flip()
