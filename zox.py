import random
import os
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.align import Align
from rich.layout import Layout

pokemon_char = {
    "Mewtwo": 90,
    "Snorlax": 80,
    "Machamp": 75,
    "Gengar": 70,
    "Bulbasaur": 60,
    "Squirtle": 58,
    "Charmander": 55,
    "Eevee": 52,
    "Pikachu": 50,
    "Jigglypuff": 45,
}

class UI:
    def __init__(self):
        self.console = Console()
        self.user_name = ""
        self.battle_results = []

    def Intro(self):
        content = """
        Welcome to Pokemon battle!
        Made by: Sherwin P. Limosnero

        What is your name?
        """

        panel = Panel(content.strip(), border_style="bold", expand=False)
        self.console.print(panel)

        self.user_name = input("Your name: ")
        welcome_message = f"Welcome {self.user_name}! Please choose your Pokémon."
        welcome_panel = Panel(welcome_message, border_style="bold", expand=False)
        self.console.print(welcome_panel)

    def Battle_Results(self):
        table = Table(title="Battle Results")
        table.add_column("Battle No.", justify="right", style="cyan", no_wrap=True)
        table.add_column("User Power", justify="center", style="green")
        table.add_column("CPU Power", justify="center", style="red")
        table.add_column("Status", justify="center", style="green")

        for result in self.battle_results:
            table.add_row(str(result[0]), str(result[1]), str(result[2]), result[3])

        self.console.print(table)

class Game:
    def __init__(self):
        self.UI = UI()
        self.user_power = 0
        self.battle_num = 1
        self.user_pokemon = ""

    def Choose_Pokemon(self):
        count = 0
        for key in pokemon_char:
            count += 1
            print(f"[{count}] {key}", end="\n" if count % 2 == 0 else "\t")
        print()

        try:
            user_choice = int(input("Your Pokemon: "))

            if 1 <= user_choice <= len(pokemon_char):
                pokemon_list = list(pokemon_char.keys())
                selected_pokemon = pokemon_list[user_choice - 1]
                print(f"You chose {selected_pokemon}")
                return selected_pokemon
            else:
                print("Invalid choice. Please select a valid number.")
                return self.Choose_Pokemon()

        except ValueError:
            print("Invalid input. Please enter a number.")
            return self.Choose_Pokemon()

    def Bot_Pokemon(self):
        pokemon_list = list(pokemon_char.keys())
        return random.choice(pokemon_list)

    def calculate_power(self, base_power):
        return base_power + random.randint(1, 100)

    def battle(self, user_pokemon, bot_pokemon):
        user_base_power = pokemon_char[user_pokemon]
        bot_base_power = pokemon_char[bot_pokemon]

        user_final_power = self.calculate_power(user_base_power)
        bot_final_power = self.calculate_power(bot_base_power)

        result = "Tie"
        if user_final_power > bot_final_power:
            self.user_power += bot_final_power
            result = "User Wins"
        elif user_final_power < bot_final_power:
            result = "Computer Wins"

        self.UI.battle_results.append((self.battle_num, user_final_power, bot_final_power, result))

        print(f"Battle {self.battle_num}:")
        print(f"{self.UI.user_name}: {user_pokemon} - Power: {user_final_power}" + " "*20 + f"Bot: {bot_pokemon} - Power: {bot_final_power}")
        print(f"Result: {result}")
        print(f"You absorbed {self.user_power} power!")
        print()

    def Start(self):
        os.system('cls')
        self.UI.Intro()
        _In_Game = True

        while _In_Game:
            if self.user_power == 0 or input("Would you like to select a new Pokémon? (n/c): ").lower() == 'n':
                user_pokemon = self.Choose_Pokemon()
            else:
                user_pokemon = self.user_pokemon

            bot_pokemon = self.Bot_Pokemon()
            self.battle(user_pokemon, bot_pokemon)
            self.user_pokemon = user_pokemon
            self.battle_num += 1

            user_input = input("Do you want to continue battling, choose a new Pokémon, or exit? (c/n/x): ").lower()
            if user_input == 'x':
                _In_Game = False
                print("Thanks for playing! Goodbye!")
                self.UI.Battle_Results()
            elif user_input == 'n':
                continue
            elif user_input != 'c':
                print("Invalid input. Exiting the game.")
                _In_Game = False
                self.UI.Battle_Results()

def pokedex() -> Panel:
    """Display the Pokémon battle system inside a panel."""
    console = Console()

    # Instantiate the game and UI classes
    game = Game()
    game.UI.Intro()  # Print the introduction panel
    game.Start()  # Start the game logic

    # Prepare the battle results table
    table = Table(title="Battle Results")
    table.add_column("Battle No.", justify="right", style="cyan", no_wrap=True)
    table.add_column("User Power", justify="center", style="green")
    table.add_column("CPU Power", justify="center", style="red")
    table.add_column("Status", justify="center", style="green")

    # Add the battle results to the table
    for result in game.UI.battle_results:
        table.add_row(str(result[0]), str(result[1]), str(result[2]), result[3])

    # Create a panel with the battle results
    message_panel = Panel(
        Align.center(table, vertical="middle"),
        box="ROUNDED",
        padding=(1, 2),
        border_style="bright_blue",
    )

    return message_panel

if __name__ == "__main__":
    panel = pokedex()
    console = Console()
    console.print(panel)
