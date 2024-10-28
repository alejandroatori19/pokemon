import pygame
import sys

class Interface:
    widthScreen = None
    heightScreen = None
    screen = None
    trainer = None
    
    
    # Consts
    colorFont = (255, 255, 255)
    
    # ============================================
    # Constructor of the interface class
    # ============================================
    def __init__ (self, widthS=800, heightS=600):
        self.widthScreen = widthS
        self.heightScreen = heightS
        
        # Init pygame window & prepare it for the game
        self.screen = pygame.display.set_mode((widthS, heightS))
        pygame.display.set_caption("Pokemon Interface")
        
        return
    
    # ==========================================================================================================
    
    def init_graphic_interface_fully (self, background_image_path=None, pokemon1_path=None, pokemon2_path=None):
        self.set_background_image (background_image_path)
        
        # Assume pokemon1 is the player and pokemon2 is the opponent
        if pokemon1_path is not None:
            self.set_pokemon_image (pokemon1_path, enemyPokemon=False)
            self.set_pokemon_information ("Arceus", 100, 100, 100, enemyPokemon=False)
            
        if pokemon2_path is not None:
            self.set_pokemon_image (pokemon2_path, enemyPokemon=True)            
            self.set_pokemon_information ("Arceus", 50, 50, 50, enemyPokemon=True)

        
        
        return
    
    # ============================================
    # Drawers of the interface
    # ============================================
    def set_background_image (self, pathImageBackground=None):
        try:
            background_img = pygame.image.load(pathImageBackground)
            background_img = pygame.transform.scale(background_img, (self.widthScreen, self.heightScreen - int(0.4 * self.heightScreen)))  # Resize if needed
            self.screen.blit(background_img, (0, 0))  # Draw background
         
        except pygame.error as e:
            print(f"Failed to load background image: {e}")
            sys.exit("Error loading background image")
            
        return
    
    # ============================================================================
    
    def set_pokemon_image (self, pathImagePokemon, enemyPokemon=False):
        try:
            pokemonImage = pygame.image.load(pathImagePokemon)
            pokemonImage = pygame.transform.scale(pokemonImage, (120, 120))  # Resize as needed
            
            if enemyPokemon:
                self.screen.blit(pokemonImage, (600, 200))  # Draw background

            else:                
                pokemonImage = pygame.transform.flip(pokemonImage, True, False)  # Flip the image
                self.screen.blit(pokemonImage, (50, 200))  # Draw background  


        except pygame.error as e:
            print(f"Failed to load Pokémon image: {e}")
            sys.exit ("Error loading pokémon images")
            
        return
            
    def set_pokemon_information (self, name, level, hp, max_hp, enemyPokemon=False):
        if enemyPokemon:
            x = 0
            y = 50
        else:
            x = 400
            y = 50
        
        # Draw the rectangle background for Pokémon info
        info_rect = pygame.Rect(x, y, 250, 120)  # Height can be adjusted if needed
        if enemyPokemon:
            pygame.draw.rect(self.screen, (255, 255, 255), info_rect)  # Draw outer rectangle
            
        else:
            pygame.draw.rect(self.screen, (0, 0, 0), info_rect)  # Draw outer rectangle

        # Define a line height to control spacing
        line_height = 20  # Adjust this value for more or less spacing
    """
        # First line: name (align left) and level (align right)
        draw_text(name, font, BLACK, screen, x + 10, y + 10)
        draw_text(f"Lv. {level}", font, BLACK, screen, x + 190, y + 10)  # Right aligned

        # Second line: health bar (align left)
        draw_health_bar(x + 10, y + 40, hp, max_hp)  # Position the health bar

        # Third line: hpNow/totalHP (align left)
        hp_text = f"{hp}/{max_hp}"
        draw_text(hp_text, font, BLACK, screen, x + 10, y + 40 + line_height)  # Align left, adjusted by line height
        return
    """         
    # ============================================
    # Logic behind the interface
    # ============================================
    def update_graphic_interface (self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit ("Closing the program")
                
        pygame.display.flip()  # Update the display
        
        return