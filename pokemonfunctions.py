"""
IN THIS FILE POKEMONFUNCTIONS.PY, this is where all the functions are located 
that is used for this project.
"""
from pokemonapi import get_data
import random
import time

## get pokemon basic info like their name, height, weight, and type, hp, stats
# 


# 1. get info of a pokemon (only 1 can be chosen) #// get_pokemon_info(name):
# 2. Get pokemon stats (only 1 can be chosen) #// get_pokemon_stats(name):
# 3. Compare pokemon stats (between 2 pokemons) #// compare_pokemons(name1, name2):
# 4. fight - mini game (Choose 2) or let computer choose like a 1v1 #/ pokemon_battle(name1):
# 5. EXIT

#basic function
## GET A POKEMON NAME
def get_pokemon_name(name):
    pokemon = get_data(name)

    if pokemon is None:
        return None
    else:
        return pokemon["name"]


# User gets a pokemon info
# Try/except for only name and no other things
# Useful for option 1 
def get_pokemon_info(name):
    
    pokemon = get_data(name)
    
    if pokemon is None:
            return None
    else:
           return {
                    "name": pokemon["name"],
                    "height": pokemon["height"],
                    "weight": pokemon["weight"],
                    "type": pokemon["types"][0]["type"]["name"]
}


#print(get_pokemon_info("pikachu"))


## GET STATS OF A POKEMON
## USEFUL FOR OPTION 2
def get_pokemon_stats(name):
     pokemon = get_data(name)

     if pokemon is None:
            return None
     else:
            return {
                    "hp": pokemon["stats"][0]["base_stat"], #hp
                    "attack": pokemon["stats"][1]["base_stat"], #attack
                    "defense": pokemon["stats"][2]["base_stat"] #defense
                }
#print(get_pokemon_stats("pikachu"))

## COMPARE STATS OF A POKEMON 
## USEFUL FOR OPTION 3
def compare_pokemons(name1, name2):
     pokemon1 = get_data(name1)
     pokemon2 = get_data(name2)


     if pokemon1 is None or pokemon2 is None:
            return None
     else:
         return {
                    "pokemon1": get_pokemon_stats(name1),
                    "pokemon2": get_pokemon_stats(name2)
}

#print(compare_pokemons("pikachu", "squirtle"))


## POKEMON BATTLE
## USEFUL FOR OPTION 4
def pokemon_battle(name):
    # User chooses a Pokémon
    pokemon = get_data(name)

    # Computer chooses a random Pokémon
    random_id = random.randint(1, 1025)
    computer_pokemon = get_data(random_id)

    if pokemon is None or computer_pokemon is None:
        return None

    print(f"You chose: {pokemon['name']}")
    print(f"Computer chose: {computer_pokemon['name']}")
    print("*" * 45)
              
    print()

    # Start the battle
    winner = pokemon_rumble(
        pokemon["name"],
        computer_pokemon["name"]
    )

    return winner


def pokemon_rumble(user, computer):
    # Randomize who attacks first
    first = random.choice(["user", "computer"])

    # Get full Pokemon data
    user_pokemon = get_data(user)
    computer_pokemon = get_data(computer)

    if user_pokemon is None or computer_pokemon is None:
        return None

    # Total HP = HP + Defense
    user_hp = (
        user_pokemon["stats"][0]["base_stat"]
        + user_pokemon["stats"][2]["base_stat"]
    )

    computer_hp = (
        computer_pokemon["stats"][0]["base_stat"]
        + computer_pokemon["stats"][2]["base_stat"]
    )

    # Attack stat
    user_attack = user_pokemon["stats"][1]["base_stat"]
    computer_attack = computer_pokemon["stats"][1]["base_stat"]

    print(f"{user_pokemon['name']} HP: {user_hp}")
    print(f"{computer_pokemon['name']} HP: {computer_hp}")
    print("------------")
    print()

    time.sleep(.3)
    print(f"{first} attacks first!")

    while user_hp > 0 and computer_hp > 0:

        if first == "user":

            computer_hp -= user_attack

            time.sleep(.3)
            print(
                f"{user_pokemon['name']} attacks "
                f"{computer_pokemon['name']} for {user_attack} damage!"
            )

            time.sleep(.3)
            print(f"{computer_pokemon['name']} HP: {computer_hp}")

            # Check if computer Pokemon lost
            if computer_hp <= 0:
                time.sleep(.3)
                print(f"{user_pokemon['name']} WON!")
                return user_pokemon["name"]

            user_hp -= computer_attack

            time.sleep(.3)
            print(
                f"{computer_pokemon['name']} attacks "
                f"{user_pokemon['name']} for {computer_attack} damage!"
            )

            time.sleep(.3)
            print(f"{user_pokemon['name']} HP: {user_hp}")

            if user_hp <= 0:
                time.sleep(.3)
                print(f"{computer_pokemon['name']} WON!")
                return computer_pokemon["name"]

        else:

            user_hp -= computer_attack

            time.sleep(.3)
            print(
                f"{computer_pokemon['name']} attacks "
                f"{user_pokemon['name']} for {computer_attack} damage!"
            )

            time.sleep(.3)
            print(f"{user_pokemon['name']} HP: {user_hp}")

            # Check if user Pokemon lost
            if user_hp <= 0:
                time.sleep(.3)
                print(f"{computer_pokemon['name']} WON!")
                return computer_pokemon["name"]

            computer_hp -= user_attack

            time.sleep(.3)
            print(
                f"{user_pokemon['name']} attacks "
                f"{computer_pokemon['name']} for {user_attack} damage!"
            )

            time.sleep(.3)
            print(f"{computer_pokemon['name']} HP: {computer_hp}")

            if computer_hp <= 0:
                time.sleep(.3)
                print(f"{user_pokemon['name']} WON!")
                return user_pokemon["name"]


