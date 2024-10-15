import pygame
import random

class Alien(pygame.sprite.Sprite):
    def __init__(self, ai_settings, screen):
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load('alien.bmp')
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, ai_settings.screen_width - self.rect.width)
        self.rect.y = random.randint(0, 100)

    def update(self):
        """Move the alien downwards based on the alien speed."""
        self.rect.y += self.ai_settings.alien_speed  # Move downwards by alien speed

    def draw(self):
        """Draw the alien on the screen."""
        self.screen.blit(self.image, self.rect)  # Draw the alien
