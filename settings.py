class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialise the game's settings."""
        #Screen settings
        self.screen_width =1200
        self.screen_height = 300
        self.bg_color = (230,230,230)

        #ship settings
        self.ship_speed = 1.5