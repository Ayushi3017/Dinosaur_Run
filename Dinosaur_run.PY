import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dino Run")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (240, 240, 240)
GREEN = (100, 200, 100)
RED = (255, 50, 50)
DARK_GRAY = (50, 50, 50)

# Fonts
font_small = pygame.font.SysFont('Arial', 24, bold=True)
font_medium = pygame.font.SysFont('Arial', 32, bold=True)
font_large = pygame.font.SysFont('Arial', 48, bold=True)

# Clock
clock = pygame.time.Clock()
FPS = 60

# Create sprite graphics (same as before)
def create_dino_run1():
    surface = pygame.Surface((60, 80), pygame.SRCALPHA)
    pygame.draw.rect(surface, WHITE, (20, 30, 40, 50))
    pygame.draw.rect(surface, WHITE, (20, 70, 15, 10))
    pygame.draw.rect(surface, WHITE, (45, 70, 15, 10))
    pygame.draw.rect(surface, WHITE, (50, 20, 20, 20))
    pygame.draw.rect(surface, BLACK, (60, 25, 5, 5))
    return surface

def create_dino_run2():
    surface = pygame.Surface((60, 80), pygame.SRCALPHA)
    pygame.draw.rect(surface, WHITE, (20, 30, 40, 50))
    pygame.draw.rect(surface, WHITE, (25, 70, 15, 10))
    pygame.draw.rect(surface, WHITE, (40, 70, 15, 10))
    pygame.draw.rect(surface, WHITE, (50, 20, 20, 20))
    pygame.draw.rect(surface, BLACK, (60, 25, 5, 5))
    return surface

def create_dino_jump():
    surface = pygame.Surface((60, 80), pygame.SRCALPHA)
    pygame.draw.rect(surface, WHITE, (20, 20, 40, 60))
    pygame.draw.rect(surface, WHITE, (30, 70, 20, 10))
    pygame.draw.rect(surface, WHITE, (50, 10, 20, 20))
    pygame.draw.rect(surface, BLACK, (60, 15, 5, 5))
    return surface

def create_cactus1():
    surface = pygame.Surface((40, 70), pygame.SRCALPHA)
    pygame.draw.rect(surface, GREEN, (15, 20, 10, 50))
    pygame.draw.rect(surface, GREEN, (5, 30, 10, 10))
    pygame.draw.rect(surface, GREEN, (25, 40, 10, 10))
    return surface

def create_cactus2():
    surface = pygame.Surface((50, 60), pygame.SRCALPHA)
    pygame.draw.rect(surface, GREEN, (10, 30, 10, 30))
    pygame.draw.rect(surface, GREEN, (30, 20, 10, 40))
    return surface

def create_cactus3():
    surface = pygame.Surface((60, 50), pygame.SRCALPHA)
    pygame.draw.rect(surface, GREEN, (10, 30, 10, 20))
    pygame.draw.rect(surface, GREEN, (25, 20, 10, 30))
    pygame.draw.rect(surface, GREEN, (40, 25, 10, 25))
    return surface

# Game objects
dino_run1 = create_dino_run1()
dino_run2 = create_dino_run2()
dino_jump = create_dino_jump()
cactus_imgs = [create_cactus1(), create_cactus2(), create_cactus3()]

# Game state
class GameState:
    def __init__(self):
        self.reset()
        
    def reset(self):
        self.dino_x = 50
        self.dino_y = HEIGHT - 80 - 50
        self.dino_velocity_y = 0
        self.is_jumping = False
        self.animation_count = 0
        self.cactus_x = WIDTH
        self.cactus_y = HEIGHT - 70 - 50
        self.cactus_speed = 6
        self.score = 0
        self.high_score = 0
        self.game_active = True

game = GameState()

def draw_scoreboard():
    # Scoreboard background
    scoreboard_rect = pygame.Rect(10, 10, 250, 80)
    pygame.draw.rect(screen, DARK_GRAY, scoreboard_rect, border_radius=10)
    pygame.draw.rect(screen, WHITE, scoreboard_rect, 2, border_radius=10)
    
    # Score text
    score_text = font_medium.render(f"SCORE: {game.score}", True, WHITE)
    high_score_text = font_medium.render(f"HIGH: {game.high_score}", True, WHITE)
    
    screen.blit(score_text, (20, 20))
    screen.blit(high_score_text, (20, 50))

def draw_dino(x, y):
    game.animation_count += 1
    if game.is_jumping:
        screen.blit(dino_jump, (x, y))
    else:
        if game.animation_count % 20 < 10:
            screen.blit(dino_run1, (x, y))
        else:
            screen.blit(dino_run2, (x, y))

def draw_cactus(x, y):
    cactus_img = random.choice(cactus_imgs)
    screen.blit(cactus_img, (x, y))

def draw_ground():
    pygame.draw.rect(screen, GRAY, (0, HEIGHT - 70, WIDTH, 70))
    for i in range(0, WIDTH, 40):
        pygame.draw.rect(screen, BLACK, (i, HEIGHT - 50, 20, 2))

def draw_game_over():
    # Dark overlay
    overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 180))
    screen.blit(overlay, (0, 0))
    
    # Game over text
    game_over_text = font_large.render("GAME OVER", True, RED)
    final_score_text = font_medium.render(f"Final Score: {game.score}", True, WHITE)
    high_score_text = font_medium.render(f"High Score: {game.high_score}", True, WHITE)
    restart_text = font_small.render("Press SPACE to restart", True, WHITE)
    
    screen.blit(game_over_text, (WIDTH//2 - game_over_text.get_width()//2, HEIGHT//2 - 70))
    screen.blit(final_score_text, (WIDTH//2 - final_score_text.get_width()//2, HEIGHT//2 - 20))
    screen.blit(high_score_text, (WIDTH//2 - high_score_text.get_width()//2, HEIGHT//2 + 20))
    screen.blit(restart_text, (WIDTH//2 - restart_text.get_width()//2, HEIGHT//2 + 70))

# Main game loop
running = True
while running:
    screen.fill(BLACK)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if game.game_active and not game.is_jumping:
                    game.dino_velocity_y = -15
                    game.is_jumping = True
                elif not game.game_active:
                    game.reset()
    
    if game.game_active:
        # Dino physics
        game.dino_y += game.dino_velocity_y
        game.dino_velocity_y += 0.8
        if game.dino_y >= HEIGHT - 80 - 50:
            game.dino_y = HEIGHT - 80 - 50
            game.is_jumping = False

        # Move cactus
        game.cactus_x -= game.cactus_speed
        if game.cactus_x < -60:
            game.cactus_x = WIDTH + random.randint(200, 400)
            game.score += 1
            game.cactus_speed = 6 + game.score // 10

        # Collision detection
        dino_rect = pygame.Rect(game.dino_x + 10, game.dino_y + 10, 40, 60)
        cactus_rect = pygame.Rect(game.cactus_x + 5, game.cactus_y + 5, 30, 60)
        
        if dino_rect.colliderect(cactus_rect):
            game.high_score = max(game.high_score, game.score)
            game.game_active = False

    # Draw everything
    draw_ground()
    draw_dino(game.dino_x, game.dino_y)
    
    if game.game_active:
        draw_cactus(game.cactus_x, game.cactus_y)
    
    # Always show scoreboard (even during game over)
    draw_scoreboard()
    
    if not game.game_active:
        draw_game_over()

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
sys.exit()