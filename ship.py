import pygame


class Ship():
    def __init__(self, ai_settings, screen):
        """Inicializa a nave espacial e define sua posição inicial"""
        self.screen = screen
        self.ai_settings = ai_settings

        #carrega a imagem da nave
        self.image = pygame.image.load('images/nave2.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #inicia uma nova nave espacial na parte inferior central
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #armazena um valor decimal para o centro da espaçonave
        self.center = float(self.rect.centerx)

        #flag de movimento
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """atualiza a movimentação da espaçonave com base na flag de movimento"""
        #atualiza o valor do centro da espaçonave, e não do retângulo
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        #atualiza o objeto rect de acorco com self.enter
        self.rect.centerx = self.center


    def blitme(self):
        """Desenha a nave espacial em sua localização atual"""
        self.screen.blit(self.image, self.rect)