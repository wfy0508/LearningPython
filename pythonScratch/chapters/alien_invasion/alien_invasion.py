import pygame
import sys
from setting import Settings
from ship import Ship


class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        # 将配置项抽出来，创建单独的文件
        self.settings = Settings()
        # 创建一个显示窗口
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_hight))
        pygame.display.set_caption("Alien Invasion")
        # 创建一个飞船
        self.ship = Ship(self)

    def run_game(self):
        while True:
            # 检测退出等事件
            self._check_event()
            # 检测按键
            self.ship.update()
            # 更新屏幕
            self._update_screen()
            # 设置屏幕刷新率
            self.clock.tick(60)

    def _check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                if event.key == pygame.K_LEFT:
                    self.ship.moving_left = False

    def _update_screen(self):
        # 填充屏幕背景色
        self.screen.fill(self.settings.bg_color)
        # 绘制飞船
        self.ship.blitme()
        # 在每次执行while循环时都绘制一个空屏幕，并擦去旧屏幕，使得只有新的空屏幕可见。
        pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
