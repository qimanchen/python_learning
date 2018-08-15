#!/usr/bin/env python3
# -*- coding: utf8 -*-

import pygame
from Hei_Ma_Python.hei_ma_pygame.plane_sprites import GameSprite


# game initial
pygame.init()

# load game's window
screen = pygame.display.set_mode((480, 700))

# load background image to game's window
bg = pygame.image.load("./images/background.png")
# set background image location in the game's window
screen.blit(bg, (0, 0))

# load plan hero image
hero = pygame.image.load("./images/me1.png")
# plane hero image start location set
hero_rect = pygame.Rect(150, 300, 102, 126)
# create clock object
clock = pygame.time.Clock()


# creat enemy sprite
enemy = GameSprite("./images/enemy1.png")
enemy1 = GameSprite("./images/enemy1.png", 2)

# creat enemy sprite group
enemy_group = pygame.sprite.Group(enemy, enemy1)

# game's loop for game don't stop
while True:
    # set update speed for image
    clock.tick(60)

    # listen quit game's event
    for event in pygame.event.get():
        # judge quit event
        if event.type == pygame.QUIT:
            print("Exit system ...")
            pygame.quit()
            exit()
    # plane location update
    hero_rect.y -= 1
    # check hero touch game's window broad (top)
    if hero_rect.bottom == 0:
        # return window down
        hero_rect.y = 700
    # update game's background
    screen.blit(bg, (0, 0))
    screen.blit(hero, hero_rect)

    # 让精灵组调用两方法
    # update: 让组中的的所有精灵更新位置
    enemy_group.update()
    # draw： 在screen上绘制所有的精灵
    enemy_group.draw(screen)

    pygame.display.update()


