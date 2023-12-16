import pygame
import random
import sys
import time

#Ziad
#=====================================================================

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Collect the Falling Apples")

# Player settings
PLAYER_WIDTH, PLAYER_HEIGHT = 100, 100
player_image = pygame.image.load('./basket.png')  # Load the basket image
player_image = pygame.transform.scale(player_image, (PLAYER_WIDTH, PLAYER_HEIGHT))
# Center the player x
player_x = (WIDTH - PLAYER_WIDTH) // 2
# Bottom but up a little
player_y = HEIGHT - PLAYER_HEIGHT - 20
player_speed = 10

#Abdullah
#=====================================================================


# Object settings
APPLE_WIDTH, APPLE_HEIGHT = 60, 60
apple_image = pygame.image.load('./apple.png')
apple_image = pygame.transform.scale(apple_image, (APPLE_WIDTH, APPLE_HEIGHT))
# Random x
apple_x = random.randint(0, WIDTH - APPLE_WIDTH)
# Just above the screen to come down
apple_y = -APPLE_HEIGHT
apple_speed = 8

# Grass background
grass_background = pygame.image.load('grass.png')
grass_background = pygame.transform.scale(grass_background, (WIDTH, HEIGHT))

# Clock
clock = pygame.time.Clock()

# Score
score = 0
missed_apples = 0

# Show introduction screen
WINDOW.fill((0, 180, 0))  # Green background
font = pygame.font.Font(None, 72)
intro_text = font.render("Collect the Falling Apples", True, (200, 0, 0))
WINDOW.blit(intro_text, ((WIDTH - intro_text.get_width()) // 2, (HEIGHT - intro_text.get_height()) // 2))
pygame.display.update()
time.sleep(1)

# Reset clock for accurate timing
clock.tick() 
#mazen
#===================================================================== 
#yehia
#=====================================================================
#Abdelrahman
#=====================================================================
 player_rect = pygame.Rect(player_x, player_y, PLAYER_WIDTH, PLAYER_HEIGHT)
    apple_rect = pygame.Rect(apple_x, apple_y, APPLE_WIDTH, APPLE_HEIGHT)

    if player_rect.colliderect(apple_rect):
        apple_x = random.randint(0, WIDTH - APPLE_WIDTH)
        apple_y = -APPLE_HEIGHT
        score += 1

    WINDOW.blit(grass_background, (0, 0))
    WINDOW.blit(player_image, (player_x, player_y))
    WINDOW.blit(apple_image, (apple_x, apple_y))

    font = pygame.font.Font(None, 36)
    score_text = font.render(f'Score: {score}', True, (255, 255, 255))
    missed_text = font.render(f'Missed: {missed_apples}', True, (255, 255, 255))
    WINDOW.blit(score_text, (10, 10))
    WINDOW.blit(missed_text, (10, 50))

    pygame.display.update()
    clock.tick(80)

