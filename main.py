import sys

import pygame
from pygame.sprite import Group

from alien import Alien
from event_handlers import handle_events
from game_stats import GameStats
from render import render
from scores import Scoreboard
from settings import Settings

from ship import Ship
from update_game_state import update_game_state
import logging

from widgets import Button

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
        self.bullets = Group()  # bullet group
        self.aliens = Group()
        self.game_stats = GameStats()
        self.score_board = Scoreboard(self.screen, self.game_stats)
        self.clock = pygame.time.Clock()
        logger.debug("game initialized")


    def setup(self):
        self.ship: Ship = Ship(self.screen)  # create ship
        Alien.create_fleet(self.screen, self.aliens, self.ship.rect.height)

    def run(self):
        self.setup()
        play_button = Button(self.screen, "play")
        last_fr = 0
        try:

            while True:
                # handle events
                handle_events(self.screen, self.ship, self.bullets, self.game_stats, play_button, self.aliens,
                              self.score_board)
                if self.game_stats.game_active:
                    update_game_state(self.screen, self.ship, self.bullets,
                                      self.aliens, self.game_stats, self.score_board)

                render(self.screen, self.ship, self.bullets, self.aliens, self.game_stats, play_button,
                       self.score_board)
                self.clock.tick()
                cur_fr = int(self.clock.get_fps())
                if (last_fr - 5) <= cur_fr >= (last_fr+5):
                    logger.debug(f"FPS=> {cur_fr}")
                last_fr = cur_fr
        except KeyboardInterrupt:
            sys.exit(0)


if __name__ == '__main__':
    game = AlienInvasion()
    logger.info("starting")

    game.run()
