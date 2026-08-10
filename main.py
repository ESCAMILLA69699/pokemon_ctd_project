from pokemonfunctions import get_pokemon_info, get_pokemon_stats, compare_pokemons, pokemon_battle
from pokemonapi import get_data
from design import topdisplay, pikachu_logo, menuchoices, searching, designstats
import time

def main():
    topdisplay()
    pikachu_logo()


    while True:
        menuchoices()

        user = input("Choose a number to begin with the program: ")

        if user == "1":
            user_choice = input("What Pokemon would you like to choose? ")
            print()

            searching(user_choice)

            designstats(user_choice)
           
            result = get_pokemon_info(user_choice)

            time.sleep(.5)
            print(f"Name: {result["name"]}")
            time.sleep(.5)
            print(f"Height: {result["height"]}")
            time.sleep(.5)
            print(f"Weight: {result["weight"]}")
            time.sleep(.5)
            print(f"Type: {result["type"]}")
            print("#" * 45)

        elif user == "2":
            user_choice = input("What Pokemon would you like to choose? ")
            print()

            

            result = get_pokemon_stats(user_choice)

            searching(user_choice)

            designstats(user_choice)
            print("STATS =")
            print()
            time.sleep(.5)
            print(f"HP: {result["hp"]}")
            time.sleep(.5)
            print(f"Attack: {result["attack"]}")
            time.sleep(.5)
            print(f"Defense: {result["defense"]}")
            print("#" * 45)

        elif user == "3":
            print("Choose 2 Pokemon to compare their stats:")
            print()

            user_choice1 = input("Choose your first Pokemon: ")
            user_choice2 = input("Choose your second Pokemon: ")
            print()


            result = compare_pokemons(user_choice1, user_choice2)

            searching(user_choice1)
            searching(user_choice2)

            designstats(user_choice1)

            time.sleep(.5)
            print(f"HP: {result["pokemon1"]["hp"]}")
            time.sleep(.5)
            print(f"Attack: {result["pokemon1"]["attack"]}")
            time.sleep(.5)
            print(f"Defense: {result["pokemon1"]["defense"]}")
            print("#" * 45)
            print()

            print("VS".center(45))

            print()
            designstats(user_choice2)
            time.sleep(.5)
            print(f"HP: {result["pokemon2"]["hp"]}")
            time.sleep(.5)
            print(f"Attack: {result["pokemon2"]["attack"]}")
            time.sleep(.5)
            print(f"Defense: {result["pokemon2"]["defense"]}")
            time.sleep(.5)
            print("#" * 45)
            print()

            

        elif user == "4":

            print("You will fight against a CPU.")
            user_choice = input("Choose your Pokemon: ")

            print()
            searching(user_choice)
            print()


            print("*" * 45)
            print("BATTLE".center(45))
            
            print()
            
            result = pokemon_battle(user_choice)
            
            
            print(result)

        elif user == "5":
            print("Thank you for playing!")
            break

        else:
            print("Invalid choice. Please choose 1-5.")

main()

## finish the desing for step 4 and 5
# finish requierments and should be done by monday