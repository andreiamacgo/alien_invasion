import sys
import pygame
from settings import Settings
from game_stats import GameStats
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

    # Cria uma instância para guardar a estatística do jogo
    stats = GameStats(ai_settings)

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
        gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
        gf.update_aliens(ai_settings,  stats, screen, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

run_game()
