import time


def pikachu_logo():
    time.sleep(.2)
    print(r"""
░█▀▀▄░░░░░░░░░░░▄▀▀█
░█░░░▀▄░▄▄▄▄▄░▄▀░░░█
░░▀▄░░░▀░░░░░▀░░░▄▀
░░░░▌░▄▄░░░▄▄░▐▀▀
░░░▐░░█▄░░░▄█░░▌▄▄▀▀▀▀█
░░░▌▄▄▀▀░▄░▀▀▄▄▐░░░░░░█
▄▀▀▐▀▀░▄▄▄▄▄░▀▀▌▄▄▄░░░█
█░░░▀▄░█░░░█░▄▀░░░░█▀▀▀
░▀▄░░▀░░▀▀▀░░▀░░░▄█▀
░░░█░░░░░░░░░░░▄▀▄░▀▄
░░░█░░░░░░░░░▄▀█░░█░░█
░░░█░░░░░░░░░░░█▄█░░▄▀
░░░█░░░░░░░░░░░████▀
░░░▀▄▄▀▀▄▄▀▀▄▄▄█▀
""")
# credits to: https://gist.github.com/wgcv/14bc49b786db47c3af90

def topdisplay():
    print("=" * 45)
    print("Welcome to my Pokemon Project: CLI Tool".center(45))
    print()
    print("BY: ALEXANDER ESCAMILLA".center(40))
    print("=" * 45)


def menuchoices():
     
     

     print("*" * 45)
     print("Main Menu".center(40))
     print("*" * 45)
     print()
     print("1. Get Pokemon Info")
     time.sleep(0.5)
     print("2. Get Pokemon Stats")
     time.sleep(0.5)
     print("3. Compare Pokemon Stats")
     time.sleep(0.5)
     print("4. Pokemon Battle")
     time.sleep(0.5)
     print("5. Exit")
     print()

def searching(user_choice, result):
    print("Searching for Pokémon...")
    time.sleep(1)

    if result is None:
        print(f"{user_choice.capitalize()} was not found!")
        return False
    else:
        print(f"{user_choice.capitalize()} found!")
        print()
        return True


def designstats(user_choice):
    print("#" * 45)
    print(user_choice.center(45))
    print("------".center(45))
    print()

def battlemenu():
    print("*" * 45)
    print("BATTLE".center(45))
    print("*" * 45)

def rules():
    print("*" * 45)
    print
    print("Before starting, here are the rules:".center(45))
    print()
    print("1. Don't pick any Intengers when prompted for a pokemon name-")
    print("   due to API structure.")
    print()
    print("2. Stay within the Intenger range (1 through 5).")
    print()
    print("3. If pokemon isn't found, it might not be your fault due to the -")
    print("   API or check your spelling.")
    print()
    print("*" * 45)

print(rules())

#topdisplay()
#pikachu_logo()
#print(menuchoices())
#print(searching("pikachu"))\


