


# Constants
MAX_POKEMON_PER_TEAM = 6
MAX_IVS = 15
MAX_EVS = 252
LIMIT_TOTAL_EV_PER_POKEMON = 510

MAX_LEVEL_POKEMON = 100
# Lists of data

genrePokemon = ["Male", "Female", "Sexless"]

# Naturalezas 
naturePokemon = ["Adamant",         #  Increased Attack, Decreased Special Attack
                     "Bashful",         #  No stat modifications
                     "Bold",            #  Increased Defense, Decreased Attack
                     "Brave",           #  Increased Attack, Decreased Speed
                     "Calm",            #  Increased Special Defense, Decreased Attack
                     "Careful",         #  Increased Special Defense, Decreased Special Attack
                     "Docile",          #  No stat modifications
                     "Gentle",          #  Increased Special Defense, Decreased Defense
                     "Hardy",           #  No stat modifications
                     "Hasty",           #  Increased Speed, Decreased Defense
                     "Impish",          #  Increased Defense, Decreased Special Attack
                     "Jolly",           #  Increased Speed, Decreased Special Attack
                     "Lax",             #  Increased Defense, Decreased Special Defense
                     "Lonely",          #  Increased Attack, Decreased Defense
                     "Mild",            #  Increased Special Attack, Decreased Defense
                     "Modest",          #  Increased Special Attack, Decreased Attack
                     "Naive",           #  Increased Speed, Decreased Special Defense
                     "Naughty",         #  Increased Attack, Decreased Special Defense
                     "Quiet",           #  Increased Special Attack, Decreased Speed
                     "Quirky",          #  No stat modifications
                     "Rash",            #  Increased Special Attack, Decreased Special Defense
                     "Relaxed",         #  Increased Defense, Decreased Speed
                     "Sassy",           #  Increased Special Defense, Decreased Speed
                     "Serious",         #  No stat modifications
                     "Timid"            #  Increased Speed, Decreased Attack
                     ]               

statusPokemon = ["Healthy",             # No status condition.
                 "Poisoned",            # Gradual HP loss.
                 "Badly Poisoned",      # Increasingly severe poison, more damaging than regular poison.
                 "Paralyzed",           # May prevent the Pokémon from attacking.
                 "Burned",              # Inflicts damage over time and may reduce Attack.
                 "Frozen",              # Renders the Pokémon unable to move.
                 "Asleep",              # Renders the Pokémon unable to move for a few turns.
                 "Confused",            # May cause a Pokémon to hurt itself in its confusion.
                 "Fainted"              # The Pokémon has lost all its HP and cannot battle.
                 ]

# They are by index
typePokemon = ["Normal",         # 0         
               "Fire",           # 1
               "Water",          # 2
               "Electric", 
               "Grass",          # 4
               "Ice",            # 5
               "Fighting",       # 6
               "Poison", 
               "Ground", 
               "Flying",         # 9
               "Psychic",        # 10
               "Bug",            # 11
               "Rock",
               "Ghost",
               "Dragon",         # 14
               "Dark",           # 15
               "Steel",          # 16
               "Fairy"           # 17
               ]



typePokedexPokemon = [[4, 7], 
                      [4, 7], 
                      [4, 7], 
                      [1],
                      [1],
                      [1, 9],
                      [2],
                      [2],
                      [2]
                      
                      
                      
                      ]

pokedexPokemon = ["Bulbasaur", 
                  "Ivysaur", 
                  "Venusaur", 
                  "Charmander", 
                  "Charmeleon", 
                  "Charizard", 
                  "Squirtle",
                  "Wartortle", 
                  "Blastoise"
                  
                  
                  
                  ]