import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
ORANGE = (255, 165, 0)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong")

# Set up the paddles
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
paddle_speed = 5
player_paddle = pygame.Rect(50, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
opponent_paddle = pygame.Rect(WIDTH - 50 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)

# Set up the ball
BALL_SIZE = 15
ball_speed_x = 7 * random.choice((1, -1))
ball_speed_y = 7 * random.choice((1, -1))
ball = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)

# Set up scores
player_score = 0
opponent_score = 0
font = pygame.font.Font(None, 36)

# Game loop
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get mouse position
    mouse_pos = pygame.mouse.get_pos()

    # Move player paddle with mouse
    player_paddle.y = mouse_pos[1] - PADDLE_HEIGHT // 2

    # Move the opponent paddle
    if ball.y < opponent_paddle.y + PADDLE_HEIGHT // 2:
        opponent_paddle.y -= paddle_speed
    if ball.y > opponent_paddle.y + PADDLE_HEIGHT // 2:
        opponent_paddle.y += paddle_speed

    # Ball movement
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Ball collision with paddles
    if ball.colliderect(player_paddle) or ball.colliderect(opponent_paddle):
        ball_speed_x *= -1

    # Ball collision with top and bottom walls
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y *= -1

    # Ball out of bounds
    if ball.left <= 0:
        opponent_score += 1
        ball.center = (WIDTH // 2, HEIGHT // 2)
        ball_speed_x *= random.choice((1, -1))

    if ball.right >= WIDTH:
        player_score += 1
        ball.center = (WIDTH // 2, HEIGHT // 2)
        ball_speed_x *= random.choice((1, -1))

    # Draw everything
    screen.fill(BLACK)
    pygame.draw.rect(screen, BLUE, player_paddle)
    pygame.draw.rect(screen, RED, opponent_paddle)
    pygame.draw.ellipse(screen, ORANGE, ball)
    player_text = font.render(f"Player: {player_score}", True, WHITE)
    opponent_text = font.render(f"Opponent: {opponent_score}", True, WHITE)
    screen.blit(player_text, (50, 20))
    screen.blit(opponent_text, (WIDTH - 200, 20))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
