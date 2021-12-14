import pygame.font
from pygame.sprite import Group

from game_stats import GameStats
from settings import Settings
from ship import Ship


class Scoreboard:

    def __init__(self, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats: GameStats = stats
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont('poppins', 48)
        self.score_image = None
        self.score_rect = None

        self.high_score_image = None
        self.high_score_rect = None

        self.level_image = None
        self.level_image_rect = None
        self.ships_left = Group()
        self.update_score()
        self.update_high_score()
        self.update_level()
        self.update_ships_left()

    def update_high_score(self):
        high_score = "{:,}".format(int(round(self.stats.high_score)))
        self.high_score_image = self.font.render(
            high_score, True, self.text_color, Settings.bg_color)
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def update_level(self):
        self.level_image = self.font.render(
            f"{self.stats.level}", True, self.text_color, Settings.bg_color)
        self.level_image_rect = self.high_score_image.get_rect()
        self.level_image_rect.right = self.score_rect.right
        self.level_image_rect.top = self.score_rect.bottom + 10

    def update_score(self):
        score_str = "{:,}".format(int(round(self.stats.score, -1)))
        self.score_image = self.font.render(score_str, True, self.text_color, Settings.bg_color)

        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def render(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)

        self.screen.blit(self.level_image, self.level_image_rect)
        self.ships_left.draw(self.screen)

    def update_ships_left(self):
        self.ships_left = Group()
        for ship_no in range(self.stats.ships_left):
            ship = Ship(self.screen)
            ship.rect.x = 10 + ship_no * ship.rect.width
            ship.rect.y = 10
            self.ships_left.add(ship)
