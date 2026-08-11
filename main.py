from pokemonfunctions import get_pokemon_info, get_pokemon_stats, compare_pokemons, pokemon_battle
from pokemonapi import get_data
from design import topdisplay, pikachu_logo, menuchoices, searching, designstats, goback
import time

def main():
    topdisplay()
    pikachu_logo()
    print("Hello trainer! You have 5 choices to interact with.")
    print("You will be ask to choose a number in order to interact with the game.")
    print("Choose wisely ;)")
    print()
    
    


    while True:
        print()
        menuchoices()

        user = input("Choose a number: ")

        # CLARIFYING DONE
        if user == "1":
            print("---------Choose only ONE pokemon to get its information---------".center(45))
            print()

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


            input("\nPress Enter to return to the main menu:")
            

        #CLARIFYING DONE
        elif user == "2":
            print("---------Choose only ONE pokemon to get its stats---------".center(45))
            print()

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

            input("\nPress Enter to return to the main menu:")

        # CLARIFYING DONE
        elif user == "3":
            print("---------Choose only TWO pokemons to get their stats---------".center(45))
            print()

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

            input("\nPress Enter to return to the main menu:")
            
        # CLARIFYING DONE
        elif user == "4":
            print("---------Choose only ONE pokemon---------".center(45))
            print()

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

            input("\nPress Enter to return to the main menu:")

        elif user == "5":
            print("Thank you for playing!")
            pikachu_logo()
            break

        else:
            print("Invalid choice. Please choose 1-5.")

main()

#layout is good -- 
# Tuesday: -- 
# for number 5 be descriptive regarding how this game is played  -- 
# fix the going back aspect, a bit sloppy -- 

# Wednesday:
# fix the diff unit cases that can be encountered from steps 1- 4
# tidy up extra spaces and indents
# fix stats, info style like {pokemon}'s info and vice versa 1 - 3
# tify up the goodbye section
# i feel that function goback can be deleted
# Ready to be deployed