import pygame.sprite

from alien import Alien
from bullet import Bullet
from game_stats import GameStats
from scores import Scoreboard
from settings import Settings
from ship import Ship
from widgets import Button


def render(screen, ship: Ship, bullets: pygame.sprite.Group,
           aliens: pygame.sprite.Group, stats: GameStats, button: Button, score_board: Scoreboard):
    screen.fill(Settings.bg_color)  # set bg

    for bullet in bullets.sprites():  # create bullets
        bullet: Bullet
        bullet.render_bullet()
    ship.render()

    for alien in aliens.sprites():
        alien: Alien
        alien.render()

    score_board.render()

    if not stats.game_active:
        button.render()
    pygame.display.flip()
