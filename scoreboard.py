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

    def prep_score(self):
        """Torna os pontos dentro de uma imagem renderizada"""
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
