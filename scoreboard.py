import pygame.font

class Scoreboard():
    """Classe para relatar as informações de pontuação"""
    def __init__(self, ai_settings, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        # Configurações de fonte para imformações de pontuação
        self.text_collor = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # Prepara a imagem inicial de pontos
        self.prep_score()
        self.prep_high_score()
        self.prep_level()

    def prep_score(self):
        """Torna os pontos em uma imagem renderizada"""
        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score).replace(',','.')
        self.score_image = self.font.render(score_str, True, self.text_collor, self.ai_settings.bg_collor)

        # Exibe os ponos na canto superior direito da tela
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """ Desenha a pontuação na tela"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)

    def prep_high_score(self):
        """Torna o recorde de pontos em de uma imagem renderizada"""
        high_score = int(round(self.stats.high_score, -1))
        high_score_str = "{:,}".format(high_score).replace(',','.')
        self.high_score_image = self.font.render(high_score_str, True, self.text_collor, self.ai_settings.bg_collor)

        # Exibe o recorde de pontos na canto superior da tela
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_level(self):
        """Torna o level em uma imagem renderizada"""
        self.level_image = self.font.render(str(self.stats.level), True, self.text_collor, self.ai_settings.bg_collor)

        # Posiciona o level baixo dos pontos
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10




