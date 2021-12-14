from settings import Settings


class GameStats:

    def __init__(self):
        pass
        self.ships_left = 0

        self.game_active = False
        self.score = 0
        self.high_score = 0
        self.level = 1

        self.reset_stats()

    def reset_stats(self):
        self.ships_left = Settings.ship_limit
        self.score = 0
        self.level = 1
