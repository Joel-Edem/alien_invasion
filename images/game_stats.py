from settings import Settings


class GameStats:

    def __init__(self):
        pass
        self.ships_left = 0
        self.reset_stats()
        self.game_active = True

    def reset_stats(self):
        self.ships_left = Settings.ship_limit

