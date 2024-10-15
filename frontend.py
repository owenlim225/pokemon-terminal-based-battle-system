import random
import time
from rich import box
from rich.align import Align
from rich.panel import Panel
from rich.table import Table
from rich.layout import Layout
from rich.progress import Progress
from rich.console import Console, Group

console = Console()

import backend as BE
from backend import GameData

# ======================Progress Bar===========================

# with Progress() as progress:
#     task = progress.add_task("[cyan]Processing...", total=100)
#     for i in range(100):
#         progress.update(task, advance=1)

# =============================================================




class Frontend:
    def __init__(self) -> None:
        self.backend = BE.Backend()
        self.game_data = GameData()



        self.rich_layout = self.make_layout()
        self.rich_layout["header"].update(header())
        self.rich_layout["body"].update(self.main_window())
        self.rich_layout["mechanics"].update(self.mechanics_buttons())
        self.rich_layout["footer"].update(self.battle_footer())


    def header() -> Panel:
        grid = Table.grid(expand=True)
        grid.add_column(justify="center")
        grid.add_row(
            "[b]🔥🏆Pokemon Battle 2.0!🏆🔥[/b]"
        )
        return Panel(grid, border_style="blue")





    def make_layout(self) -> Layout:
        """Define the layout."""
        layout = Layout(name="root")

        # Split layout into three
        layout.split(
            Layout(name="header", size=3),
            Layout(name="main", ratio=3),
            Layout(name="footer", size=5),
        )

        # Split the main area into side and body
        layout["main"].split_row(
            Layout(name="side", ratio=1, minimum_size=30),
            Layout(name="body", ratio=3, minimum_size=70),
        )
        layout["side"].split_column(
            Layout(name="user_detail"),
            Layout(name="mechanics"))
        return layout










    def poison_or_potion(self, player) -> None:
        """Apply either a poison or a potion effect to the player's Pokémon power."""
        console = Console()

        while True:
            try:
                # Ask the user if they want to accept the blessing
                accept = input("A 🧙 wants to bless your Pokémon! Accept? (Yes/No): ")

                # Validate the input
                if accept.lower() == "yes":
                    user_input = int(input("🧙 asks you for a number (1-6): "))
                    if not (1 <= user_input <= 6):
                        raise ValueError("Input must be a number between 1 and 6.")
                    
                    # Show the progress bar (3 seconds total)
                    with Progress() as progress:
                        task = progress.add_task("[cyan]🧙 is casting the spell...", total=100)
                        for _ in range(100):
                            progress.update(task, advance=1)
                            time.sleep(0.03)  # 3 seconds total sleep time

                    # Define possible outcomes (poison or potion)
                    outcomes = ["poison", "potion"]
                    result = random.choice(outcomes)

                    # Access the player's battle Pokémon
                    pokemon = player.battle_pokemon
                    pokemon_name = pokemon[0]  # Name of the Pokémon
                    current_power = pokemon[2]  # Current power of the Pokémon

                    # Apply the effect based on the outcome
                    if result == "poison":
                        effect_value = -random.randint(1, 5) * user_input
                        new_power = max(0, current_power + effect_value)  # Ensure power doesn't go below 0
                        pokemon[2] = new_power  # Update Pokémon's power
                        console.print(f"Unlucky! 🧙 cast a [bold red]poison spell[/bold red]. {pokemon_name}'s power is reduced by {abs(effect_value)} to {new_power}.")

                    elif result == "potion":
                        effect_value = random.randint(1, 5) * user_input
                        new_power = current_power + effect_value
                        pokemon[2] = new_power  # Update Pokémon's power
                        console.print(f"Lucky! 🧙 cast a [bold green]potion spell[/bold green]. {pokemon_name}'s power is increased by {effect_value} to {new_power}.")

                    # Exit the loop after the effect is applied
                    break

                elif accept.lower() == "no":
                    console.print("You declined the offer ❌.", style="bold red")
                    time.sleep(2)
                    break

                else:
                    raise ValueError("Invalid input. Please type 'Yes' or 'No'.")

            except ValueError as e:
                console.print(f"[bold red]Error:[/bold red] {e}. Please try again.")
                time.sleep(2)
                





    def display_program_info(self) -> None:
        pass



    def display_pokemon_selection_table(pokemon_list):
        # Initialize Rich console
        console = Console()

        # Create a Rich table
        table = Table(title="⭐ Select your pokemon 🔥")

        # Add table headers
        table.add_column("Index", justify="center", style="cyan", no_wrap=True)
        table.add_column("Pokemon", justify="center", style="green")
        table.add_column("Health", justify="center", style="red")
        table.add_column("Power", justify="center", style="magenta")


        # Add rows to the table
        for i, pokemon_data in enumerate(pokemon_list, start=1):
            pokemon, health, power = pokemon_data
            table.add_row(str(i), pokemon, str(health), str(power))

        # Print the table to the console
        console.print(table)


    

if __name__ == "__main__":
    Frontend()