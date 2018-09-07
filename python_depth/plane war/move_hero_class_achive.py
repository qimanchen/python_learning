#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import pygame

# import all event type
from pygame.locals import *
import sys


# create hero object
class HeroPlane(object):

    def __init__(self, screen_temp):
        self.x = 210
        self.y = 700
        self.image = pygame.image.load("feiji/hero1.png")
        self.screen = screen_temp

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

    def move_left(self):
        self.x -= 5

    def move_right(self):
        self.x += 5


def key_control(hero):
    # set event listener
    for event in pygame.event.get():

        # check quit event
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        # check key down ?
        if event.type == KEYDOWN:
            # press a or left?
            if event.key == K_a or event.key == K_LEFT:
                hero.move_left()
            # press d or right?
            if event.key == K_d or event.key == K_RIGHT:
                hero.move_right()
            # press space?
            if event.key == K_SPACE:
                pass


def main():

    # load all pygame modules
    pygame.init()

    # create a window for show contents
    screen = pygame.display.set_mode((480, 852), 0, 32)

    # load background figure
    background = pygame.image.load("feiji/background.png")

    # load hero figure
    hero = HeroPlane(screen)

    # show background figure in window
    while True:

        # set background picture place position in window
        screen.blit(background, (0, 0))
        # draw hero to screen
        hero.display()
        # update show contents(figure) to window
        pygame.display.update()

        key_control(hero)


if __name__ == '__main__':
    main()
