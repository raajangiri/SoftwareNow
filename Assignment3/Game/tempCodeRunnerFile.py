
import pygame
from settings import Settings
from ship import Ship
from alien import Alien
from bullet import Bullet
from button import Button  # Ensure you have a button.py file with the Button class

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Create ship, bullets, and restart button
    ship = Ship(ai_settings, screen)
    bullets = pygame.sprite.Group()
    restart_button = Button(screen, 'Restart')

    # Start the game
    score = 0
    level = 1  # Initialize level
    game_active = True
    aliens = pygame.sprite.Group()  # Create aliens group
    spawn_aliens(ai_settings, screen, aliens, level)

    clock = pygame.time.Clock()  # Create a clock object to control the frame rate

    # Timer variables for bullet firing
    last_bullet_time = 0
    bullet_cooldown = 500  # Cooldown in milliseconds

    # Main loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            # Check for mouse button down events
            if event.type == pygame.MOUSEBUTTONDOWN and not game_active:
                mouse_pos = pygame.mouse.get_pos()
                if restart_button.is_clicked(mouse_pos):
                    score = 0  # Reset score
                    level = 1  # Reset level
                    game_active = True  # Set the game back to active
                    aliens.empty()  # Clear existing aliens
                    spawn_aliens(ai_settings, screen, aliens, level)  # Spawn new aliens
                    bullets.empty()  # Clear bullets

        if game_active:
            keys = pygame.key.get_pressed()
            moving_left = keys[pygame.K_LEFT]
            moving_right = keys[pygame.K_RIGHT]
            fire_bullet = keys[pygame.K_SPACE]

            # Ship movement
            ship.update(moving_left, moving_right)

            # Fire bullet with cooldown
            current_time = pygame.time.get_ticks()
            if fire_bullet and current_time - last_bullet_time > bullet_cooldown:
                bullet = Bullet(ai_settings, screen, ship)
                bullets.add(bullet)
                last_bullet_time = current_time  # Update the last bullet time

            # Update bullet position
            bullets.update()

            # Check for bullet collisions with aliens
            for bullet in bullets.copy():
                bullet_hit = pygame.sprite.spritecollideany(bullet, aliens)
                if bullet_hit:
                    bullet.kill()
                    bullet_hit.kill()  # Remove the alien
                    score += 1  # Increase score
                    print(f"Score: {score}")  # Print score to console

                    # Check if the score reached a multiple of 10
                    if score % 10 == 0:
                        level += 1  # Increase level
                        print(f"Level up! Current Level: {level}")  # Print level up message
                        spawn_aliens(ai_settings, screen, aliens, level)  # Spawn new aliens for the new level

            # Update aliens' positions
            aliens.update()  # Make sure this is called to update alien positions

            # Check if any aliens have crossed the ship
            for alien in aliens:
                if alien.rect.bottom >= ai_settings.screen_height - 50:  # Game over condition
                    game_active = False  # Set game to inactive
                    break  # Exit the loop for game over

            # Clear screen
            screen.fill(ai_settings.bg_color)

            # Draw ship, aliens, and bullets
            ship.blitme()
            aliens.draw(screen)
            bullets.draw(screen)

            # Draw score and level
            score_image = pygame.font.SysFont(None, 48).render(f'Score: {score}', True, (255, 255, 255))
            level_image = pygame.font.SysFont(None, 48).render(f'Level: {level}', True, (255, 255, 255))
            screen.blit(score_image, (10, 10))
            screen.blit(level_image, (10, 50))  # Display level below score

            # Check if all aliens are defeated
            if not aliens:
                spawn_aliens(ai_settings, screen, aliens, level)  # Spawn new aliens if all are defeated

        else:
            # Show game over message and restart button
            show_game_over(screen, score, restart_button)

        pygame.display.flip()
        clock.tick(60)  # Limit the frame rate to 60 FPS

def spawn_aliens(ai_settings, screen, aliens, level):
    """Spawn aliens in the game."""
    number_of_aliens = level + 4  # Increase the number of aliens based on the level
    for i in range(number_of_aliens):
        alien = Alien(ai_settings, screen)
        alien.rect.x = i * 100
        alien.rect.y = 50
        aliens.add(alien)

def show_game_over(screen, score, restart_button):
    """Display game over message, score, and restart button."""
    screen.fill((0, 0, 0))  # Black background
    font = pygame.font.SysFont(None, 74)
    game_over_surface = font.render('Game Over', True, (255, 0, 0))
    score_surface = font.render(f'Score: {score}', True, (255, 255, 255))

    # Center the text
    screen.blit(game_over_surface, (screen.get_width() // 2 - game_over_surface.get_width() // 2, 100))
    screen.blit(score_surface, (screen.get_width() // 2 - score_surface.get_width() // 2, 200))

    # Draw the restart button
    restart_button.draw_button()  # Draw the restart button on the screen

    pygame.display.flip()

if __name__ == '__main__':
    run_game()

