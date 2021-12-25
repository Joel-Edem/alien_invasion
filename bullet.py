import pygame
from pygame.sprite import Sprite

from settings import Settings
from ship import Ship


class Bullet(Sprite):

    def __init__(self, screen, ship: Ship):
        super().__init__()

        self.screen = screen
        self.ship = ship

        # initialize bullet
        self.rect: pygame.Rect = pygame.Rect(0, 0, Settings.bullet_width, Settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.color =  Settings.bullet_color
        self.y = float(self.rect.y)
        self.speed_factor = Settings.bullet_speed_factor

    def update(self, ) -> None:
        self.y -= self.speed_factor
        self.rect.y = self.y

    def render_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

    @classmethod
    def fire_bullet(cls, bullets, screen, ship):
        # if len(bullets) < Settings.max_bullets:
        for i in range(100000):
            bullet = Bullet(screen, ship)
            bullets.add(bullet)

