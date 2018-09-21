import pygame
import self as self
from pygame.examples.headless_no_windows_needed import screen


class Ship():
    def __init__(self, ai_settings, screen):

        """Initialize the ship and set its starting position"""
        self.screen = screen


        self.ai_settings = ai_settings

        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom


        self.center = float(self.rect.centerx)




        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on the movement flag."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left >0:
            self.rect.centerx -= self.ai_settings.ship_speed_factor
    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
