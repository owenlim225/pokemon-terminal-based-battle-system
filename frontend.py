import random, os, time
from rich.panel import Panel
from rich.progress import Progress
from rich.console import Console
from rich.text import Text
from rich.table import Table
from rich.layout import Layout

import backend as BE
from backend import GameData

class Frontend:
    def __init__(self) -> None:
        self.console = Console()
        self.backend = BE.Backend()
        self.game_data = GameData()

        # Initialize layout
        self.layout = self.make_layout()
        self.layout["header"].update(self.header())
        self.layout["upper"].update(self.main_window())  
        self.layout["player1"].update(self.player_panel(1))
        self.layout["player2"].update(self.player_panel(2))
        self.layout["footer"].update(self.footer())

    # ============== Rich Console ==============
    def header(self) -> Panel:
        grid = Table.grid(expand=True)
        grid.add_column(justify="center")
        grid.add_row("[b]🔥🏆Pokemon Battle 2.0!🏆🔥[/b]")
        return Panel(grid, border_style="blue")

    def footer(self) -> Panel:
        grid = Table.grid(expand=True)
        grid.add_column(justify="center")
        grid.add_row("[b]🔥 Be the best in the world 🔥[/b]")
        return Panel(grid, border_style="blue")

    def main_window(self) -> Panel:
        # Use display_program_info to display the battle program info
        return self.display_program_info()

    def player_panel(self, player_number: int) -> Panel:
        # Panels for Player 1 and Player 2 at the bottom
        return Panel(f"Player {player_number} Status", border_style="magenta" if player_number == 1 else "cyan")

    def make_layout(self) -> Layout:
        """Define the layout."""
        layout = Layout(name="root")

        # Header and Footer with a fixed size
        layout.split(
            Layout(name="header", size=3),
            Layout(name="middle", ratio=1),
            Layout(name="footer", size=3),
        )

        # Split the middle into upper and lower parts (upper part is larger)
        layout["middle"].split(
            Layout(name="upper", ratio=3),  # Upper part (larger section)
            Layout(name="lower", ratio=1),  # Lower part
        )

        # Split the lower part into Player 1 and Player 2 panels
        layout["lower"].split_row(
            Layout(name="player1", ratio=1, minimum_size=30),   # Left panel for Player 1
            Layout(name="player2", ratio=1, minimum_size=30),   # Right panel for Player 2
        )

        return layout

    def display_program_info(self) -> Panel:
        os.system('cls')
        
        # Step 1: Show the loading screen
        with Progress() as progress:
            task = progress.add_task("[green]Loading 🔥🏆Pokemon Battle 2.0!🏆🔥...", total=100)
            for i in range(100):
                progress.update(task, advance=1)
                time.sleep(5 / 100)  # Total time is 5 seconds

        # Step 2: After loading, update the panel with battle instructions
        info_text = Text.from_markup("""
        ⚔️[bold yellow]  Battle Instructions:[/] 
                ❤️ [green]Potion:[/] Boost Power          ☣️ [red]Poison:[/] Reduces Power 

                🥇 [green]Winner:[/]            🥉 [red]Loser:[/]
                💚 Health: [green]+5 pts[/]      💔 Health: [red]-10 pts[/]  
                
                ❗  [bold yellow]Every battle, current Pokémon's [green]health[/] will [red]decrease[/] by 2 points due to fatigue.[/]
                ❗  Battle continues until all selected Pokémon from both players have fought.
                                     
        [bold green]Press Enter to Start[/]
        """, justify="center")

        # Create a Panel with the formatted text after loading
        return Panel(info_text, border_style="green")

    def run(self):
        """Runs the main layout."""
        self.console.clear()
        # Display the layout (which includes the loading and program info)
        self.console.print(self.layout)







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
    console = Console()
    frontend = Frontend()

    # Show the layout, including the loading screen and battle info
    frontend.run()