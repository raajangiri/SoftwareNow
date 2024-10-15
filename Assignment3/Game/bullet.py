import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired from the ship."""

    def __init__(self, ai_settings, screen, ship):
        """Create a bullet object at the ship's current position."""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Create a bullet rect at (0, 0) and then set correct position
        self.image = pygame.Surface((3, 15))  # Create a surface for the bullet
        self.image.fill((255, 0, 0))  # Fill it with red color
        self.rect = self.image.get_rect()  # Get the rect for the bullet
        self.rect.centerx = ship.rect.centerx  # Position bullet at the center of the ship
        self.rect.top = ship.rect.top  # Start bullet just above the ship

        # Store the bullet's position as a float
        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet up the screen."""
        # Update the bullet's position
        self.y -= self.ai_settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        self.screen.blit(self.image, self.rect)  # Draw the bullet
