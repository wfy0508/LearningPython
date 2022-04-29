import pygame

from plane_sprite import *

# 定义屏幕大小的常量
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
# 刷新的帧率
FREQUENCY = 60


class PlaneGame(object):
    def __init__(self):
        print("游戏初始化。。。")

        # 1. 创建游戏的窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        # 2. 创建游戏的时钟
        self.clock = pygame.time.Clock()
        # 3. 调用似有方法，创建精灵和精灵族
        self.__create_sprite()

    def __create_sprite(self):
        # 创建背景精灵和精灵组
        bg1 = Background("../images/background.png")
        bg2 = Background("../images/background.png")
        # 使两张相同的图片上下叠放在一起，循环滚动
        bg2.rect.y = -bg2.rect.height
        self.back_group = pygame.sprite.Group(bg1, bg2)

    def start_game(self):
        print("游戏开始。。。")
        while True:
            # 1 设置刷新频率
            self.clock.tick(FREQUENCY)
            # 2 事件监听 __event_handler
            self.__event_handler()
            # 3 碰撞检测 __crash_check
            self.__crash_check()
            # 4 更新/绘制精灵族 __update_sprite
            self.__update_sprite()
            # 5 更新显示 __update_display
            pygame.display.update()

    def __event_handler(self):
        for event in pygame.event.get():
            # 判断游戏是否退出
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()

    def __crash_check(self):
        pass

    def __update_sprite(self):
        self.back_group.update()
        self.back_group.draw(self.screen)

    @staticmethod
    def __game_over():
        pygame.quit()
        exit(0)


if __name__ == '__main__':
    game = PlaneGame()
    game.start_game()
