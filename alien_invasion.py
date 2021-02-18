import sys
import pygame
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
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

    #Cria o botão de play
    play_button = Button(ai_settings, screen, "Jogar")

    # Cria uma instância para guardar a estatística do jogo e cria um placar
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

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
        gf.check_event(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings,  stats, screen, sb, ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)

run_game()
