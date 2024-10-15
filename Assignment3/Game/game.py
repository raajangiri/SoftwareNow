import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, WHITE
from spaceship import Spaceship
from alien import Alien

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Alien Invasion")
        self.clock = pygame.time.Clock()
        self.spaceship = Spaceship(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 70)
        self.aliens = [Alien() for _ in range(5)]  # Start with 5 aliens
        self.score = 0  # Initialize score

    def run(self):
        running = True
        while running:
            keys = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            # Update game objects
            self.spaceship.update(keys)
            for alien in self.aliens:
                alien.update()
                if alien.rect.top > SCREEN_HEIGHT:  # If alien goes off screen
                    alien.rect.y = random.randint(-100, -40)  # Reset alien position
                    alien.rect.x = random.randint(0, SCREEN_WIDTH - alien.rect.width)  # Random horizontal position
                    self.score += 1  # Increase score for each alien that goes off screen

            # Draw everything
            self.screen.fill(WHITE)
            self.spaceship.draw(self.screen)
            for alien in self.aliens:
                alien.draw(self.screen)

            # Display the score
            font = pygame.font.SysFont(None, 36)
            score_text = font.render(f'Score: {self.score}', True, (0, 0, 0))
            self.screen.blit(score_text, (10, 10))

            pygame.display.flip()
            self.clock.tick(FPS)

        pygame.quit()
