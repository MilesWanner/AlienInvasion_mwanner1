"""
Program: Alien Invasion - Track 1 (Ship Module)
Author: Miles Wanner
Purpose: Define the player's ship, load the image, and manage its vertical movement.
Starter Code: Adapted from the Alien Invasion starter repository:
https://github.com/RedBeard41/alien_Invasion_starter
Date: July 2026
"""

import pygame
from pathlib import Path
from pygame.sprite import Sprite

class Ship(Sprite):
    """Represent and manage the player-controlled ship."""
    def __init__(self, ai_game: "AlienInvasion") -> None:
        """Initialize the ship and place it along the left edge of the screen."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings

        super().__init__()

        image_path = Path(__file__).parent / "images" / "ship.bmp"
        self.image = pygame.image.load(image_path)
        self.rotated_image = pygame.transform.rotate(self.image, -90)
        self.rect = self.rotated_image.get_rect()
        self.rect.midleft = self.screen_rect.midleft
        self.moving_up = False
        self.moving_down = False

    def update(self) -> None:
        """Update the ship's vertical position within the screen boundaries."""
        if self.moving_up and self.rect.top > 0:
            self.rect.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += self.settings.ship_speed

    def blitme(self) -> None:
        """Draw the ship at its current position."""
        self.screen.blit(self.rotated_image, self.rect)

    def center_ship(self) -> None:
        """Return the ship to its starting position on the left edge."""
        self.rect.midleft = self.screen_rect.midleft