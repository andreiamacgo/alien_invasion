import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Classe pra representar alien"""

    def __init__(self, ai_settings, screen):
        """Inicia o alien e define a sua posição inicial"""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Carrega a imagem do alien e define seu atributo rect
        self.image = pygame.image.load('images/alien3.bmp')
        self.rect = self.image.get_rect()

        # Inicia cada novo alien no topo esquerdo da tela
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Guarda a posição exata do alien
        self.x = float(self.rect.x)

    def blitme(self):
        """Desenha o alien na sua posição atual"""
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        """Retorna 'Treu' ser o alien estiver na borda da tela"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x