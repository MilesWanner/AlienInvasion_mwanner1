"""
Program: Alien Invasion - Track 1 (Game Stats Module)
Author: Miles Wanner
Purpose: Store and reset statistics that change during gameplay.
Starter Code: Adapted from the Alien Invasion starter repository:
https://github.com/RedBeard41/alien_Invasion_starter
Date: July 2026
"""


class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game: "AlienInvasion") -> None:
        """Initialize the game statistics."""
        self.settings = ai_game.settings

        self.high_score = 0

        self.reset_stats()

    def reset_stats(self) -> None:
        """Reset statistics that change when a new game begins."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1