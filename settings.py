class Settings():
    def __init__(self):
        # Configurações de tela
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_collor = (0, 180, 255)

        # Configuraçõe de espaçonave
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        # Definições de tiro
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_collor = 255, 140, 50
        self.bullets_allowed = 4

        # Configurações de Alien
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # fleet_direction igual a 1 representa direta e igual -1 representa esquerda
        self.fleet_direction = 1