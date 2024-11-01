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
            self.init_pokemon_information ("Arceus", 100, 100, 100, enemyPokemon=False)
            
        if pokemon2_path is not None:
            self.set_pokemon_image (pokemon2_path, enemyPokemon=True)            
            self.init_pokemon_information ("Arceus", 50, 50, 50, enemyPokemon=True)

        
        
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
    
    def init_pokemon_information (self, name, level, hp, max_hp, enemyPokemon=False):
        # Set x and y coordinates of the rectangle that  contains information
        if enemyPokemon:
            xCoordinate = 0
            yCoordinate = 50
            backgroundColor = (255, 255, 255)
        else:
            xCoordinate = 400
            yCoordinate = 50
            backgroundColor = (0, 0, 0)
        
        size = [250, 120]
        
        # Draw the rectangle background for Pokémon info
        info_rect = pygame.Rect(xCoordinate, yCoordinate, size[0], size[1])  
        
        pygame.draw.rect(self.screen, backgroundColor, info_rect)  # Draw outer rectangle

        # Define a line height to control spacing
        line_height = 20  # Adjust this value for more or less spacing
    
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