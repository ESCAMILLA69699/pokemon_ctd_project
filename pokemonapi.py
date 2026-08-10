"""
In this POKEMONAPI file:

This file communicates with the PokeAPI. It sends requests to retrieve 
Pokémon information in JSON, based on the name provided by the user.
"""
# Base endpoint: https://pokeapi.co/api/v2/pokemon/{name}

import requests

BASE_URL = "https://pokeapi.co/api/v2"

def get_data(name):
    poke_url = f"{BASE_URL}/pokemon/{name}"
    response = requests.get(poke_url)

    if response.status_code == 200:
        ## IF POKEMON CAN BE FOUND IN THE API, then it'll return as code 200
        return response.json()
    else:
        ## OTHERWISE, as code 404 (not found)
        print(f"UH OH, something went wrong: {response.status_code}")


#get_data("pikachu")
#get_data("squirtle")
#works good