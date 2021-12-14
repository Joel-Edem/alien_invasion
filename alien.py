from collections import namedtuple

import pygame
from pygame.sprite import Sprite

from settings import Settings

Position = namedtuple('Position', ['x', 'y'])


class Alien(Sprite):

    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left < 0:
            return True

    def render(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.x += (Settings.alien_speed_factor * Settings.fleet_direction)
        self.rect.x = self.x

    @staticmethod
    def get_max_aliens_x(alien_width):
        available_space_x = Settings.screen_width - 2 * alien_width
        return int(available_space_x / (2 * alien_width))

    @staticmethod
    def get_max_aliens_y(alien_height, ship_height):

        available_y = Settings.screen_height - (3 * alien_height) - ship_height
        return int(available_y / (2 * alien_height))

    @classmethod
    def create_alien(cls, screen, position: Position):
        alien = cls(screen)
        alien.x = alien.rect.width + 2 * alien.rect.width * position.x
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * position.y
        return alien

    @classmethod
    def create_fleet(cls, screen, aliens: pygame.sprite.Group, ship_height: int):
        alien = cls(screen)
        number_of_aliens_x = cls.get_max_aliens_x(alien.rect.width)
        number_of_aliens_y = cls.get_max_aliens_y(alien.rect.height, ship_height)
        for y in range(number_of_aliens_y):
            for x in range(number_of_aliens_x):
                aliens.add(cls.create_alien(screen, Position(x, y)))
