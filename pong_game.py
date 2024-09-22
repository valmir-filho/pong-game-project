import pygame
import sys

# Initialize Pygame.
pygame.init()

# Define constants.
WIDTH, HEIGHT = 800, 600
BALL_RADIUS = 15
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create the game window.
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game")

# Set the clock.
clock = pygame.time.Clock()


# Function to draw the ball.
def draw_ball(ball_pos):
    pygame.draw.circle(screen, WHITE, ball_pos, BALL_RADIUS)


# Function to draw paddles.
def draw_paddle(paddle_rect):
    pygame.draw.rect(screen, WHITE, paddle_rect)


# Function to display the score.
def draw_score(left_score, right_score):
    font = pygame.font.Font(None, 74)
    score_text = f"{left_score}  {right_score}"
    text = font.render(score_text, True, WHITE)
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, 20))


# Main game function.
def main():
    ball_pos = [WIDTH // 2, HEIGHT // 2]
    ball_vel = [5, 5]
    
    left_paddle = pygame.Rect(30, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
    right_paddle = pygame.Rect(WIDTH - 40, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)

    left_score = 0
    right_score = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and left_paddle.top > 0:
            left_paddle.y -= 5
        if keys[pygame.K_s] and left_paddle.bottom < HEIGHT:
            left_paddle.y += 5
        if keys[pygame.K_UP] and right_paddle.top > 0:
            right_paddle.y -= 5
        if keys[pygame.K_DOWN] and right_paddle.bottom < HEIGHT:
            right_paddle.y += 5

        # Update ball position.
        ball_pos[0] += ball_vel[0]
        ball_pos[1] += ball_vel[1]

        # Check for collisions with the walls.
        if ball_pos[1] <= BALL_RADIUS or ball_pos[1] >= HEIGHT - BALL_RADIUS:
            ball_vel[1] = -ball_vel[1]
        
        # Check for collisions with paddles.
        if left_paddle.collidepoint(ball_pos[0] - BALL_RADIUS, ball_pos[1]):
            ball_vel[0] = -ball_vel[0]
        if right_paddle.collidepoint(ball_pos[0] + BALL_RADIUS, ball_pos[1]):
            ball_vel[0] = -ball_vel[0]

        # Check if the ball goes out of bounds.
        if ball_pos[0] < 0:
            right_score += 1
            ball_pos = [WIDTH // 2, HEIGHT // 2]
            ball_vel = [5, 5]
        elif ball_pos[0] > WIDTH:
            left_score += 1
            ball_pos = [WIDTH // 2, HEIGHT // 2]
            ball_vel = [-5, 5]

        # Clear the screen.
        screen.fill(BLACK)

        # Draw the ball and paddles.
        draw_ball(ball_pos)
        draw_paddle(left_paddle)
        draw_paddle(right_paddle)

        # Draw the score.
        draw_score(left_score, right_score)

        # Update the display.
        pygame.display.flip()
        clock.tick(60)

# Run the game.
if __name__ == "__main__":
    main()
