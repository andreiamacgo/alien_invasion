class Settings():
    def __init__(self):
        """Inicia as configurações estáticas do jogo"""
        # Configurações de tela
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_collor = (0, 180, 255)

        # Configuraçõe de espaçonave
        self.ship_limit = 3

        # Definições de tiro
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_collor = 255, 140, 50
        self.bullets_allowed = 4

        # Configurações de Alien
        self.fleet_drop_speed = 10

        # Quão rápido o jogo acelera
        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()


    def initialize_dynamic_settings(self):
        """Inicia configurações que mudam no decorrer do jogo"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

        # fleet_direction igual a 1 representa direta e igual -1 representa esquerda
        self.fleet_direction = 1

    def increase_speed(self):
        """Aumenta as configurações de velocidades"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale