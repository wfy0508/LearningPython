import pygame
from plane_sprite import *

pygame.init()

# 绘制游戏窗口
window = pygame.display.set_mode((480, 700))
# 绘制背景图像
# 首先加载背景图像文件
bg = pygame.image.load("../images/background.png")
# 设置图像在窗口中的位置
window.blit(bg, (0, 0))

# 绘制飞机图像
plane = pygame.image.load("../images/me1.png")
# 将飞机放置在图像(200, 500)的位置
window.blit(plane, (200, 350))

# 创建游戏时钟对象
clock = pygame.time.Clock()

# 创建一个飞机图像的初始位置
plane_position = pygame.Rect(200, 350, 102, 126)

# 创建精灵对象
enemy = GameSprite("./images/enemy1.png")
enemy1 = GameSprite("./images/enemy1.png", speed=2)
# 创建一个精灵组
enemy_group = pygame.sprite.Group(enemy, enemy1)

while True:
    # 可以执行游戏体内执行的频率
    clock.tick(60)
    # 捕获事件，当用户点击退出按钮时，程序退出
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("游戏退出...")
            pygame.quit()
            exit(1)

    # 让飞机向上移动
    plane_position.y -= 1
    # 判断飞机的位置，如果小于0，就重置飞机的位置
    # if plane_rect.y <= 0:
    #     plane_rect.y = 700
    # 优化版本：如果飞机完全飞出屏幕就将飞机置于屏幕底部
    if plane_position.y + plane_position.h <= 0:
        plane_position.y = 700 - plane_position.h
    # 重新绘制背景图像
    window.blit(bg, (0, 0))
    window.blit(plane, plane_position)

    # 让精灵族调用两个方法
    # update
    enemy_group.update()
    # draw
    enemy_group.draw(window)

    # 更新屏幕显示
    pygame.display.update()
