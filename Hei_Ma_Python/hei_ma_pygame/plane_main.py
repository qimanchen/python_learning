#!/usr/bin/env python3

import pygame
from Hei_Ma_Python.hei_ma_pygame.plane_sprites import *


class PlaneGame(object):
    """飞机大战主游戏"""

    def __init__(self):
        print("游戏初始化")
        # 1. 创建游戏的窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)  # 不要把固定数值锁死
        # 2. 创建游戏时钟
        self.clock = pygame.time.Clock()
        # 3. 调用私有方法，精灵和精灵组的创建
        self.__create_sprites()
        # 4. 设置定时器事件
        # set_timer(eventid, milliseconds) -> None
        # eventid 可以通过pygame.USEREVENT 指定每增加一个则增加1
        # ms为set_timer的时间单位
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)
        # 设置子弹时钟
        pygame.time.set_timer(HERO_FIRE_EVENT, 500)

    def __create_sprites(self):

        # 创建背景精灵和精灵组
        bg1 = Background()
        bg2 = Background(True)

        self.back_group = pygame.sprite.Group(bg1, bg2)

        # 创建敌机精灵组
        self.enemy_group = pygame.sprite.Group()

        # 创建英雄精灵
        # 方便其他模块可以调用它
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

    def start_game(self):
        print("游戏开始...")
        while True:
            # 设置刷新帧率
            self.clock.tick(FRAME_PER_SEC)
            # 事件监听
            self.__event_handler()
            # 碰撞检测
            self.__check_collide()

            # 更新/绘制精灵
            self.__update_sprites()
            # 更新显示
            pygame.display.update()

    def __event_handler(self):

        for event in pygame.event.get():

            # 判断是否退出程序
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
            # 监测敌机创建事件实现
            elif event.type == CREATE_ENEMY_EVENT:
                enemy = Enemy()
                self.enemy_group.add(enemy)
            # elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            #     print("向右移动")
            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()
        # 使用键盘提供的方法 --> 可以动态的移动英雄飞机
        keys_pressed = pygame.key.get_pressed()
        # 判断元组中对应按键的索引
        if (keys_pressed[pygame.K_RIGHT]
                or keys_pressed[pygame.K_LEFT]
                or keys_pressed[pygame.K_UP]
                or keys_pressed[pygame.K_DOWN]):
            if keys_pressed[pygame.K_RIGHT]:
                self.hero.speed = 2
            elif keys_pressed[pygame.K_LEFT]:
                self.hero.speed = -2
            elif keys_pressed[pygame.K_UP]:
                self.hero.up_stats = True
                self.hero.speed_d = -2
            elif keys_pressed[pygame.K_DOWN]:
                self.hero.up_stats = True
                self.hero.speed_d = 2
            else:
                self.hero.speed = 0
                self.hero.speed_d = 0
                self.hero.up_stats = False
                self.hero.co_key = False
        else:
            if keys_pressed[pygame.K_RIGHT] and keys_pressed[pygame.K_UP]:
                self.hero.speed = 2
                self.hero.up_stats = True
                self.hero.speed_d = -2
            elif keys_pressed[pygame.K_LEFT] and keys_pressed[pygame.K_DOWN]:
                self.hero.speed = -2
                self.hero.up_stats = True
                self.hero.speed_d = 2
            elif keys_pressed[pygame.K_RIGHT] and keys_pressed[pygame.K_DOWN]:
                self.hero.speed = 2
                self.hero.up_stats = True
                self.hero.speed_d = 2
            elif keys_pressed[pygame.K_LEFT] and keys_pressed[pygame.K_UP]:
                self.hero.speed = -2
                self.hero.up_stats = True
                self.hero.speed_d = -2
            else:
                self.hero.speed = 0
                self.hero.speed_d = 0
                self.hero.up_stats = False
                self.hero.co_key = False

    def __check_collide(self):

        # pygame.sprite.groupcollide(group1, group2,kill,kill,collide) --> sprite_list
        # 两个精灵组中的精灵会被自动删除
        pygame.sprite.groupcollide(self.hero.bullets, self.enemy_group,
                                   True, True)
        # pygame.sprite.spritecollide(sprite, group, dokill, collided=None) --> sprite_list
        # 设置为True -- > 敌机会烧毁
        enemier = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)
        # 碰撞以后才会有内容
        # 判断列表是否有内容
        if len(enemier) > 0:
            # 让英雄牺牲
            self.hero.kill()
            # 结束游戏
            PlaneGame.__game_over()

    def __update_sprites(self):

        # 更新背景
        self.back_group.update()
        self.back_group.draw(self.screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

        self.hero_group.update()
        self.hero_group.draw(self.screen)

        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)

    @staticmethod
    def __game_over():
        print("游戏结束")

        pygame.quit()
        exit()


if __name__ == '__main__':

    # 创建游戏对象
    game = PlaneGame()
    # 启动游戏
    game.start_game()
