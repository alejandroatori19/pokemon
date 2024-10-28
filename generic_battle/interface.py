import pygame
import sys

class Interface:
    widthScreen = None
    heightScreen = None
    screen = None
    trainer = None
    
    
    # Consts
    typeFont = None
    colorFont = (255, 255, 255)
    backgroundInformation = (144, 238, 144)
    
    # ============================================
    # Constructor of the interface class
    # ============================================
    def __init__ (self, widthS=800, heightS=600):
        self.widthScreen = widthS
        self.heightScreen = heightS
        
        # Init pygame window & prepare it for the game
        pygame.init ()
        self.screen = pygame.display.set_mode((widthS, heightS))
        pygame.display.set_caption("Pokemon Interface")
        
        self.typeFont = pygame.font.Font(None, 25)      # Default arial

        
        return
    
    # ==========================================================================================================
    
    def init_graphic_interface_fully (self, background_image_path=None, pokemon1_path=None, pokemon2_path=None):
        self.init_background_image (background_image_path)
        
        # Assume pokemon1 is the player and pokemon2 is the opponent
        if pokemon1_path is not None:
            self.init_pokemon_image (pokemon1_path, enemyPokemon=False)
            self.init_pokemon_information ("Arceus", 100, 100, 100, enemyPokemon=False)
            
        if pokemon2_path is not None:
            self.init_pokemon_image (pokemon2_path, enemyPokemon=True)            
            self.init_pokemon_information ("Arceus", 50, 50, 50, enemyPokemon=True)

        
        
        return
    
    # ============================================
    # Drawers of the interface
    # ============================================
    def init_background_image (self, pathImageBackground=None):
        try:
            background_img = pygame.image.load(pathImageBackground)
            background_img = pygame.transform.scale(background_img, (self.widthScreen, self.heightScreen - int(0.4 * self.heightScreen)))  # Resize if needed
            self.screen.blit(background_img, (0, 0))  # Draw background
         
        except pygame.error as e:
            print(f"Failed to load background image: {e}")
            sys.exit("Error loading background image")
            
        return
    
    # ============================================================================
    
    def init_pokemon_image (self, pathImagePokemon, enemyPokemon=False):
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
    
    def init_pokemon_information (self, name, level, hp, max_hp, enemyPokemon=False):
        # Set x and y coordinates of the rectangle that  contains information
        if enemyPokemon:
            xCoordinate = 20
            yCoordinate = 50
        else:
            xCoordinate = 530
            yCoordinate = 50
        
        size = [250, 100]
        
        # Draw the rectangle background for Pokémon info
        rectangleInformation = pygame.Rect(xCoordinate, yCoordinate, size[0], size[1])  
        
        pygame.draw.rect(self.screen, self.backgroundInformation, rectangleInformation)  # Draw outer rectangle

        # Define a line height to control spacing
        spacing = 30  # Adjust this value for more or less spacing
        
        # Draw level
        self.draw_text(name, xCoordinate + 10, yCoordinate + 10)
        self.draw_text (f"Lv. {level}", xCoordinate + 150, yCoordinate + 10)
        
        # Second line: health bar (align left)
        self.draw_health_bar(xCoordinate + 10, yCoordinate + 10 + spacing, hp, max_hp)  
        
        self.draw_text (f"HP: {hp}/{max_hp}", xCoordinate + 10, yCoordinate + 10 + spacing*2)
    
        return
    
        
    # ============================================
    # Draw text, set pokemon image, etc. Things will be repeated while the game is running
    # ============================================
    def draw_text (self, text, xCoordinate, yCoordinate):

        textObject = self.typeFont.render(text, True, self.colorFont)
        self.screen.blit(textObject, (xCoordinate, yCoordinate))
        return
    
    # ===============================================================
    
    def draw_health_bar (self, xCoordinate, yCoordinate, hp, max_hp):
        # Draw background (max HP)
        pygame.draw.rect(self.screen, (255, 0, 0), (xCoordinate, yCoordinate, 200, 20))
        # Calculate health proportion
        hpRatio = hp / max_hp
        # Draw current health
        pygame.draw.rect(self.screen, (0, 255, 0), (xCoordinate, yCoordinate, 200 * hpRatio, 20))
        return
        
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