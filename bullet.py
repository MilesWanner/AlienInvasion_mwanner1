"""
Program: Alien Invasion - Track 1 (Bullet Module)
Author: Miles Wanner
Purpose: Define the bullets, set their starting position, and manage their movement.
Starter Code: Adapted from the Alien Invasion starter repository:
https://github.com/RedBeard41/alien_Invasion_starter
Date: July 2026
"""

import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Represent a bullet fired by the player's ship."""
    def __init__(self, ai_game):
        """Initialize the bullet's size, color, and starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        self.rect = pygame.Rect(0, 
                                0,
                                self.settings.bullet_height,
                                self.settings.bullet_width)
        
        self.rect.midright = ai_game.ship.rect.midright

    def update(self):
        """Update the bullet's position to move horizontally across the screen."""
        self.rect.x += self.settings.bullet_speed

    def draw_bullet(self):
        """Draw the bullet at its current position."""
        pygame.draw.rect(self.screen, self.color, self.rect)