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
        self.ship_limit = 3
        
        #Bullet settings
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 20
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 10

        #Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        #Fleet_direction of 1 represents the right; -1 represents left.
        self.fleet_direction = 1
        #How quickly the game speeds up
        self.speedup_scale = 1.1

        #How quickly the alien point values increase
        self.score_scale = 1.5
        self.initialize_dynamic_settings()
    
    def initialize_dynamic_settings(self):
        """Initialize settings that change throught the game."""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0

        #Fleet_direction of 1 represents right;-1 represents left.
        self.fleet_direction = 1

        #scoring
        self.alien_points = 50

    
    def increase_speed(self):
        """Increase speed settings and alien point values."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        