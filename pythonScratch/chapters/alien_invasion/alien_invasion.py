import pygame
import sys
from setting import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien


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
        # 创建一个编组(group)，用于存储所有有效的子弹，以便管理发射出去的所有子弹
        self.bullets = pygame.sprite.Group()
        # 创建一个编组(group)，用于存储外星人
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

    def run_game(self):
        while True:
            # 检测按键事件
            self._check_event()
            # 更新飞船位置
            self.ship.update()
            # 更新子弹位置
            self.bullets.update()
            # 移除消失的子弹
            self._update_bullets()
            # 更新屏幕显示
            self._update_screen()
            # 设置屏幕刷新率
            self.clock.tick(60)

    def _check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                self.ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                self.ship.moving_left = True
            elif event.key == pygame.K_q:
                sys.exit()
            elif event.key == pygame.K_SPACE:
                self._fire_bullet()

    def _check_keyup_events(self, event):
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                self.ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                self.ship.moving_left = False

    def _fire_bullet(self):
        """创建新子弹并将其加入编组bullets"""
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """移除消失的子弹"""
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        # print(len(self.bullets))

    def _create_fleet(self):
        """创建外星人舰队"""
        alien = Alien(self)
        alien_width = alien.rect.width
        current_x = alien_width
        while current_x < (self.settings.screen_width - 2*alien_width):
            self._create_alien(current_x)
            current_x += 2*alien_width

    def _create_alien(self, x_position):
        """创建一个外星人，并将其加入舰队"""
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        self.aliens.add(new_alien)

    def _update_screen(self):
        # 填充屏幕背景色
        self.screen.fill(self.settings.bg_color)
        # 更新
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        # 绘制飞船
        self.ship.blitme()
        # 绘制外星人
        self.aliens.draw(self.screen)
        # 在每次执行while循环时都绘制一个空屏幕，并擦去旧屏幕，使得只有新的空屏幕可见。
        pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
