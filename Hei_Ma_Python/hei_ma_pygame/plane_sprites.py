"""
官方
第三方
自定义
"""
import random
import pygame

# 屏幕大小的常量
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
# 刷新帧率
FRAME_PER_SEC = 60
# 敌机定时器常量
CREATE_ENEMY_EVENT = pygame.USEREVENT
# 英雄发射子弹时间
HERO_FIRE_EVENT = pygame.USEREVENT + 1

DELAY = 100
SWITCH_HERO = True


class GameSprite(pygame.sprite.Sprite):
    """
        palne sprite class
    """
    """
    image 的 get_rect()方法，返回 pygame.Rect(0,0,width,height)的对象
    """
    def __init__(self, image_name, speed=1):
        super().__init__()

        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed
    # update self.rect.y += self.speed

    def update(self):

        # 在屏幕的垂直方向上移动
        self.rect.y += self.speed


class Background(GameSprite):
    """游戏背景精灵"""

    def __init__(self, is_alt=False):
        # super 中__init__的参数是父类的参数
        super().__init__("./images/background.png")
        # 判断是否是交替图像
        if is_alt:
            self.rect.y = -self.rect.height

    def update(self):
        # 1. 调用父类方法的实现
        super().update()
        # 判断是否移出屏幕
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height


class Enemy(GameSprite):
    """敌机精灵"""
    def __init__(self):
        # 确定敌机图片
        super().__init__("./images/enemy1.png")
        # 设置敌机移动速度
        self.speed = random.randint(1, 3)
        # 设置敌机从屏幕的顶部（0，0）出现
        self.rect.bottom = 0
        # 设置敌机左右随机出现
        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0, max_x)

    # 监测敌机对象被销毁时的动作
    def __del__(self):
        # print("自毁")
        pass

    def update(self):
        # 调用父类的方法
        super().update()
        # 敌机飞出屏幕，从精灵组中删除精灵
        if self.rect.y >= SCREEN_RECT.height:
            # kill方法可以直接把精灵删除
            self.kill()


class Hero(GameSprite):
    """hero"""

    def __init__(self, up_stats=False, co_key=False, speed_d=0):

        super().__init__("./images/me1.png", 0)
        self.switch_hero = pygame.image.load("./images/me2.png")
        # 设置英雄飞机的初始位置
        self.rect.centerx = SCREEN_RECT.centerx
        # 在屏幕底部的上方120
        self.rect.bottom = SCREEN_RECT.bottom - 120
        self.up_stats = up_stats
        self.co_key = co_key
        self.speed_d = speed_d

        # 创建子弹精灵组
        self.bullets = pygame.sprite.Group()

    def update(self):
        # 不需要调用父类的方法
        # 更新hero
        global SWITCH_HERO
        global DELAY
        # SWITCH_HERO = not SWITCH_HERO
        if SWITCH_HERO:
            self.image, self.switch_hero = self.switch_hero, self.image
        # 更新hero的刷新帧率
        if not(DELAY % 4):
            SWITCH_HERO = not SWITCH_HERO
        DELAY -= 1
        if not DELAY:
            DELAY = 100

        if self.co_key:
            if self.up_stats:
                self.rect.y += self.speed_d
            else:
                self.rect.x += self.speed
        else:
            self.rect.y += self.speed_d
            self.rect.x += self.speed
        # 英雄在水平方向移动
        # right -- max_x = SCREEN_RECT.width - self.rect.width
        # bottom -- max_y = SCREEN_RECT.height - self.rect.height
        # right = x + width
        # left = x - width
        if self.rect.x <= 0:
            self.rect.x = 0
        elif self.rect.right >= SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right
        elif self.rect.y <= 0:
            self.rect.y = 0
        elif self.rect.bottom >= SCREEN_RECT.bottom:
            self.rect.bottom = SCREEN_RECT.bottom
        pass

    def move_hero(self):
        pass

    def fire(self):

        # 1. 创建子弹精灵
        for i in (0, 1, 2):
            bullet = Bullet()
            # 设置精灵位置
            bullet.rect.bottom = self.rect.y - 20*i
            bullet.rect.centerx = self.rect.centerx
            # 添加
            self.bullets.add(bullet)


class Bullet(GameSprite):
    """子弹精灵"""
    def __init__(self):
        super().__init__("./images/bullet1.png", -2)

    def update(self):
        super().update()
        # 判断子弹是否飞出屏幕
        if self.rect.bottom < 0:
            self.kill()

    def __del__(self):
        pass
        # print("子弹被销毁")
