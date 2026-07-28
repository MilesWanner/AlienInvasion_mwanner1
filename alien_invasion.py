"""
Program: Alien Invasion - Track 1 (Main Module)
Author: Miles Wanner
Purpose: Run Alien Invasion and manage events, objects, collisions,
scoring, game states, and screen updates.
Starter Code: Adapted from the Alien Invasion starter repository:
https://github.com/RedBeard41/alien_Invasion_starter
Date: July 2026
"""

import sys
from time import sleep

import pygame

from alien import Alien
from bullet import Bullet
from button import Button
from game_stats import GameStats
from scoreboard import Scoreboard
from settings import Settings
from ship import Ship


class AlienInvasion:
    """Set up, launch, and update Alien Invasion."""

    def __init__(self) -> None:
        """Initialize the game and create its resources."""
        pygame.init()

        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            self.settings.resolution
        )
        pygame.display.set_caption(
            "Alien Invasion - Track 1"
        )

        self.clock = pygame.time.Clock()

        self.stats = GameStats(self)
        self.scoreboard = Scoreboard(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self.play_button = Button(self, "Play")

        self.game_active = False

        self._create_fleet()

    def run_game(self) -> None:
        """Run the main game loop."""
        while True:
            self.check_events()

            if self.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

            self.update_screen()
            self.clock.tick(60)

    def check_events(self) -> None:
        """Respond to keyboard, mouse, and window events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self.check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self.check_keyup_events(event)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(
        self,
        mouse_pos: tuple[int, int],
    ) -> None:
        """Start a new game when Play is clicked."""
        button_clicked = (
            self.play_button.rect.collidepoint(
                mouse_pos
            )
        )

        if button_clicked and not self.game_active:
            self._reset_game()

    def _reset_game(self) -> None:
        """Reset the game and prepare a new session."""
        self.settings.initialize_dynamic_settings()
        self.stats.reset_stats()

        self.scoreboard.prep_score()
        self.scoreboard.prep_level()
        self.scoreboard.prep_ships()

        self.bullets.empty()
        self.aliens.empty()

        self._create_fleet()
        self.ship.center_ship()

        self.game_active = True
        pygame.mouse.set_visible(False)

    def check_keydown_events(
        self,
        event: pygame.event.Event,
    ) -> None:
        """Respond to supported keypress events."""
        if event.key == pygame.K_UP:
            self.ship.moving_up = True

        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True

        elif event.key == pygame.K_SPACE:
            self.fire_bullet()

        elif event.key == pygame.K_q:
            sys.exit()

    def check_keyup_events(
        self,
        event: pygame.event.Event,
    ) -> None:
        """Respond to supported key-release events."""
        if event.key == pygame.K_UP:
            self.ship.moving_up = False

        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def fire_bullet(self) -> None:
        """Fire a bullet when the bullet limit allows it."""
        if (
            len(self.bullets)
            < self.settings.bullets_allowed
        ):
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self) -> None:
        """Update bullets and remove those beyond the screen."""
        self.bullets.update()

        for bullet in self.bullets.copy():
            if (
                bullet.rect.left
                >= self.settings.screen_width
            ):
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self) -> None:
        """Handle collisions between bullets and aliens."""
        collisions = pygame.sprite.groupcollide(
            self.bullets,
            self.aliens,
            True,
            True,
        )

        if collisions:
            for aliens in collisions.values():
                self.stats.score += (
                    self.settings.alien_points
                    * len(aliens)
                )

            self.scoreboard.prep_score()
            self.scoreboard.check_high_score()

        if not self.aliens:
            self.bullets.empty()

            self.settings.increase_speed()
            self.stats.level += 1
            self.scoreboard.prep_level()

            self._create_fleet()

    def _create_fleet(self) -> None:
        """Create and position the alien fleet."""
        alien = Alien(self)
        alien_width = alien.rect.width
        alien_height = alien.rect.height

        current_x = 8 * alien_width
        current_y = alien_height

        while current_y < (
            self.settings.screen_height
            - 3 * alien_height
        ):
            while current_x < (
                self.settings.screen_width
                - 2 * alien_width
            ):
                self._create_alien(
                    current_x,
                    current_y,
                )
                current_x += 2 * alien_width

            current_y += 2 * alien_height
            current_x = 8 * alien_width

    def _create_alien(
        self,
        x_position: int,
        y_position: int,
    ) -> None:
        """Create an alien and add it to the fleet."""
        new_alien = Alien(self)
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    def _update_aliens(self) -> None:
        """Update the fleet and detect ship collisions."""
        self.aliens.update()

        if pygame.sprite.spritecollideany(
            self.ship,
            self.aliens,
        ):
            self._ship_hit()

        self._check_aliens_left()

    def _ship_hit(self) -> None:
        """Handle the ship being hit by an alien."""
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1
            self.scoreboard.prep_ships()

            self.bullets.empty()
            self.aliens.empty()

            self._create_fleet()
            self.ship.center_ship()

            sleep(0.5)

        else:
            self.game_active = False
            pygame.mouse.set_visible(True)

    def _check_aliens_left(self) -> None:
        """Check whether an alien reached the left edge."""
        for alien in self.aliens.sprites():
            if (
                alien.rect.left
                <= 0
            ):
                self._ship_hit()
                break

    def update_screen(self) -> None:
        """Draw all game objects and update the display."""
        self.screen.fill(self.settings.bg_color)

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.ship.blitme()
        self.aliens.draw(self.screen)

        self.scoreboard.show_score()

        if not self.game_active:
            self.play_button.draw_button()

        pygame.display.flip()


if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()