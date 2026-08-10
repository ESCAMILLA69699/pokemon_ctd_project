import json
from pokemonapi import get_data
pokemon = get_data("pikachu")

print(json.dumps(pokemon, indent=4))