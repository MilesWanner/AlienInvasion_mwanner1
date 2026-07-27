"""
Program: Alien Invasion - Track 1 (Button Module)
Author: Miles Wanner
Purpose: Define a button, prepare its message, and draw it to the screen.
Starter Code: Adapted from the Alien Invasion starter repository:
https://github.com/RedBeard41/alien_Invasion_starter
Date: July 2026
"""

import pygame.font


class Button:
    """Build and display buttons for the game."""

    def __init__(self, ai_game: "AlienInvasion", msg: str) -> None:
        """Initialize the button's dimensions, colors, font, and message."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        self.width, self.height = 200, 50
        self.button_color = (0, 135, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        self._prep_msg(msg)

    def _prep_msg(self, msg: str) -> None:
        """Render the button message and center it on the button."""
        self.msg_image = self.font.render(
            msg,
            True,
            self.text_color,
            self.button_color,
        )
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self) -> None:
        """Draw the button and its message."""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)