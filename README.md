# Pokémon Battle Game

A simple text-based Pokémon battle game where you choose your Pokémon and battle against a random bot-controlled Pokémon. Each Pokémon has a base power, and a random boost is added to determine the winner.

---

## How to Play

1. **Choose Your Pokémon**: When the game starts, you'll see a list of available Pokémon. Pick one by entering the number next to it.
2. **Battle the Bot**: You’ll then battle against a randomly selected bot Pokémon. The Pokémon with the highest final power (base power + random boost) wins.
3. **Replay or Change Pokémon**: After the battle, you can choose to select a new Pokémon or continue with the current one.

---

## Game Flow

1. **Pokémon List**: You choose from 10 different Pokémon with varying base powers.
2. **Random Power Boost**: Both your Pokémon and the bot get a random boost to their power before the battle.
3. **Winner**: The one with the higher total power wins the battle!

---

## Example Gameplay

Pokemon Battle

[1] Mewtwo [2] Snorlax [3] Machamp [4] Gengar [5] Bulbasaur [6] Squirtle [7] Charmander [8] Eevee [9] Pikachu [10] Jigglypuff

Your Pokémon: 1 Would you like to select a new Pokémon? (n/c): n

yaml
Copy code

---

## Running the Game

To start the game, simply run the script:

```bash
python pokemon_battle_game.py
Code Overview
intro(): Starts the game and shows the list of Pokémon.
user_pokemon(): Lets you choose your Pokémon.
bot_pokemon(): Randomly picks a Pokémon for the bot.
calculate_power(): Adds a random power boost to the Pokémon's base power.
battle(): Compares the powers and decides the winner.
run(): Runs the game loop, letting you battle multiple times.
Improvements to Consider
Add a winner announcement after each battle.
Implement a leveling system for Pokémon.
Add a more interactive UI.
License
MIT License.

Enjoy battling! 🎮
