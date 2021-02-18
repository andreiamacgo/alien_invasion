class GameStats():
    """rastreia estatistica do Alien Invasion"""

    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()

        # Inicia o jogo em um estado inativo
        self.game_active = False

        # Recorde de pontos -  nunca deve er redefinido
        self.high_score = 0

    def reset_stats(self):
        """inicializa estatisticas que podem mudar durante o jogo"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0

        # Inicia Invasão Alienígena em um estado ativo
        self.game_active = True