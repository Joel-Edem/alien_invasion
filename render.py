import pygame.sprite

from alien import Alien
from bullet import Bullet
from settings import Settings
from ship import Ship


def render(screen, ship: Ship, bullets: pygame.sprite.Group, aliens: pygame.sprite.Group):
    screen.fill(Settings.bg_color)  # set bg

    for bullet in bullets.sprites():  # create bullets
        bullet: Bullet
        bullet.render_bullet()
    ship.render()

    for alien in aliens.sprites():
        alien: Alien
        alien.render()

    pygame.display.flip()
