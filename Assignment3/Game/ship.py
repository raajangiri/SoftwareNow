import pygame

class Ship:
    def __init__(self, ai_settings, screen):
        """Initialize the ship and set its starting position."""
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load('ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def update(self, moving_left, moving_right):
        """Update the ship's position based on the movement flags."""
        if moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += self.ai_settings.ship_speed  # Use defined speed
        if moving_left and self.rect.left > 0:
            self.rect.x -= self.ai_settings.ship_speed  # Use defined speed

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
