import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Classe para gerenciar tiros de fogo da espaçonave"""

    def __init__(self, ai_settings, screen, ship):
        """Cria um objeto tiro para a posição atual da espçonave"""
        super().__init__()
        self.screen = screen
        # Cria  o tiro na posição (0, 0) e depois corrige a posição
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # Guarda a posião do tiro como um valor decimal
        self.y = float(self.rect.y)

        self.collor = ai_settings.bullet_collor
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """Move o projétil para cim da tela"""
        # Atualiza a posição decimal do projétil
        self.y -= self.speed_factor
        # atualiza a posição do rect
        self.rect.y = self.y

    def draw_bullet(self):
        """Desenha o projétil na tela"""
        pygame.draw.rect(self.screen, self.collor, self.rect),
