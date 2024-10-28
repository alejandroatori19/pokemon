import pygame

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Screen setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pokemon Battle")

# Load Images
pokemon_image_path = r"C:\Users\Usuario\Desktop\pokemon\generic_battle\images\arceus.png"
background_image_path = r"C:\Users\Usuario\Desktop\pokemon\generic_battle\images\background.png"

# Load player and opponent Pokémon image (same image for both)
try:
    pokemon_img = pygame.image.load(pokemon_image_path)
    pokemon_img = pygame.transform.scale(pokemon_img, (100, 100))  # Resize as needed
except pygame.error as e:
    print(f"Failed to load Pokémon image: {e}")
    pokemon_img = pygame.Surface((100, 100))
    pokemon_img.fill((255, 182, 193))  # Pink placeholder if loading fails

# Load background image
try:
    background_img = pygame.image.load(background_image_path)
    background_img = pygame.transform.scale(background_img, (SCREEN_WIDTH, SCREEN_HEIGHT))  # Resize if needed
except pygame.error as e:
    print(f"Failed to load background image: {e}")
    background_img = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    background_img.fill((144, 238, 144))  # Light green as a fallback

# Define Fonts
font = pygame.font.Font(None, 30)

def draw_health_bar(x, y, hp, max_hp, width=200, height=20):
    # Draw background (max HP)
    pygame.draw.rect(screen, RED, (x, y, width, height))
    # Calculate health proportion
    hp_ratio = hp / max_hp
    # Draw current health
    pygame.draw.rect(screen, GREEN, (x, y, width * hp_ratio, height))

def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    surface.blit(text_obj, (x, y))

def draw_pokemon_info(x, y, name, level, hp, max_hp):
    # Draw the rectangle background for Pokémon info
    info_rect = pygame.Rect(x, y, 250, 120)  # Height can be adjusted if needed
    pygame.draw.rect(screen, WHITE, info_rect)  # Draw outer rectangle

    # Define a line height to control spacing
    line_height = 20  # Adjust this value for more or less spacing

    # First line: name (align left) and level (align right)
    draw_text(name, font, BLACK, screen, x + 10, y + 10)
    draw_text(f"Lv. {level}", font, BLACK, screen, x + 190, y + 10)  # Right aligned

    # Second line: health bar (align left)
    draw_health_bar(x + 10, y + 40, hp, max_hp)  # Position the health bar

    # Third line: hpNow/totalHP (align left)
    hp_text = f"{hp}/{max_hp}"
    draw_text(hp_text, font, BLACK, screen, x + 10, y + 40 + line_height)  # Align left, adjusted by line height


def draw_interface():
    screen.blit(background_img, (0, 0))  # Draw background

    # Draw player Pokémon
    screen.blit(pokemon_img, (150, 300))  # Player Pokémon position
    draw_pokemon_info(0, 400, "Whiscash", 37, 134, 134)  # Pokémon info rectangle with health

    # Draw opponent Pokémon
    screen.blit(pokemon_img, (500, 350))  # Opponent Pokémon position
    draw_pokemon_info(550, 50, "Staravia", 33, 33, 33)  # Opponent info rectangle with health

    # Draw action buttons
    button_width, button_height = 150, 40
    actions = ["Battle", "Pokémon", "Bag", "Run"]
    
    for i, action in enumerate(actions):
        pygame.draw.rect(screen, BLACK, (SCREEN_WIDTH - button_width - 20, 200 + i * (button_height + 10), button_width, button_height))
        draw_text(action, font, WHITE, screen, SCREEN_WIDTH - button_width - 10, 200 + i * (button_height + 10) + 5)  # Center text

def main():
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        draw_interface()  # Call to draw the interface
        pygame.display.flip()  # Update the display

    pygame.quit()

if __name__ == "__main__":
    main()
