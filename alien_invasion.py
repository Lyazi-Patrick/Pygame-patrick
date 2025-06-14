import sys
from time import sleep

import pygame
from settings import Settings
from game_stats import GameStats
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    """Overall class to manage game assets and behavior"""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()

        """self.screen = pygame.display.set_mode((
            self.settings.screen_width, self.settings.screen_height
        ))
        pygame.init()"""
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        
        #Set the background color.
        self.bg_color = (230,230,230)

        pygame.display.set_caption('Alien Invasion')
        #Create an instance to store game statistics.
        self.stats = GameStats(self)
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

    def _create_fleet(self):
         """Create the fleet of aliens."""
         #Make an alien.
         #Create an alien and find the number of aliens in a row.
         #Spacing between each alien is equal to one alien width.
         alien = Alien(self)
         alien_width, alien_height = alien.rect.size
         available_space_x = self.settings.screen_width - (2*alien_width)
         number_aliens_x = available_space_x // (2*alien_width)
         
         #Determine the number of rows of aliens that fit on the screen.
         ship_height = self.ship.rect.height
         available_space_y = (self.settings.screen_height - (3*alien_height) - ship_height)
         number_rows = available_space_y // (2*alien_height)

         #Create the full fleet of aliens.
         for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number,row_number)

    def _create_alien(self, alien_number, row_number):
            #Create an alien and place it in the row.
            alien = Alien(self)
            alien_width, alien_height = alien.rect.size
            alien.x = alien_width + 2* alien_width*alien_number
            alien.rect.x = alien.x
            alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
            self.aliens.add(alien)

    def _check_fleet_edges(self):
         """Respond appropriately if any aliens have reached an Edge."""
         for alien in self.aliens.sprites():
            if alien.check_edges():
              self._change_fleet_direction()
              break
    
    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction."""
        for alien in self.aliens.sprites():
              alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1
            

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_aliens()

    def _update_bullets(self):
            """Update position of bullets and get rid of old bullets."""
            #Update bullet positions.
            self.bullets.update()

            #Get rid of the bullets that have dissappeared.
            for bullet in self.bullets.copy():
                 if bullet.rect.bottom <= 0:
                      self.bullets.remove(bullet)
            #print(len(self.bullets))

            self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
            self._update_screen()
            #Check for any bullets that have hit aliens.
            #if so, get rid of the bullet and the alien.
            collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True,True)

            if not self.aliens:
                 #Destroy existing bullets and create new fleet.
                 self.bullets.empty()
                 self._create_fleet()
    
    def _update_aliens(self):
         """Check if the fleet is at the edge,Update the positions of all aliens in the fleet."""
         self._check_fleet_edges()
         self.aliens.update()
         #look for alien-ship collisions.
         if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()   
        #look for aliens hitting the bottom of the screen.
            self._check_aliens_bottom()
    
    def _ship_hit(self):
         """Respond to the ship being hit by an alien."""
         #Decrement ships_left.
         self.stats.ships_left -= 1

         #Get rid of any remaining aliens and bullets.
         self.aliens.empty()
         self.bullets.empty()

         #Create a new fleet and center the ship.
         self._create_fleet()
         self.ship.center_ship()

         #pause.
         sleep(0.5)
        

    def _check_events(self):
            """Respond to keypresses and mouse events."""
            #Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                     self._check_keydown_events(event)

                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)
    
    def _check_keydown_events(self,event):
        """Respond to Keypresses."""
        if event.key == pygame.K_RIGHT:
             self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
             self.ship.moving_left = True
        elif event.key == pygame.K_q:
             sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
    
    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
         """Create a new bullet and add it to the bullets group."""
         if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet) 

    def _check_aliens_bottom(self):
         """Check if any aliens have reached the bottom of screen."""
         screen_rect = self.screen.get_rect()
         for alien in self.aliens.sprites():
              if alien.rect.bottom >= screen_rect.bottom:
                   #Treat this the same as if the ship got hit.
                   self._ship_hit()
                   break               
    def _update_screen(self):
            """Update images on the screen, and flip to the new screen"""
            #Redraw the screen during each pass through the loop.
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()
            for bullet in self.bullets.sprites():
                 bullet.draw_bullet()
            self.aliens.draw(self.screen)

            #Make the most recently drawn screen visible.
            pygame.display.flip()

if __name__ == '__main__':
    #Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()