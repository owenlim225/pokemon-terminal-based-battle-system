import random
from rich import box
from rich.align import Align
from rich.panel import Panel
from rich.table import Table
from rich.layout import Layout
from rich.progress import Progress
from rich.console import Console, Group

console = Console()

# ======================Progress Bar===========================

# with Progress() as progress:
#     task = progress.add_task("[cyan]Processing...", total=100)
#     for i in range(100):
#         progress.update(task, advance=1)

# =============================================================



class Frontend:
    def __init__(self) -> None:
        pass

    

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
        table.add_column("Poison", justify="center", style="yellow")
        table.add_column("Potion", justify="center", style="blue")

        # Add rows to the table
        for i, pokemon_data in enumerate(pokemon_list, start=1):
            pokemon, health, power, poisons, potions = pokemon_data
            table.add_row(str(i), pokemon, str(health), str(power), str(poisons), str(potions))

        # Print the table to the console
        console.print(table)


    

if __name__ == "__main__":
    Frontend()