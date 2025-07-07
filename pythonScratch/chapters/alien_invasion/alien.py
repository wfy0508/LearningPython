import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, ai_game) -> None:
        super().__init__()
        self.screen = ai_game.screen
        # 加载外星人图像
        self.image = pygame.image.load("pythonScratch/chapters/alien_invasion/images/alien.bmp")
        # 加载外星人图像并设置其rect属性
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # 存储外星人的精确水平位置
        self.x = self.rect.x