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

    # show background figure in window
    while True:

        # set background picture place position in window
        screen.blit(background, (0, 0))

        # update show contents(figure) to window
        pygame.display.update()

        # set event listener
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()


if __name__ == '__main__':
    main()
