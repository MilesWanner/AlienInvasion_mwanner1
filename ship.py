"""
Program: Alien Invasion - Track 1 (Ship Module)
Author: Miles Wanner
Purpose: Define the player's ship, load its image, and manage vertical movement.
Starter Code: Adapted from the Alien Invasion starter repository:
https://github.com/RedBeard41/alien_Invasion_starter
Date: July 2026
"""

from pathlib import Path

import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    """Represent and manage the player-controlled ship."""

    def __init__(self, ai_game: "AlienInvasion") -> None:
        """Initialize the ship along the left edge of the screen."""
        super().__init__()

        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings

        image_path = (
            Path(__file__).parent
            / "images"
            / "ship.bmp"
        )

        original_image = pygame.image.load(image_path)
        self.image = pygame.transform.rotate(
            original_image,
            -90,
        )

        self.rect = self.image.get_rect()
        self.rect.midleft = self.screen_rect.midleft

        self.moving_up = False
        self.moving_down = False

    def update(self) -> None:
        """Update the ship's vertical position within the screen."""
        if self.moving_up and self.rect.top > 0:
            self.rect.y -= self.settings.ship_speed

        if (
            self.moving_down
            and self.rect.bottom < self.screen_rect.bottom
        ):
            self.rect.y += self.settings.ship_speed

    def blitme(self) -> None:
        """Draw the ship at its current position."""
        self.screen.blit(self.image, self.rect)

    def center_ship(self) -> None:
        """Return the ship to the center of the left edge."""
        self.rect.midleft = self.screen_rect.midleft