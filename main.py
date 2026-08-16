from pokemonfunctions import get_pokemon_info, get_pokemon_stats, compare_pokemons, pokemon_battle
from pokemonapi import get_data
from design import topdisplay, pikachu_logo, menuchoices, searching, designstats, rules, outputtop
import time


outputtop()

def main():
   

    while True:
        print()
        menuchoices()


        try:
            user = int(input("Choose a number: "))

            if user < 1 or user > 5:
                print()
                print("Choose ONLY numbers from 1 through 5: ")
                continue

        except ValueError as e:
            print()
            print(f"ERROR: {e}")
            print("Choose ONLY numbers from 1 through 5: " )
            continue


        # CLARIFYING DONE
        
        if user == 1:
            while True:
                print("---------Choose only ONE pokemon to get its information---------".center(45))
                print()

                user_choice = input("What Pokemon would you like to choose? ")
                print()

                result = get_pokemon_info(user_choice)

                if searching(user_choice, result) == False:
                    print()
                    continue

                
                designstats(user_choice)
           

                time.sleep(.5)
                print("----INFORMATION----".center(45))
                print()
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
                break
            

        #CLARIFYING DONE
        elif user == 2:
            while True:

                print("---------Choose only ONE pokemon to get its stats---------".center(45))
                print()

                user_choice = input("What Pokemon would you like to choose? ")
                print()

            

                result = get_pokemon_stats(user_choice)

                if searching(user_choice, result) == False:
                    print()
                    continue

                designstats(user_choice)
                print("----STATS----".center(45))
                print()
                time.sleep(.5)
                print(f"HP: {result["hp"]}")
                time.sleep(.5)
                print(f"Attack: {result["attack"]}")
                time.sleep(.5)
                print(f"Defense: {result["defense"]}")
                print("#" * 45)

                input("\nPress Enter to return to the main menu:")
                break

        # CLARIFYING DONE
        elif user == 3:
            while True:

                print("---------Choose only TWO pokemons to get their stats---------".center(45))
                print()

                print("Choose 2 Pokemon to compare their stats:")
                print()

                user_choice1 = input("Choose your first Pokemon: ")
                user_choice2 = input("Choose your second Pokemon: ")
                print()


                result = compare_pokemons(user_choice1, user_choice2)

                if searching(user_choice1, result) == False:
                     print()
                     continue

                if searching(user_choice2, result) == False:
                     print()
                     continue

                designstats(user_choice1)

                time.sleep(.5)
                print("----STATS----".center(45))
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
                print("----STATS----".center(45))
                print(f"HP: {result["pokemon2"]["hp"]}")
                time.sleep(.5)
                print(f"Attack: {result["pokemon2"]["attack"]}")
                time.sleep(.5)
                print(f"Defense: {result["pokemon2"]["defense"]}")
                time.sleep(.5)
                print("#" * 45)
                print()

                input("\nPress Enter to return to the main menu:")
                break
            
        # CLARIFYING DONE
        elif user == 4:
            while True:
                print("---------Choose only ONE pokemon---------".center(45))
                print()

                print("You will fight against a CPU.")
                print("HP is determined by HP + defense. Keep that in mind!")
                user_choice = input("Choose your Pokemon: ")

                print()

                result = get_data(user_choice)
                
                if searching(user_choice, result) == False:
                    print()
                    continue


                print("*" * 45)
                print("BATTLE".center(45))
            
                print()

                pokemon_battle(user_choice)
            
               
            
                

                input("\nPress Enter to return to the main menu:")
                break

        elif user == 5:
            print("Thank you for playing, trainer!".center(45))
            time.sleep(.5)
            print()
            print("WAITTTTT... someone wants to say bye".center(45))
            time.sleep(.5)
            pikachu_logo()
            print()
            print("Pikachu wants to wish you a safe trip!".center(45))
            print("BYE NOW!".center(45))
            break

        else:
            print("Invalid choice. Please choose 1-5.")

main()





# THURSDAY:
# FIX OPTION 3 AND 4
# FIX UP FUNCTIONS
# FIX UP IMPORT FROM DESIGN.PY to see who not to use 