



class Pokemon:
    
    # ============================================
    # Attributes of the Pokemon class
    # ============================================
    namePokemon = None
    aliasPokemon = None
    idPokemon = None
    pokedexNumberPokemon = None
    typePokemon = None
    abilityPokemon = None
    levelPokemon = None
    statusPokemon = None                # These value determine if the pokemon is alive o defeated
    hpPokemon = None
    
    movementsPokemon = None
    statsPokemon = None
    ivsPokemon = None
    evsPokemon = None
    
    def __init__(self, name, alias, id, pokedexNumber, type, ability, level, status="Alive", movements=[], baseStats=None, ivsPokemon=None, evsPokemon=None):
        self.namePokemon = name
        self.aliasPokemon = alias
        self.idPokemon = id
        self.pokedexNumberPokemon = pokedexNumber
        self.typePokemon = type
        self.abilityPokemon = ability
        self.levelPokemon = level
        self.statusPokemon = status
        
        # If there is no parameter for movements it will be initialized as an empty list
        self.movementsPokemon = movements
        
        # If stats is None, it will be initialized as a dictionary with random values (Default loaded from constants.py)
        self.baseStatsPokemon = baseStats       # The same for the same pokemon (All pikachus have the same base stats)
        self.ivsPokemon = ivsPokemon            # It´s generated randomly between (0-31) for each stat
        self.evsPokemon = evsPokemon            # It´s obtained by fighting with the pokemon (0-252)
        
        return
    
    # ============================================
    # Printers of information
    # ============================================
    def show_pokemon_information (self):
        print (f"----- {self.aliasPokemon} INFO -----")
        print (f"Name: {self.namePokemon}")
        print (f"Id: {self.idPokemon}")
        print (f"Pokedex Number: {self.pokedexNumberPokemon}")        
        print (f"Type: {', '.join(self.typePokemon)}")        
        print (f"Ability: {self.abilityPokemon}")
        print (f"Level: {self.levelPokemon}")
        print (f"Status: {self.statusPokemon}")

        print ("Movements:")
        for movement in self.movementsPokemon:
            print(f"- {movement.get_movementName()} ({movement.get_movementType()}, {movement.get_movementCategory()}) - "
                  f"Power: {movement.get_movementPower()}, Accuracy: {movement.get_accuracyMovement()}, "
                  f"PP: {movement.get_movementPowerPoints()}, Priority: {movement.get_movementPriority()}"
                  )

        return
    
    
    # ============================================
    # Getters of the attributes
    # ============================================
    def get_namePokemon (self):
        return self.namePokemon
    
    def get_aliasPokemon (self):
        return self.aliasPokemon
    
    def get_idPokemon (self):
        return self.idPokemon
    
    def get_pokedexNumberPokemon (self):    
        return self.pokedexNumberPokemon
    
    def get_typePokemon (self):
        return self.typePokemon
    
    def get_abilityPokemon (self):
        return self.abilityPokemon
    
    def get_levelPokemon (self):
        return self.levelPokemon
    
    def get_statusPokemon (self):
        return self.statusPokemon
    
    def get_movementsPokemon (self):
        return self.movementsPokemon
    
    def get_statsPokemon (self):
        return self.statsPokemon    
    
    # ============================================
    # Setters of the attributes (Only a few of them can be modified)
    # ============================================
    def set_statusPokemon (self, newStatus):
        self.statusPokemon = newStatus
        return
    
    def set_hpPokemon (self):
        #finalHP = 2 * self.baseStatsPokemon.get ()
        return
    