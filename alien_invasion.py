import sys

import pygame
from pygame.sprite import Group

import ship
from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf

def run_game():

    pygame.init()
    ai_settings = Settings()

    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(ai_settings, screen)

    bullets = Group()
    aliens = Group()


    gf.create_fleet(ai_settings, screen, ship, aliens)


    bg_color(230, 230, 230)


    alien = Alien(ai_settings, screen)



   while True:


       gf.check_events(ai_settings, screen, ship, bullets)
       ship.update()

       gf.update_bullets(bullets)
       gf.update_aliens(aliens)
       gf.update_screen(ai_settings, screen, ship, alien, bullets)

       screen.fill(ai_settings.bg_color)
       ship.blitme()

       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               sys.exit()

       pygame.display.flip()



run_game()