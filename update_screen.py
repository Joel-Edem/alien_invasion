import pygame

from alien import Alien
from settings import Settings


def update_game_state(ship, bullets: pygame.sprite.Group, aliens: pygame.sprite.Group):
    ship.update()  # update ship
    update_bullets(bullets)  # update bullets
    update_aliens(aliens)


def update_aliens(aliens):
    check_fleet_edges(aliens)
    aliens.update()


def check_fleet_edges(aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(aliens)
            break


def change_fleet_direction(aliens):
    for alien in aliens.sprites():
        alien.rect.y += Settings.fleet_drop_speed
    Alien.going_right *= -1


def update_bullets(bullets: pygame.sprite.Group):
    bullets.update()
    clear_bullets(bullets)


def clear_bullets(bullets: pygame.sprite.Group):
    for bullet in bullets.sprites():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
