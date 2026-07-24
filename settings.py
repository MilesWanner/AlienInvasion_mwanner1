"""
Program: Alien Invasion - Track 1 (Settings Module)
Author: Miles Wanner
Purpose: Store settings that control the game's screen, ship, bullets, and aliens.
Starter Code: Adapted from the Alien Invasion starter repository:
https://github.com/RedBeard41/alien_Invasion_starter
Date: July 2026
"""

class Settings:
    """Store settings for the Alien Invasion game."""
    def __init__(self) -> None:
        """Initialize screen, ship, bullet, alien, and lives settings."""
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

        self.fleet_drop_speed = 10

        self.speedup_scale = 1.1
        self.score_scale = 1.5

        self.ship_limit = 3

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed = 3.0
        self.alien_speed = 3.0
        self.bullet_speed = 5.0
        self.alien_points = 50

        self.fleet_direction = 1

    def increase_level(self):
        self.ship_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)