class GameStats():
    """rastreia estatistica do Alien Invasion"""

    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()

    def reset_stats(self):
        """inicializa estatisticas que podem mudar durante o jogo"""
        self.ships_left = self.ai_settings.ship_limit

        # Inicia Invasão Alienígena em um estado ativo
        self.game_active = True