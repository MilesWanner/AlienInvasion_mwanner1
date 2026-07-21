import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, ai_game):
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
        self.rect.x += self.settings.bullet_speed

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)