#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import pygame
import sys

# 初始化pygame
pygame.init()
# pygame.display.list_modes() --> 显示当前显示器支持的屏幕分辨率
# 获得的是一个list

size = width, height = 600, 420
speed = [-2, 1]

# origin speed
or_speed = 1

bg = (255, 255, 255)  # 填充背景rgb

bg_figure = pygame.image.load("../fish_file/81/background.jpg")

clock = pygame.time.Clock()

# 创建指定窗口大小 Surface
# Surface 对象 -- 图像
# 每一次呈现出来的是一个图像
screen = pygame.display.set_mode(size, pygame.RESIZABLE)

# 设置窗口标题
pygame.display.set_caption("初次见面，请大家多多关照!")

# 设置放大缩小的比率：
ratio = 1.0

# 设置屏幕放大比率
screen_ratio = (1.0, 1.0)

# 加载图片 jpg png gif (支持多动图像格式）
oturtle = pygame.image.load("../fish_file/78/turtle.png")

turtle = oturtle.copy()

# 获取图像的位置矩形
oturtle_rect = oturtle.get_rect()
# 防止图像两个数据相同
position = turtle_rect = oturtle_rect.copy()

# 图像翻转
l_head = turtle
r_head = pygame.transform.flip(turtle, True, False)
fullscreen = False


def window_limit(position):
    if position.right > size[0]:
        position.right = size[0]
    if position.left < 0:
        position.left = 0
    if position.bottom > size[1]:
        position.bottom = size[1]
    if position.top < 0:
        position.top = 0
    return position


# 游戏循环
while True:
    # 监听退出事件的发生
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        # 监测键盘位置移动
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_KP_PLUS:
                or_speed += 1
                if or_speed > 10:
                    or_speed = 10
                for i in range(len(speed)):
                    if speed[i] == 0:
                        speed[i] = speed[i]
                    else:
                        speed[i] = speed[i] / abs(speed[i])

                speed = [spe * or_speed for spe in speed]
            if event.key == pygame.K_KP_MINUS:
                or_speed -= 1
                if or_speed < 0:
                    or_speed = 1
                # 列表表达式不适合这一功能
                for i in range(len(speed)):
                    if speed[i] == 0:
                        speed[i] = speed[i]
                    else:
                        speed[i] = speed[i] / abs(speed[i])
                speed = [spe * or_speed for spe in speed]
            if event.key == pygame.K_LEFT:
                turtle = l_head
                speed = [-1, 0]
            if event.key == pygame.K_RIGHT:
                turtle = r_head
                speed = [1, 0]
            if event.key == pygame.K_UP:
                speed = [0, -1]
            if event.key == pygame.K_DOWN:
                speed = [0, 1]

            # 全屏 （A)
            if event.key == pygame.K_a:
                fullscreen = not fullscreen
                if fullscreen:
                    # 获取最大的屏幕的分辨率
                    # print(pygame.display.list_modes()[0])
                    screen_ratio = [pygame.display.list_modes()[0][0]/size[0],
                                    pygame.display.list_modes()[0][1]/size[1]]
                    # 处理小乌龟随屏幕的大小而改变
                    # TODO 屏幕放大是不能很好的全屏
                    turtle_rect.width = oturtle_rect.width * screen_ratio[0]
                    turtle_rect.height = oturtle_rect.height * screen_ratio[1]
                    turtle = pygame.transform.smoothscale(oturtle, (int(turtle_rect.width),
                                                                    int(turtle_rect.height)))

                    l_head = turtle
                    r_head = pygame.transform.flip(turtle, True, False)
                    position.width = turtle_rect.width
                    position.height = turtle_rect.height
                    position = window_limit(position)

                    size = pygame.display.list_modes()[0]
                    screen = pygame.display.set_mode(size, pygame.FULLSCREEN | pygame.HWSURFACE)
                else:
                    size = width, height
                    turtle = pygame.transform.smoothscale(oturtle, (int(oturtle_rect.width * 1.0),
                                                                    int(oturtle_rect.height * 1.0)))
                    # 更新屏幕大小变化后的position及小乌龟图像大小
                    l_head = turtle
                    r_head = pygame.transform.flip(turtle, True, False)
                    position.width = oturtle_rect.width
                    position.height = oturtle_rect.height
                    position = window_limit(position)
                    print(position)

                    screen = pygame.display.set_mode(size)
                # 更新窗口变化后的position
                # l_head = turtle
                # r_head = turtle
                # position.width = turtle_rect.width
                # position.height = turtle_rect.height
                # position = window_limit(position)

            # 放大缩小turtle（-,=), 空格恢复
            if event.key == pygame.K_EQUALS or event.key == pygame.K_MINUS or event.key == pygame.K_SPACE:
                # 最大只能放大一倍，缩小50%
                if event.key == pygame.K_EQUALS and ratio < 2:
                    ratio += 0.1
                if event.key == pygame.K_MINUS and ratio > 0.5:
                    ratio -= 0.1
                if event.key == pygame.K_SPACE:
                    ratio = 1.0

                # 放大操作
                # 图像像素数据改变
                turtle_rect.width = oturtle_rect.width*ratio
                turtle_rect.height = oturtle_rect.height*ratio
                turtle = pygame.transform.smoothscale(oturtle, (int(oturtle_rect.width * ratio),
                                                                int(oturtle_rect.height * ratio)))
                l_head = turtle
                r_head = pygame.transform.flip(turtle, True, False)
                position.width = turtle_rect.width
                position.height = turtle_rect.height
                # 防止窗口变化使得小乌龟行动异常
                position = window_limit(position)
                # 打印图片大小变化
                # print(turtle_rect)

        # 用户调整窗口尺寸
        if event.type == pygame.VIDEORESIZE:
            size = event.size
            # width, height = size
            screen = pygame.display.set_mode(size, pygame.RESIZABLE)
            # 解决屏幕缩小后又放大的问题
            # print(position)
            # 随着窗口大小调整，图像位置的调整
            position = window_limit(position)

    # 移动图像
    # speed(水平，y)
    position = position.move(speed)

    # 监测边界
    # 左上角为零
    if position.left < 0 or position.right > size[0]:
        # 翻转图像
        # （figure, 水平翻转， 垂直翻转）
        # flip -- 上下， 左右翻转
        # scale -- 缩放图像（快速）
        # rotate -- 旋转图像
        # rotozoom -- 缩放并旋转
        # scale2x -- 快速放大一倍图像
        # smoothscale -- 平滑缩放图像（精准）
        # chop -- 裁剪图像
        turtle = pygame.transform.flip(turtle, True, False)

        # 反向移动
        speed[0] = -speed[0]

    if position.top < 0 or position.bottom > size[1]:
        speed[1] = -speed[1]

    # 填充背景图片
    # 填充背景
    # screen.fill(bg) bg --(255, 255, 255) RGB 颜色
    screen.blit(bg_figure, (0, 0))

    # 更新图像
    # 将背景的图像的改变图像素
    screen.blit(turtle, position)
    # 更新界面
    pygame.display.flip()
    # 延迟10ms
    # 如何控制游戏的运行速度 --- 帧率控制
    # 设置帧率
    clock.tick(50)
    pygame.display.update()
    # pygame.time.delay(10)
    # pygame效率 --- c语言的实现
