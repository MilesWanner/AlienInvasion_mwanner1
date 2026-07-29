"""
Program: Alien Invasion - Track 1 (Game Stats Module)
Author: Miles Wanner
Purpose: Store and reset the statistics that change during gameplay.
Starter Code: Adapted from the Alien Invasion starter repository:
https://github.com/RedBeard41/alien_Invasion_starter
Date: July 2026
"""

class GameStats:
    """Track statistics that change during the game."""
    def __init__(self, ai_game: "AlienInvasion") -> None:
        """Store the game settings and initialize game statistics."""
        self.settings = ai_game.settings
        self.high_score = 0
        self.reset_stats()

    def reset_stats(self) -> None:
        """Reset the number of remaining ships to the configured limit."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1