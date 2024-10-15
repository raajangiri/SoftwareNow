import pygame

class Spaceship:
    def __init__(self, x, y):
        self.image = pygame.image.load('ship.bmp')
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 5  # Movement speed of the spaceship

    def update(self, keys):
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed  # Move left
        if keys[pygame.K_RIGHT] and self.rect.right < 800:
            self.rect.x += self.speed  # Move right

    def draw(self, screen):
        screen.blit(self.image, self.rect)
