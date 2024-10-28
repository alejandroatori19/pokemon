from constants import *
from pokemon import Pokemon
from movement import Movement
import time

def create_movements(movements_dict):
    movement_objects = []
    
    for name, details in movements_dict.items():
        # Extracting each detail from the dictionary
        descriptionM = details["description"]
        powerM = details["power"] if details["power"] is not None else 0  # Default to 0 if no power
        accuracyM = details["accuracy"] if details["accuracy"] is not None else 100  # Default to 100 if none
        typeM = details["type"]
        categoryM = details["category"]
        powerPointsM = details["pp"]
        priorityM = details.get("priority", 0)  # Default to 0 if no priority field

        # Creating the movement object
        movement = Movement(
            nameM=name,
            descriptionM=descriptionM,
            powerM=powerM,
            accuracyM=accuracyM,
            typeM=typeM,
            categoryM=categoryM,
            powerPointsM=powerPointsM,
            priorityM=priorityM
        )
        
        # Adding the created object to the list
        movement_objects.append(movement)
    
    return movement_objects

def fill_pokemon_class():
    data = arceus_data
    
    name = data["name"]
    alias = "Test"  # You could set an alias if needed, for now it's set to None
    id = data["id"]
    pokedexNumber = data["pokedex_number"]
    type_ = data["type"]
    ability = data["ability"]
    level = data["level"]
    status = data.get("status", "Alive")  # Defaults to "Alive" if not provided
    movements = create_movements (data["movements"])  # We'll assume the movements are fine as-is
    baseStats = data["base_stats"]
    ivsPokemon = data["stats"]  # Assuming "stats" are the IVs for this specific Pokémon
    evsPokemon = None  # You can include EVs if they are part of the data, but it's not provided here

    # Create an instance of Pokemon
    pokemon_instance = Pokemon(
        name=name,
        alias=alias,
        id=id,
        pokedexNumber=pokedexNumber,
        type=type_,
        ability=ability,
        level=level,
        status=status,
        movements=movements,
        baseStats=baseStats,
        ivsPokemon=ivsPokemon,
        evsPokemon=evsPokemon
    )
    
    return pokemon_instance

pokemon1 = fill_pokemon_class ()

pokemon1.show_pokemon_information ()


    
    

    

