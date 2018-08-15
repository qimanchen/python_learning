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

        self.speed = random.randint(1, 3)

        self.rect.bottom = 0

        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0, max_x)

    def __del__(self):
        # print("自毁")
        pass

    def update(self):
        super().update()
        if self.rect.y >= SCREEN_RECT.height:
            self.kill()


class Hero(GameSprite):
    """hero"""

    def __init__(self):

        super().__init__("./images/me1.png", 0)

        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120
