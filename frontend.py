import random, os, time
from rich.panel import Panel
from rich.progress import Progress
from rich.console import Console
from rich.text import Text
from rich.table import Table
from rich.layout import Layout


from backend import Backend, GameData


class Frontend:
    def __init__(self) -> None:
        self.console = Console()
        self.backend = Backend()
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
        return self.display_program_info()

    def player_panel(self, player_number: int) -> Panel:
        return Panel(f"Player {player_number} Status", border_style="magenta" if player_number == 1 else "cyan")

    def make_layout(self) -> Layout:
        layout = Layout(name="root")

        layout.split(
            Layout(name="header", size=3),
            Layout(name="middle", ratio=1),
            Layout(name="footer", size=3),
        )
        layout["middle"].split(
            Layout(name="upper", ratio=3),
            Layout(name="lower", ratio=1),
        )
        layout["lower"].split_row(
            Layout(name="player1", ratio=1, minimum_size=30),
            Layout(name="player2", ratio=1, minimum_size=30),
        )

        return layout

    def show_loading_screen(self, loading_time: int = 5) -> None:
        """Show a loading screen with a progress bar for a given duration."""
        with Progress() as progress:
            task = progress.add_task("[green]Loading 🔥🏆Pokemon Battle 2.0!🏆🔥...", total=100)
            for _ in range(100):
                progress.update(task, advance=1)
                time.sleep(loading_time / 100)

    def display_program_info(self) -> Panel:
        os.system('cls')  # Clear the console for a fresh start

        # self.show_loading_screen(loading_time=5)

        info_text = Text.from_markup("""
        ⚔️[bold yellow]  Battle Instructions:[/] 
                ❤️ [green]Potion:[/] Boost Power          ☣️ [red]Poison:[/] Reduces Power 

                🥇 [green]Winner:[/]            🥉 [red]Loser:[/]
                💚 Health: [green]+5 pts[/]      💔 Health: [red]-10 pts[/]  
                
                ❗  [bold yellow]Every battle, current Pokémon's [green]health[/] will [red]decrease[/] by 2 points due to fatigue.[/]
                ❗  Battle continues until all selected Pokémon from both players have fought.
                                    
        [bold green]Press Enter to Start[/]
        """, justify="center")

        self.console.print(Panel(info_text, border_style="green"))

        input()

        return Panel(Text("Battle starting!", justify="center"), border_style="green")

    def run(self):
        self.console.clear()
        self.console.print(self.layout)

    def apply_effect(self, result: str, user_input: int, pokemon_name: str, current_power: int, player) -> None:
        console = Console()
        if result == "poison":
            effect_value = -random.randint(1, 5) * user_input
            new_power = max(0, current_power + effect_value)
            player.battle_pokemon[2] = new_power
            console.print(f"Unlucky! 🧙 cast a [bold red]poison spell[/bold red]. {pokemon_name}'s power is reduced by {abs(effect_value)} to {new_power}.")
        
        elif result == "potion":
            effect_value = random.randint(1, 5) * user_input
            new_power = current_power + effect_value
            player.battle_pokemon[2] = new_power
            console.print(f"Lucky! 🧙 cast a [bold green]potion spell[/bold green]. {pokemon_name}'s power is increased by {effect_value} to {new_power}.")

    def poison_or_potion(self, player) -> None:
        while True:
            try:
                accept = input("A 🧙 wants to bless your Pokémon! Accept? (Yes/No): ")

                if accept.lower() == "yes":
                    user_input = self.get_valid_user_input()

                    self.show_progress("🧙 is casting the spell...", 3)

                    result = random.choice(["poison", "potion"])
                    pokemon = player.battle_pokemon
                    pokemon_name, _, current_power = pokemon

                    self.apply_effect(result, user_input, pokemon_name, current_power, player)
                    break

                elif accept.lower() == "no":
                    self.console.print("You declined the offer ❌.", style="bold red")
                    time.sleep(2)
                    break

                else:
                    raise ValueError("Invalid input. Please type 'Yes' or 'No'.")

            except ValueError as e:
                self.console.print(f"[bold red]Error:[/bold red] {e}. Please try again.")
                time.sleep(2)

    def get_valid_user_input(self) -> int:
        while True:
            try:
                user_input = int(input("🧙 asks you for a number (1-6): "))
                if 1 <= user_input <= 6:
                    return user_input
                else:
                    raise ValueError("Input must be a number between 1 and 6.")
            except ValueError as e:
                self.console.print(f"[bold red]Error:[/bold red] {e}")

    def create_pokemon_table(self) -> Table:
        table = Table(title="⭐ Select your pokemon 🔥")
        table.add_column("Index", justify="center", style="cyan", no_wrap=True)
        table.add_column("Pokemon", justify="center", style="green")
        table.add_column("Health", justify="center", style="red")
        table.add_column("Power", justify="center", style="magenta")
        return table

    def display_pokemon_selection_table(self, pokemon_list: list[list]) -> None:
        if not pokemon_list:
            self.console.print("[bold red]No Pokémon data available.[/bold red]")
            return

        table = self.create_pokemon_table()

        for i, pokemon_data in enumerate(pokemon_list, start=1):
            # Handle cases where there's an extra fourth element
            if len(pokemon_data) < 3:
                self.console.print(f"[bold red]Error: Insufficient data for Pokémon at index {i}[/bold red]")
                self.console.print(f"Invalid data: {pokemon_data}")  # Log invalid data
                continue

            # Extract only the first three values: pokemon, health, power
            pokemon, health, power = pokemon_data[:3]

            # Check if data types are valid
            if not isinstance(pokemon, str) or not isinstance(health, int) or not isinstance(power, int):
                self.console.print(f"[bold red]Error: Invalid data types for Pokémon at index {i}[/bold red]")
                self.console.print(f"Invalid data: {pokemon_data}")  # Log invalid data
                continue

            # Add valid data to the table
            table.add_row(str(i), pokemon, str(health), str(power))

        self.console.print(table)



if __name__ == "__main__":
    