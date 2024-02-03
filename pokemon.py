import permanentData as const









class pokemon ():
     # Atributos de la clase
     pokemonName = None            # Nombre original del pokemon (Por ejemplo: 'Arceus')
     pokemonNumberPokdex = None    # Numero de pokedex del pokemon
     pokemonID = None              # Id del pokemon (Es un código unico del pokemon)
     pokemonNickname = None        # Mote del pokemon
     pokemonType = None            # Tipo del pokemon                                          
     pokemonHability = None        # Habilidad del pokemon                                     
     pokemonNature = None          # Naturaleza del pokemon 
     pokemonLevel = None           # Level del pokemon
     pokemonGenre = None          # Genero del pokemon

     # IVs / EVs
     pokemonIVsList = []
     pokemonEVsList = []

     # Después de capturarlo
     pokemonObject = None          # Objeto que lleva el pokemon

     # Constructor de la clase
     def __init__ (self, pokNumberPokdex, pokID, pokNickName, pokHability, pokNature, pokLevel, pokGenre):
          
          # Asignaciones primarias al pokemon generado/capturado
          self.pokemonNumberPokdex = pokNumberPokdex - 1                                       # int
          self.pokemonID = pokID                                                               # Int
          self.pokemonNickname = pokNickName                                                   # String
          self.pokemonType = const.typePokedexPokemon [self.pokemonNumberPokdex]               # List          
          self.pokemonHability = pokHability                                                   # String (El nombre de la habilidad) # FURUTO ID HABILIDAD
          self.pokemonNature = pokNature                                                       # int (id de la naturaleza)
          self.pokemonLevel =  pokLevel                                                        # Int (Nivel del pokemon)
          self.pokemonGenre = const.genrePokemon [pokGenre]                                    # Int 

          # Asignacion de IV




          return

     # Destructor de la clase     
     def __del__ (self):


          return
     
     def print_data_pokemon (self):

          print ("\n--------------- POKEMON DATA ---------------")
          
          print ("Name:", const.pokedexPokemon[self.pokemonNumberPokdex]) 
          print ("ID Pokedex:", self.pokemonNumberPokdex)
          print ("ID Pokemon:", self.pokemonID)
          print ("Nickname:", self.pokemonNickname)
          self.print_pokemon_type ()
          print ("Hability:", self.pokemonHability) 
          print ("Nature:", const.naturePokemon[self.pokemonNature]) 
          print ("Level:", self.pokemonLevel) 
          print ("Gender:", self.pokemonGenre) 

          print ("------------- END POKEMON DATA -------------\n")

          return
     
     def print_pokemon_type (self):
          # Como puede tener 1 o 2 tipos entonces habrá que hacerlo de esta manera para quedarlo bien
          for typePok in self.pokemonType:
               if (len (self.pokemonType) == 2):
                    # Primer tipo del pokemon
                    if typePok == self.pokemonType[0]:
                         print ("Types: " + const.typePokemon [typePok], end = " - ")

                    # Segundo tipo del pokemon
                    else:
                         print (const.typePokemon [typePok])
               
               # Si solo tiene un tipo imprime ese mensaje
               else:
                    print ("Type:", const.typePokemon [typePok])

          return