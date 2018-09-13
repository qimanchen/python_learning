#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import time
import random
import sys
import pygame
# import all event type
from pygame.locals import *


# create hero object
class HeroPlane(object):

    def __init__(self, screen_temp):
        self.x = 210
        self.y = 700
        self.hero_key = [False, False, False, False]
        self.image = pygame.image.load("feiji/hero1.png")
        self.image2 = pygame.image.load("feiji/hero2.png")
        self.screen = screen_temp
        self.bullet_list = []  # save bullet object

    def plane_dynamic_display(self, switch_hero):

        remove_bullet = []

        if switch_hero:
            self.screen.blit(self.image2, (self.x, self.y))
            switch_hero = False
        else:
            self.screen.blit(self.image, (self.x, self.y))

        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()
            if bullet.judge():  # check bullet out board
                remove_bullet.append(bullet)
        for bullet in remove_bullet:
            self.bullet_list.remove(bullet)
        return switch_hero

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()

    def move_left(self):
        if self.hero_key[0]:
            self.x -= 5

    def move_right(self):
        if self.hero_key[1]:
            self.x += 5

    def fire(self):
        self.bullet_list.append(Bullet(self.screen, self.x, self.y))


class EnemyPlane(object):

    def __init__(self, screen_temp):
        self.x = 0
        self.y = 0
        self.speed = 5
        self.image = pygame.image.load("feiji/enemy0.png")
        # self.image2 = pygame.image.load("feiji/hero2.png")
        self.screen = screen_temp
        self.bullet_list = []  # save bullet object

    def display(self):

        remove_bullet = []
        self.screen.blit(self.image, (self.x, self.y))

        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()
            if bullet.judge():  # check bullet out board
                remove_bullet.append(bullet)
        for bullet in remove_bullet:
            self.bullet_list.remove(bullet)

    def move(self):
        self.x += self.speed
        if self.x > 480 - 51 or self.x < 0:
            self.speed = -self.speed
        self.y += 1

    def fire(self):
        random_num = random.randint(1, 100)
        if random_num == 8 or random_num == 28:
            self.bullet_list.append(EnemyBullet(self.screen, self.x, self.y))


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

    # check bullet deleted
    def __del__(self):
        pass

    def judge(self):
        if self.y < 0:
            return True
        return False


class EnemyBullet(object):

    def __init__(self, screen_temp, x, y):
        self.x = x + 25
        self.y = y + 40
        self.image = pygame.image.load("feiji/bullet1.png")
        self.screen = screen_temp

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

    def move(self):
        self.y += 5

    # check bullet deleted
    def __del__(self):
        pass

    def judge(self):
        if self.y > 852:
            return True
        return False


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
                hero.hero_key[0] = True
            # press d or right?
            if event.key == K_d or event.key == K_RIGHT:
                hero.hero_key[1] = True
            # press space?
            if event.key == K_SPACE:
                hero.fire()
        if event.type == KEYUP:
            # press a or left?
            if event.key == K_a or event.key == K_LEFT:
                hero.hero_key[0] = False
            # press d or right?
            if event.key == K_d or event.key == K_RIGHT:
                hero.hero_key[1] = False
            # # press space?
            # if event.key == K_SPACE:
            #     hero.fire()
    hero.move_right()
    hero.move_left()


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

    # create one enemy plane
    enemy = EnemyPlane(screen)

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
        # enemy
        enemy.display()
        enemy.move()
        enemy.fire()
        # update show contents(figure) to window
        pygame.display.update()

        key_control(hero)

        clock.tick(60)


if __name__ == '__main__':
    main()
