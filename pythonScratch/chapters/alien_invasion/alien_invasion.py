import pygame
import sys
from time import sleep
from setting import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats


class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        # 将配置项抽出来，创建单独的文件
        self.settings = Settings()
        # 创建一个显示窗口
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        # 创建一个飞船
        self.ship = Ship(self)
        # 创建一个编组(group)，用于存储所有有效的子弹，以便管理发射出去的所有子弹
        self.bullets = pygame.sprite.Group()
        # 创建一个编组(group)，用于存储外星人
        self.aliens = pygame.sprite.Group()
        self._create_fleet()
        # 创建一个用于存储游戏统计信息的实例​​
        self.stats = GameStats(self)
        # 游戏启动后置于活动状态
        self.game_active = True

    def run_game(self):
        while True:
            # 检测按键事件
            self._check_event()
            if self.game_active:
                # 更新飞船位置
                self.ship.update()
                # 更新子弹位置
                self.bullets.update()
                # 移除消失的子弹
                self._update_bullets()
                # 更新外星人的位置
                self._update_alien()
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
        self._check_alien_bullets_collisions

    def _check_alien_bullets_collisions(self):
        """检查是否有子弹击中了外星人​​,如果是，就删除相应的子弹和外星人​​"""
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)
        # 删除现有的子弹并创建一个新的外星舰队​​
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()

    def _create_fleet(self):
        """创建外星人舰队"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        current_x, current_y = alien_width, alien_height
        # 每创建一行外星人运行一次。
        # 每添加一行外星人后，都重置current_x的值，确保下一行的第一个外星人与前面各行的第一个外星人对齐。
        # 然后，将current_y的值加上外星人高度的两倍，确保下一行外星人离屏幕下边缘更近。
        while current_y < (self.settings.screen_height - 3*alien_height):
            while current_x < (self.settings.screen_width - 2*alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2*alien_width
            current_x = alien_width
            current_y += 2*alien_height

    def _create_alien(self, x_position, y_position):
        """创建一个外星人，并将其加入舰队"""
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    def _update_alien(self):
        """更新外星人的位置"""
        self._check_fleet_edges()
        self.aliens.update()
        # 外星人和飞船之间的碰撞​​
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        # 检查是否有外星人到达了屏幕的下边缘​​
        self._check_aliens_bottom()

    def _check_fleet_edges(self):
        """有外星人到达边缘时采取相应的措施"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """将整个外星舰队向下移动，并改变它们的方向"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction*-1

    def _ship_hit(self):
        """响应飞船和外星人的碰撞"""
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1
            # 晴空外星人和子弹
            self.bullets.empty()
            self.aliens.empty()
            # 创建一个新的外星人舰队， 并将飞船放置在屏幕底部
            self._create_fleet()
            self.ship.center_ship()

            # 暂定0.5秒
            sleep(0.5)
        else:
            self.game_active = False

    def _check_aliens_bottom(self):
        """检测是否有外星人到达屏幕底部"""
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                self._ship_hit()
                break

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
