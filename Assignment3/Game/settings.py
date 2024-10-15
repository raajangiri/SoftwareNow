class Settings:
    """A class to store all settings for Alien Invasion."""
    def __init__(self):
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (0, 0, 0)
        self.ship_speed = 2.0  # Increase ship speed
        self.bullet_speed = 3.0
        self.bullet_limit = 3
        self.alien_speed = 0.6  # Ideal speed for aliens
