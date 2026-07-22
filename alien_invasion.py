"""
Program: Alien Invasion - Track 1 (Main Module)
Author: Miles Wanner
Purpose: Run the Alien Invasion game and manage events, objects, collisions,
and screen updates.
Starter Code: Adapted from the Alien Invasion starter repository:
https://github.com/RedBeard41/alien_Invasion_starter
Date: July 2026
"""

import sys
import pygame
from time import sleep

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats

class AlienInvasion:
    """Sets up, launches, and updates the Alien Invasion game."""
    def __init__(self) -> None:
        """Initialize the game, create the game window, and set up the game objects."""
        pygame.init()

        self.game_active = True
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.resolution))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Alien Invasion - Track 1")
        self.stats = GameStats(self)

        self.bg_color = self.settings.bg_color
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        
        self._create_fleet()

    def run_game(self) -> None:
        """Run the main game loop and update active game objects each frame."""
        while True:
            self.check_events()

            if self.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

            self.update_screen()
            self.clock.tick(60)

    def _update_bullets(self) -> None:
        """Update bullet positions and remove bullets that leave the screen."""
        self.bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect.left >= self.settings.screen_width:
                self.bullets.remove(bullet)
        self._check_bullet_alien_collisions()

        self._check_aliens_bottom()

    def _check_bullet_alien_collisions(self) -> None:
        """Handle bullet-alien collisions and create a new fleet when needed."""
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True
        )

        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()

    def check_events(self) -> None:
        """Respond to window, keypress, and key-release events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self.check_keyup_events(event)

    def check_keydown_events(self, event: pygame.event.Event) -> None:
        """Respond to supported keypress events."""
        if event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_SPACE:
            self.fire_bullet()
        elif event.key == pygame.K_q:
            sys.exit()

    def check_keyup_events(self, event: pygame.event.Event) -> None:
        """Respond when the up or down arrow key is released."""
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def fire_bullet(self) -> None:
        """Create and add a bullet when the active bullet limit allows it."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
    
    def update_screen(self) -> None:
        """Draw all game objects and display the updated screen."""
        self.screen.fill(self.settings.bg_color)

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.ship.blitme()
        self.aliens.draw(self.screen)

        pygame.display.flip()

    def _create_fleet(self) -> None:
        """Create and position the alien fleet."""
        alien = Alien(self)
        alien_width = alien.rect.width
        alien_height = alien.rect.height
        current_x, current_y = alien_width, alien_height
        
        while current_y < (self.settings.screen_height - 3 * alien_height):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width
            
            current_y += 2 * alien_height
            current_x = alien_width

        self.aliens.add(alien)

    def _create_alien(self, x_position: int, y_position: int) -> None:
        """Create an alien, set its position, and add it to the fleet."""
        new_alien = Alien(self)
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    def _update_aliens(self) -> None:
        """Update alien positions and check for collisions with the ship."""
        self._check_fleet_edges()
        self.aliens.update()

        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

    def _ship_hit(self) -> None:
        """Handle a ship hit and end the game when no ships remain."""
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1

            self.bullets.empty()
            self.aliens.empty()

            self._create_fleet()
            self.ship.center_ship()

            sleep(0.5)
        else:
            self.game_active = False

    def _check_fleet_edges(self) -> None:
        """Check whether any alien has reached a screen edge."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self) -> None:
        """Drop the entire fleet and change the fleet's direction."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _check_aliens_bottom(self) -> None:
        """Check whether any alien has reached the bottom of the screen."""
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                self._ship_hit()
                break


if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()