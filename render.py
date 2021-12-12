import pygame.sprite

from bullet import Bullet
from settings import Settings
from ship import Ship


def render(screen, ship:Ship, bullets: pygame.sprite.Group):
    screen.fill(Settings.bg_color)  # set bg

    for bullet in bullets.sprites():  # create bullets
        bullet: Bullet
        bullet.render_bullet()
