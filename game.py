import pygame
import random
import sys
import time

#Ziad
#=====================================================================






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