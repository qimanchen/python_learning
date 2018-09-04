#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import pygame
import sys
from pygame.locals import *


pygame.init()

size = width, height = 800, 600
bg = (255, 255, 255)

# set clock object
clock = pygame.time.Clock()

# draw game frame
screen = pygame.display.set_mode(size)

# add game frame title
pygame.display.set_caption("FishC Demo")

turtle = pygame.image.load("../fish_file/78/turtle.png")

# 0 -> No choose, 1 -> choosing, 2 -> finish choose
select = 0

# init a rect object
select_rect = pygame.Rect(0, 0, 0, 0)

# 0 -> No drag, 1 -> draging, 2 -> finish drag
drag = 0

position = turtle.get_rect()

# set turtle picture to frame center
position.center = width // 2, height // 2

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == MOUSEBUTTONDOWN:
            #
            if event.button == 1:
                # first click, choose area of cutting
                if select == 0 and drag == 0:
                    pos_start = event.pos
                    # print("pos_start: ", pos_start)
                    select = 1

                # second click, drag selected figure
                elif select == 2 and drag == 0:
                    # create new frame -- cut picture
                    capture = screen.subsurface(select_rect).copy()
                    cap_rect = capture.get_rect()
                    # print("cap_rect: ", cap_rect)
                    drag = 1

                # third click, init (delete select figure)
                elif select == 2 and drag == 2:
                    select = 0
                    drag = 0

        elif event.type == MOUSEBUTTONUP:
            if event.button == 1:
                # first release, over select
                if select == 1 and drag == 0:
                    pos_stop = event.pos
                    # print("pos_stop: ", pos_stop)
                    select = 2

                # second release, over drag
                if select == 2 and drag == 1:
                    drag = 2

    screen.fill(bg)
    screen.blit(turtle, position)

    # draw select rectangle real time
    if select:
        # get mouse real time position
        mouse_pos = pygame.mouse.get_pos()
        if select == 1:
            pos_stop = mouse_pos
            # print("pos_stop: ", pos_stop)

        # calculate select area rectangle
        select_rect.left, select_rect.top = pos_start
        select_rect.width, select_rect.height = pos_stop[0] - pos_start[0], pos_stop[1] - pos_start[1]

        # rect -- draw rectangle
        pygame.draw.rect(screen, (0, 0, 0), select_rect, 1)

    # drag cut figure
    if drag:
        if drag == 1:
            cap_rect.center = mouse_pos
            # print("cap_rect.center: ", cap_rect.center)
            # print("cap_rect: ", cap_rect)
        screen.blit(capture, cap_rect)

    # draw all pictures
    pygame.display.flip()

    # set clock
    clock.tick(30)



