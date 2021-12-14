import sys

import pygame
from pygame.sprite import Group

from alien import Alien
from event_handlers import handle_events
from images.game_stats import GameStats
from render import render
from settings import Settings

from ship import Ship
from update_screen import update_game_state
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class AlienInvasion:

    def __init__(self):
        logger.debug("initializing game")
        pygame.init()
        self.screen = pygame.display.set_mode(
            (Settings.screen_width, Settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.ship = None
        self.bullets = None
        self.aliens = None
        self.game_stats = None
        logger.debug("game initialized")

    def setup(self):

        self.ship: Ship = Ship(self.screen)  # create ship
        self.bullets = Group()  # bullet group
        self.aliens = Group()
        self.game_stats = GameStats()
        Alien.create_fleet(self.screen, self.aliens, self.ship.rect.height)

    def run(self):
        self.setup()
        try:

            while True:
                # handle events
                handle_events(self.screen, self.ship, self.bullets)
                if self.game_stats.game_active:
                    update_game_state(self.screen, self.ship, self.bullets, self.aliens, self.game_stats)

                render(self.screen, self.ship, self.bullets, self.aliens)

        except KeyboardInterrupt:
            sys.exit(0)


if __name__ == '__main__':
    game = AlienInvasion()
    logger.info("starting")

    game.run()
