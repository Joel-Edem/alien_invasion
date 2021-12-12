import pygame
from pygame.sprite import Group

from event_handlers import handle_events
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
        logger.debug("game initialized")

    def run(self):
        ship: Ship = Ship(self.screen)  # create ship
        bullets = Group()  # bullet group
        try:

            while True:
                # handle events
                handle_events(self.screen, ship, bullets)

                update_game_state(ship, bullets)

                render(self.screen, ship, bullets)

        except KeyboardInterrupt:
            print("Shutting")


if __name__ == '__main__':
    game = AlienInvasion()
    logger.info("starting")

    game.run()

