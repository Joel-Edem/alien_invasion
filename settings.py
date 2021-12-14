class Settings:
    aspect_ratio = 16 * 9
    screen_width = 1200
    screen_height = screen_width / 16 * 9
    bg_color = (230, 230, 230)

    # Ship settings
    ship_speed_factor = 5
    ship_limit = 3
    # Bullet settings
    bullet_speed_factor = 3
    bullet_width = 3
    bullet_height = 15
    bullet_color = 60, 60, 60
    max_bullets = 3

    # Alien Config
    alien_speed_factor = 1
    fleet_drop_speed = 10
    fleet_direction = 1
    # LEVEL SETTINGS
    speedup_scale = 1.1

    # Scoring
    alien_points = 50
    score_scale = 1.5

    @classmethod
    def reset_settings(cls):
        cls.ship_speed_factor = 5
        cls.bullet_speed_factor = 3
        cls.alien_speed_factor = 1
        cls.fleet_direction = 1  # fleet_direction of 1 represents right; -1 represents left.

    @classmethod
    def increase_speed(cls):
        cls.ship_speed_factor *= cls.speedup_scale
        cls.bullet_speed_factor *= cls.speedup_scale
        cls.alien_speed_factor *= cls.speedup_scale
        cls.alien_points = int(cls.alien_points*cls.score_scale)
