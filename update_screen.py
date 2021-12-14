import time

import pygame
from pygame.sprite import Group

from alien import Alien
from images.game_stats import GameStats
from settings import Settings
from ship import Ship


def update_game_state(screen, ship: Ship, bullets: Group, aliens: Group, stats: GameStats):
    ship.update()  # update ship
    update_bullets(bullets, aliens, screen, ship)  # update bullets
    update_aliens(aliens, ship, stats, screen, bullets)


def update_aliens(aliens, ship, stats, screen, bullets):
    check_fleet_edges(aliens)
    aliens.update()
    check_ship_hit(stats, screen, ship, aliens, bullets)
    check_aliens_bottom(stats, screen, ship, aliens, bullets)


def reset_game(stats, screen, ship, aliens, bullets):
    if stats.ships_left:
        stats.ships_left -= 1
        aliens.empty()
        bullets.empty()
        Alien.create_fleet(screen, aliens, ship.rect.height)
        ship.center_ship()

        time.sleep(0.5)
    else:
        stats.game_active = False


def check_ship_hit(stats, screen, ship, aliens, bullets):
    if pygame.sprite.spritecollideany(ship, aliens):
        reset_game(stats, screen, ship, aliens, bullets)


def check_aliens_bottom(stats, screen, ship, aliens, bullets):
    # screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= ship.rect.top:
            reset_game(stats, screen, ship, aliens, bullets)
            break


def check_fleet_edges(aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(aliens)
            break


def change_fleet_direction(aliens):
    for alien in aliens.sprites():
        alien.rect.y += Settings.fleet_drop_speed
    Alien.going_right *= -1


def update_bullets(bullets: pygame.sprite.Group, aliens: pygame.sprite.Group, screen, ship: Ship):
    bullets.update()
    check_alien_bullet_collision(bullets, aliens, screen, ship)
    clear_bullets(bullets)


def check_alien_bullet_collision(bullets: pygame.sprite.Group, aliens: pygame.sprite.Group, screen, ship: Ship):
    pygame.sprite.groupcollide(bullets, aliens, True, True)

    if len(aliens) == 0:
        bullets.empty()
        Alien.create_fleet(screen, aliens, ship.rect.height)


def clear_bullets(bullets: pygame.sprite.Group):
    for bullet in bullets.sprites():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
