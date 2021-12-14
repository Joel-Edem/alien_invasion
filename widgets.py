import pygame.font


class Button:
    def __init__(self, screen, message: str, **kwargs):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.width = kwargs.get('width', 200)
        self.height = kwargs.get('height', 50)
        self.button_color = kwargs.get('bg_color', (0, 255, 0))
        self.text_color = kwargs.get('text_color', (255, 255, 255))
        self.font = pygame.font.SysFont(['poppins'], kwargs.get('font_size', 48))

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        self.msg_image_rect = None
        self.msg_img = None

        self.prep_message(message)

    def prep_message(self, message):
        self.msg_img = self.font.render(message, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_img.get_rect()
        self.msg_image_rect.center = self.rect.center

    def render(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_img, self.msg_image_rect)
