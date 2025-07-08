class Settings:
    def __init__(self) -> None:
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed = 1.5
        # 设置子弹的大小和颜色
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_speed = 2.0
        self.bullet_allowed = 10
        # 设置外星人的移动速度
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # 1:向右移动, -1:向左移动
        self.fleet_direction=1
        # 限制飞船数量
        self.ship_limit=3