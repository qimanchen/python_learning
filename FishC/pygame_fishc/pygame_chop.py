#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import pygame
import sys
from pygame.locals import *


pygame.init()

size = width, height = 640, 480
bg = (255, 255, 255)

clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("FishC Demo")

oturtle = pygame.image.load("../fish_file/78/turtle.png")

# chop achieve
# cut picture
# capture = screen.subsurface(select_rect).copy()
turtle = pygame.transform.chop(oturtle, (107, 110, 50, 50))

# turtle = oturtle.copy()

position = turtle.get_rect()
position.center = width // 2, height // 2

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(bg)
    screen.blit(turtle, position)

    # 绘制一个矩形框
    pygame.draw.rect(screen, (0, 0, 0), position, 1)
    # rect(Surface, color, Rect, width=0)
    # 绘制图像，矩形颜色，矩形的范围，指定边框的大小，0 -- 填充矩形，1 -- 一个像素大小

    pygame.display.flip()

    clock.tick(30)
