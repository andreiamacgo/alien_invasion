import sys
import pygame
from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf
from pygame.sprite import Group



def run_game():
    # inicializ o jogi e cria o objeto tela
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Invasão Alienígena")
    ship = Ship(ai_settings, screen)
    # Cria um grupo que guarda os tiros projetados e um grupo de aliens
    bullets = Group()
    aliens = Group()

    # Cria uma frota de aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)

    bg_color = (ai_settings.bg_collor)

    #Cria um alien
    alien = Alien(ai_settings, screen)

    # inicia o loop principal do jogo
    while True:
        gf.check_event(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_aliens(ai_settings, aliens)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

run_game()
