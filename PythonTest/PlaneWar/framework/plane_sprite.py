import pygame

# 定义屏幕大小的常量
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
# 刷新的帧率
FREQUENCY = 60


class GameSprite(pygame.sprite.Sprite):
    """飞机大战游戏精灵"""

    def __init__(self, image_name, speed=1):
        # 调用父类的初始化方法<当定义的类不是继承object时，首先要调用父类的初始化方法>
        super().__init__()

        # 定义对象的属性
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        # 默认让飞机在垂直向上移动
        self.rect.y += self.speed


class Background(GameSprite):
    def update(self):
        # 调用父类的实现方法
        super().update()
        # 判断图像是否移出屏幕，移出则将图像设置到屏幕的上方
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height
