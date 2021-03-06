import pygame.image
from pygame.sprite import Sprite

from settings import Settings


class Ship(Sprite):

    def __init__(self, screen):
        super().__init__()
        self.screen: pygame.display = screen

        # load image
        self.image = pygame.image.load("images/ship.bmp").convert()
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)
        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += Settings.ship_speed_factor
        elif self.moving_left and self.rect.left > 0:
            self.center -= Settings.ship_speed_factor

        self.rect.centerx = self.center

    def render(self):
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        self.center = self.screen_rect.centerx
