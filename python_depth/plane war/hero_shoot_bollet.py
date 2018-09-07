#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import time
import sys
import pygame
# import all event type
from pygame.locals import *


# create hero object
class HeroPlane(object):

    def __init__(self, screen_temp):
        self.x = 210
        self.y = 700
        self.image = pygame.image.load("feiji/hero1.png")
        self.image2 = pygame.image.load("feiji/hero2.png")
        self.screen = screen_temp
        self.bullet_list = []  # save bullet object

    def plane_dynamic_display(self, switch_hero):

        if switch_hero:
            self.screen.blit(self.image2, (self.x, self.y))
            switch_hero = False
        else:
            self.screen.blit(self.image, (self.x, self.y))

        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()
        return switch_hero

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()

    def move_left(self):
        self.x -= 5

    def move_right(self):
        self.x += 5

    def fire(self):
        self.bullet_list.append(Bullet(self.screen, self.x, self.y))


class Bullet(object):

    def __init__(self, screen_temp, x, y):
        self.x = x + 40
        self.y = y - 20
        self.image = pygame.image.load("feiji/bullet.png")
        self.screen = screen_temp

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

    def move(self):
        self.y -= 3


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
                hero.fire()


def main():

    # load all pygame modules
    pygame.init()
    # create a window for show contents
    screen = pygame.display.set_mode((480, 852), 0, 32)
    # load background figure
    background = pygame.image.load("feiji/background.png")
    # load hero figure
    hero = HeroPlane(screen)

    # set renew frame rate
    clock = pygame.time.Clock()

    switch_plane = False
    switch_count = 1

    # show background figure in window
    while True:

        # set background picture place position in window
        screen.blit(background, (0, 0))
        # draw hero to screen
        if switch_count % 3 == 0:
            switch_plane = True

        switch_count += 1
        if switch_count == 60:
            switch_count = 1

        switch_plane = hero.plane_dynamic_display(switch_plane)
        # update show contents(figure) to window
        pygame.display.update()

        key_control(hero)

        clock.tick(60)


if __name__ == '__main__':
    main()
