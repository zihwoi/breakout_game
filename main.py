# main.py

import pygame
import sys
from settings import WIDTH, HEIGHT, FPS, BLACK
from game import Paddle, Ball

# Initialize Pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Breakout Game')

# Clock for controlling the frame rate
clock = pygame.time.Clock()

# Create game objects
paddle = Paddle()
ball = Ball()

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the keys pressed for paddle movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        paddle.move("left")
    if keys[pygame.K_RIGHT]:
        paddle.move("right")

    # Move the ball
    ball.move()

    # Check for ball collision with the paddle
    if ball.y + ball.radius >= paddle.rect.y and paddle.rect.collidepoint(ball.x, ball.y):
        ball.bounce()

    # Reset ball if it goes below the screen
    if ball.y - ball.radius > HEIGHT:
        ball.reset()

    # Fill the screen with black
    screen.fill(BLACK)

    # Draw everything
    paddle.draw(screen)
    ball.draw(screen)

    # Update the display
    pygame.display.flip()

    # Maintain the frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
sys.exit()

