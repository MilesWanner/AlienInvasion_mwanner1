"""
Program: Alien Invasion - Track 1 (Alien Module)
Author: Miles Wanner
Purpose: Define the alien class, load the image, and manage its movement. 
Starter Code: Adapted from the Alien Invasion starter repository:
https://github.com/RedBeard41/alien_Invasion_starter
Date: July 2026
"""

import pygame
from pygame.sprite import Sprite
from pathlib import Path

class Alien(Sprite):
    """Represents a single alien in the fleet."""
    def __init__(self, ai_game):
        """Initialize the alien, load its image, and set its starting position."""
        super().__init__()

        self.screen = ai_game.screen
        image_path = Path(__file__).parent / "images" / "alien.bmp"
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.settings = ai_game.settings

    def update(self):
        """Update the alien's horizontal position based on the fleet direction."""
        self.rect.x += self.settings.alien_speed * self.settings.fleet_direction

    def check_edges(self):
        """Return True if the alien has reached a screen edge."""
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)

