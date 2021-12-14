import time

import pygame
from pygame.sprite import Group

from alien import Alien
from game_stats import GameStats
from scores import Scoreboard
from settings import Settings
from ship import Ship


def update_game_state(screen, ship: Ship, bullets: Group, aliens: Group, stats: GameStats, score_board: Scoreboard):
    ship.update()  # update ship
    update_bullets(bullets, aliens, screen, ship, stats, score_board)  # update bullets
    update_aliens(aliens, ship, stats, screen, bullets, score_board)


def update_aliens(aliens, ship, stats, screen, bullets, score_board):
    check_fleet_edges(aliens)
    aliens.update()
    check_ship_hit(stats, screen, ship, aliens, bullets, score_board)
    check_aliens_bottom(stats, screen, ship, aliens, bullets, score_board)


def reset_game(stats, screen, ship, aliens, bullets, score_board):
    if stats.ships_left:
        stats.ships_left -= 1
        score_board.update_ships_left()
        aliens.empty()
        bullets.empty()
        Alien.create_fleet(screen, aliens, ship.rect.height)
        ship.center_ship()

        time.sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


def check_ship_hit(stats, screen, ship, aliens, bullets, score_board):
    if pygame.sprite.spritecollideany(ship, aliens):
        reset_game(stats, screen, ship, aliens, bullets, score_board)


def check_aliens_bottom(stats, screen, ship, aliens, bullets, score_board):
    # screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= ship.rect.top:
            reset_game(stats, screen, ship, aliens, bullets, score_board)
            break


def check_fleet_edges(aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(aliens)
            break


def change_fleet_direction(aliens):
    for alien in aliens.sprites():
        alien.rect.y += Settings.fleet_drop_speed
    Settings.fleet_direction *= -1


def update_bullets(bullets: Group, aliens: Group, screen, ship: Ship, stats: GameStats,
                   score_board: Scoreboard):
    bullets.update()
    check_alien_bullet_collision(bullets, aliens, screen, ship, stats, score_board)
    clear_bullets(bullets)


def check_high_score(stats: GameStats, score_board: Scoreboard):
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        score_board.update_high_score()


def check_alien_bullet_collision(bullets: Group, aliens: Group, screen,
                                 ship: Ship, stats: GameStats, score_board: Scoreboard):
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        for _alien in collisions.values():
            _alien: [Alien]
            stats.score += (Settings.alien_points * len(_alien))
            score_board.update_score()
        check_high_score(stats, score_board)

    if len(aliens) == 0:
        bullets.empty()
        Settings.increase_speed()

        stats.level += 1
        score_board.update_level()

        Alien.create_fleet(screen, aliens, ship.rect.height)


def clear_bullets(bullets: pygame.sprite.Group):
    for bullet in bullets.sprites():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
