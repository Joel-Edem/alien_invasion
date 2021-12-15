import sys

import pygame
from pygame.sprite import Group

from alien import Alien
from bullet import Bullet
from game_stats import GameStats
from scores import Scoreboard
from settings import Settings
from ship import Ship
from widgets import Button


def handle_events(screen, ship: Ship, bullets: Group, stats: GameStats, button: Button,
                  aliens: Group, score_board: Scoreboard):
    # listen to and handle events
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif e.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            handle_click(mouse_x, mouse_y, button, stats, screen, ship, aliens, bullets, score_board)

        elif e.type == pygame.KEYDOWN:
            handle_keydown(screen, e, ship, bullets)

        elif e.type == pygame.KEYUP:
            handle_key_up(e, ship)


def handle_click(x, y, button: Button, stats: GameStats, screen, ship: Ship, aliens: Group,
                 bullets: Group, score_board: Scoreboard):
    clicked = button.rect.collidepoint(x, y)
    if clicked and not stats.game_active:
        Settings.reset_settings()
        pygame.mouse.set_visible(False)
        aliens.empty()
        bullets.empty()
        stats.reset_stats()
        score_board.update_level()
        score_board.update_high_score()
        score_board.update_score()
        score_board.update_ships_left()
        stats.game_active = True

        Alien.create_fleet(screen, aliens, ship.rect.height)
        ship.center_ship()


def handle_keydown(screen, e: pygame.event.Event, ship, bullets):
    if e.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif e.key == pygame.K_LEFT:
        ship.moving_left = True
    elif e.key == pygame.K_SPACE:
        Bullet.fire_bullet(bullets, screen, ship)
    if e.key == pygame.K_q:
        pygame.quit()
        sys.exit(0)


def handle_key_up(e, ship):
    if e.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif e.key == pygame.K_LEFT:
        ship.moving_left = False
