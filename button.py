import pygame.font

class Button():
    def __init__(self, ai_settings, screen, msg):
        """Iniializa atributos do botão"""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Define as dimensões e propriedade do botão
        self.width, self.height = 200, 50
        self.button_collor = (60, 170, 80)
        self.text_collor = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Constrói o objeto rect do botão e o centraliza
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # A mensagem do botão precisa ser preparada apenas uma vez
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """TRansforma mensagem em uma imagem renderizada e contraliza o texto no botão"""
        self.msg_image = self.font.render(msg, True, self.text_collor, self.button_collor)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # Desenha o botão
        self.screen.fill(self.button_collor, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
