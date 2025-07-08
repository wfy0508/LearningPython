import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    def __init__(self, ai_game) -> None:
        super().__init__()
        self.screen = ai_game.screen
        # 加载外星人图像
        self.image = pygame.image.load(
            "pythonScratch/chapters/alien_invasion/images/alien.bmp")
        # 加载外星人图像并设置其rect属性
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # 存储外星人的精确水平位置
        self.x = self.rect.x
        self.settings = ai_game.settings

    def update(self):
        # 向右移动，x坐标不变
        self.x += self.settings.alien_speed*self.settings.fleet_direction
        self.rect.x = self.x

    def check_edges(self):
        """如果外星人位于屏幕边缘, 就返回True"""
        self_rect = self.screen.get_rect()
        return (self.rect.right >= self_rect.right) or (self.rect.left <= 0)
