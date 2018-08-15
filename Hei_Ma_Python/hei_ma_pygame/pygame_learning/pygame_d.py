# -*- coding: utf8 -*-

import pygame
import time
import os

"""
sudo pip3 install pygame
pygame:
python3 -m pygame.example.aliens --> 验证pygame是否被正常安装

导入素材

静止图像
图像重叠
静止图像
"""

# 游戏的初始化和退出
# pygame.init()  -- 导入并初始化所有pygame模块，使用其他模块之前，必须先调用init模块
# pygame.quit() -- 卸载所有pygame模块，在游戏结束之前使用

# 理解游戏中的坐标系
"""
原点： 左上角(0,0)

(0,0) --------------------(x)
|
|    Y
|        height(矩形区域)
|----x---
|      width
|
(y)

pygame.Rect(x,y,width,height) -> Rect 描述矩形区域
# 不用使用init方法也可直接执行
属性：
x,y,
size: -- 会返回一个元组(width,height)
width,height
"""

# 创建游戏主窗口
"""
display module实现
pygame.display.set_mode() 初始化游戏显示窗口
pygame.display.update() 刷新屏幕内容显示，稍后显示

set_mode():
set_mode(resolution=(0,0), flags=0, depth=0) -> surface
返回游戏窗口  -- 后续的图像都要绘制在其中
resolution --> 指定屏幕的宽高
flags --> 屏幕附加选项， 全屏，默认不需要传递
depth --> 表示颜色的位数，默认自动匹配
"""

# 简单的游戏
"""
图像文件：
1. 文件内容保存在内存中，加载到内存中
看到某个图像的内容:
1. pygame.image.load(file_path) 加载图像的数据
2. 使用游戏屏幕对象，调用blit方法指定到指定位置
pygame.Surface.blit(图像，位置)
3. 调用pygame.dispaly.update() 更新整个屏幕
要看到绘制结果，一定要使用它更新

透明图像：
显示图像时，不会再没事实际像素的地方遮挡

dispaly.update():
可以在screen对象完成所有的blit方法后，统一一次display.update()  -- 显示最终的结果
screen 油画的画布 -- blit 绘制很多图像 -- 虚拟绘制
display.update() 最终显示

游戏中的动画原理：
静止图片的连续快速播放
一般电脑每秒绘制60次， -- 达到比较好的动画品质
每次 -- Frame 帧 -- 对应update一次
"""

# pygame.init()
#
# # 编写游戏代码
# print("游戏代码")
#
# pygame.quit()

# hero_rect = pygame.Rect(100, 500, 120,125)
#
# print(hero_rect.x,hero_rect.y)
# print(hero_rect.width, hero_rect.height)
# print(hero_rect.size)

pygame.init()

# 游戏的初始化
# 创建游戏的窗口
screen = pygame.display.set_mode((480, 700))

# 绘制背景图像
# os.chdir('C:\\Users\\acer\\Desktop\\git_learning\\python_learning\\Hei_Ma_Python\\hei_ma_pygame')
# 加载图像
bg = pygame.image.load("../images/background.png")
# 文件使用./ 当前执行程序所在目录
# 绘制
screen.blit(bg, (0, 0))
# 位置，指定从左开始

# 载入英雄
hero = pygame.image.load("../images/me1.png")
# screen.blit(hero, (100, 200))
# # pygame.display.update()

# 游戏循环 -〉意味着游戏的开始
# 保证游戏不会退出
"""
游戏初始化：
    设置游戏窗口
    绘制图像初始绘制
    设置游戏时钟
游戏循环：
    设置刷新帧率
    检测用户交互
    更新所有图像的位置
    更新屏幕显示
    
游戏时钟：
变化图像位置 -- 动画效果
pygame.time.Clock
    游戏初始化 -- 创建一个时钟对象
    在游戏循环中，时钟对象调用tick(帧率)方法
    
每一update，每一次要把所有的图像都重新绘制一遍
"""
# 创建时钟对象
clock = pygame.time.Clock()

# 定义rect记录飞机的初始位置
hero_rect = pygame.Rect(150, 300, 102,126)
# 修改飞机位置
# 调用blit绘制图像
# 位置可以传入Rect的返回
# 调用update更新显示

"""
游戏循环中检听事件：
用户对游戏作的操作 -- 时间
监听：判断用户的具体操作，捕获用户的操作

代码：
pygame.event.get()  -- 可以获取当前所做动作的事件列表


精灵和精灵组：
pygame.sprite.Sprite -- 存储图像数据，位置rect的对象
pygame.sprite.Group

不同的游戏角色不同的子类
update()方法

精灵组：
__init__() 加入多个精灵
add()
sprites（） 返回所有精灵列表
update(*args) 精灵各自调用各自的update方法
draw(Surface) 把所有的image绘制到Surface的rect位置上

需要使用pygame.dispaly.update()

"""
while True:
    # 指定循环体内部的代码执行的频率
    clock.tick(120)  # 每秒钟执行六十次
    # event_list = pygame.event.get()  # 捕获事件

    # 监听事件
    for event in pygame.event.get():
        # 判断时间类型是否退出事件
        if event.type == pygame.QUIT:
            print("退出系统...")

            pygame.quit()

            # 退出系统
            exit()  # 直接退出当前程序
    hero_rect.y -= 1
    # 判断飞机的位置
    # Rect 属性 bottom = y + height
    if hero_rect.y + hero_rect.height == 0:
        hero_rect.y = 700
    screen.blit(bg, (0, 0))  # 防止图像重叠
    screen.blit(hero, hero_rect)

    pygame.display.update()

pygame.quit()

