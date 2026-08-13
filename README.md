## Getting Started

### Requirements

Make sure you have **Python 3** installed.

The project uses the following libraries:

- `requests` - Used to send requests to the PokeAPI and retrieve Pokemon data.
- `time` - Used to add small delays to the CLI output.
- `random` - Used to randomly select Pokemon from the computer side and determine who attacks first during battles.

### Installation

Clone the repository:

```bash
git clone https://github.com/ESCAMILLA69699/pokemon_ctd_project.git
```

Enter the project folder:

```bash
cd pokemon_ctd_project
```

Install the required external package:

```bash
pip install requests
```

### Run the Program

```bash
python main.py
```

## Features

The program includes five main options:

1. **Pokemon Information**
   - Search for a Pokemon and display its name, height, weight, and type.

2. **Pokemon Stats**
   - Search for a Pokemon and display its HP, attack, and defense.

3. **Compare Pokemon**
   - Compare the HP, attack, and defense of two different Pokemon.

4. **Pokemon Battle**
   - Choose a Pokemon and battle against a randomly selected computer Pokemon.
   - The `pokemonbattle()` function selects the computer's random Pokemon and prepares the battle.
   - The `pokemonrumble()` function handles the actual fight by calculating the Pokemon's total HP (defense + HP), determining who attacks first, and continuing the battle until there is a winner.


## Credits

Pokemon data is provided by **PokeAPI**:

https://pokeapi.co/

Pikachu ASCII art used in `design.py` was created by **wgcv on GitHub**.

https://gist.github.com/wgcv/14bc49b786db47c3af90



## Author

**Alexander Escamilla**

