import sys

import pygame

from bullet import Bullet


def handle_events(screen, ship, bullets):
    # listen to and handle events
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit(0)

        elif e.type == pygame.KEYDOWN:
            handle_keydown(screen, e, ship, bullets)

        elif e.type == pygame.KEYUP:
            handle_key_up(e, ship)


def handle_keydown(screen, e: pygame.event.Event, ship, bullets):
    if e.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif e.key == pygame.K_LEFT:
        ship.moving_left = True
    elif e.key == pygame.K_SPACE:
        Bullet.fire_bullet(bullets, screen, ship)


def handle_key_up(e, ship):
    if e.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif e.key == pygame.K_LEFT:
        ship.moving_left = False
