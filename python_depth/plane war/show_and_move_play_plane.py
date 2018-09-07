#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import pygame

# import all event type
from pygame.locals import *
import sys


def main():

    # load all pygame modules
    pygame.init()

    # create a window for show contents
    screen = pygame.display.set_mode((480, 852), 0, 32)

    # load background figure
    background = pygame.image.load("feiji/background.png")

    # load hero figure
    hero = pygame.image.load("feiji/hero1.png")

    # set hero locals
    x = 210
    y = 700

    # show background figure in window
    while True:

        # set background picture place position in window
        screen.blit(background, (0, 0))

        # draw hero to screen
        screen.blit(hero, (x, y))

        # update show contents(figure) to window
        pygame.display.update()

        # set event listener
        for event in pygame.event.get():

            # check quit event
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            # check keydown
            if event.type == KEYDOWN:
                # press a or left?
                if event.key == K_a or event.key == K_LEFT:
                    x -= 1

                # press d or right?
                if event.key == K_d or event.key == K_RIGHT:
                    x += 1

                # press space?
                if event.key == K_SPACE:
                    pass


if __name__ == '__main__':
    main()
