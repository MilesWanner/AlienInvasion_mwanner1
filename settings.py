class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 700
        self.resolution = (self.screen_width, self.screen_height)
        self.bg_color = (230, 230, 230)
        self.ship_speed = 3.0

        self.bullet_speed = 5.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 5

        self.alien_speed = 5.0
        self.fleet_drop_speed = 50
        self.fleet_direction = -1

        self.ship_limit = 3