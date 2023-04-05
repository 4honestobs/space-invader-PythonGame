import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    """Initialize the ship and set its starting position."""
    def __init__(self, screen, game_settings):
        super().__init__()
        self.screen = screen
        self.game_settings = game_settings
        # Load the ship image and get it's rect.
        self.image = pygame.image.load('ship.png')

        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = 0 # Value position y of the ship.
        self.rect.bottom = self.screen_rect.bottom
        # Store a decimal value for the ship's center.
        self.center = float(self.rect.centerx)
        # Movement flag.
        self.moving_right = False
        self.moving_left = False
        self.moving_forward = False
        self.moving_downward = False

    def update(self):
        """Update the ship's position based on the movement flag."""
        if self.moving_right is True and self.rect.right < self.screen_rect.right:
            self.center += self.game_settings.ship_speed_factor
        if self.moving_left is True and self.rect.left > 0:
            self.center -= self.game_settings.ship_speed_factor
        if self.moving_forward is True and self.rect.top > self.screen_rect.top: # Update movement up and down
            self.centery -= self.game_settings.ship_speed_factor
        if self.moving_downward is True and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.game_settings.ship_speed_factor

        # Update rect object from self.center
        self.rect.centerx = self.center

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Center the ship on the screen."""
        self.center = self.screen_rect.centerx
        self.centery = 570 # Edit base position of ship.


if __name__ == '__main__':
    print("Go to main file and run from there.")

