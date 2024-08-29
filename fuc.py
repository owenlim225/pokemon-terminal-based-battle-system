# Limosnero, Sherwin P.
# J2S <3

from time import sleep
import threading
import random

from rich import box
from rich.align import Align
from rich.console import Console, Group
from rich.layout import Layout
from rich.panel import Panel
from rich.table import Table
from rich.live import Live



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




console = Console()

# Flag to control the main loop
exit_flag = False

def header() -> Panel:
    grid = Table.grid(expand=True)
    grid.add_column(justify="center")
    grid.add_row(
        "[b]Pokemon Battle![/b]"
    )
    return Panel(grid, border_style="blue")

class Display:
    def __init__(self):
        self.layout = self.make_layout()
        self.user_name = "Player"
        self.battle_no = 0
        self.user_final_power = 0
        self.current_pokemon = "Pikachu"  # Initialize current Pokemon
        self.battle_results = []  # Store battle results
        self.title_name = ""

        self.layout["header"].update(header())
        self.layout["body"].update(self.main_window())
        self.layout["mechanics"].update(self.mechanics_buttons())
        self.layout["user_detail"].update(self.user_stats())
        self.layout["footer"].update(self.battle_footer())

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



    # When user input mali
    def invalid_input(self) -> Panel:
        title_name = ""
        invalid_input = Table.grid(padding=1)
        invalid_input.add_column(style="white", justify="center")
        
        invalid_input.add_row(
            "[red]Invalid Input[/red]"
        )
        
        
        invalid_input.add_row(
            "Please try again."
        )

        self.update_main_window(invalid_input, title_name)



    # Main window panel
    def main_window(self) -> Panel:
        main_window_dialogue = Table.grid(padding=1)
        main_window_dialogue.add_column(style="white", justify="center")
        
        main_window_dialogue.add_row(
            "Welcome to [bright_blue]Pokemon[/bright_blue] [red]Battle![/red]"
        )

        main_window_dialogue.add_row(
            "A quick Terminal-based battle system game made by: [yellow]Sherwin P. Limosnero[/yellow] from [red]J2S![/red]"
        )

        main_window_dialogue.add_row(
            "To play the [green]game[/green], refer to the [bright_blue]buttons[/bright_blue] on your left side"
        )

        main_window_dialogue.add_row(
            "type the letter then press [green]enter[/green] to use!"
        )

        main_window_dialogue.add_row(
            "For [yellow]first time players[/yellow], input [green][Q][/green] to show [green]Stats and buttons[/green]."
        )

        main_window_dialogue.add_row(
            "To select your starting [green]Pokemon[/green] by typing [green][S][/green] then enter."
        )

        # Main_window_dialogue get passed here
        message = Table.grid(padding=1)
        message.add_column()
        message.add_column(no_wrap=True)
        message.add_row(main_window_dialogue)


        # Then the message get passed here para makita sa body.
        message_panel = Panel(
            Align.center(
                Group("\n", Align.center(main_window_dialogue))),
                border_style="bright_blue")
        return message_panel



    def update_main_window(self, content, title_name: str):
        # Use the provided title_name instead of reassigning it
        new_main_window = Table.grid(padding=1)
        new_main_window.add_column(style="white", justify="center")
        new_main_window.add_row(content)
        
        # Create the panel with the correct title
        message_panel = Panel(
            Align.center(
                Group("\n", Align.center(new_main_window))),
            title=title_name,  # Use the passed title_name here
            border_style="bright_blue"
        )
        
        # Directly update the body with the new message panel
        self.layout["body"].update(message_panel)









    def update_user_stats(self, user_name: str, battle_no: int, user_final_power: int, current_pokemon: str):
        self.user_name = user_name
        self.battle_no = battle_no
        self.user_final_power = user_final_power
        self.current_pokemon = current_pokemon
        self.layout["user_detail"].update(self.user_stats())









    def update_battle_results(self, results):
        # Set the title for the battle records
        title_name = "Battle Records"
        
        # Create the battle results table
        table = Table()

        table.add_column("Battle No.", justify="right", style="cyan", no_wrap=True)
        table.add_column("User Power", justify="center", style="green")
        table.add_column("CPU Power", justify="center", style="red")
        table.add_column("Status", justify="center", style="green", min_width=20, max_width=50)

        # Add rows to the table
        for result in results:
            table.add_row(str(result[0]), str(result[1]), str(result[2]), result[3])


        # Create the panel with the correct title
        message_panel = Panel(
            Align.center(
                Group("\n", Align.center(table))),
            title=title_name,  # Use the passed title_name here
            border_style="bright_blue"
        )
        
        # Directly update the body with the new message panel
        self.layout["body"].update(message_panel)
        self.layout["footer"].visible = False












    def pokedex(self):
        title_name = "Pokedex"

        table = Table()

        table.add_column("Name", justify="right", style="cyan", no_wrap=True)
        table.add_column("Power", justify="center", style="green")

        for key, value in pokemon_char.items():
            table.add_row(str(key), str(value))

        # Update the main window with battle results, using the correct title
        self.update_main_window(table, title_name)
        


    def select_pokemon(self):
        title_name = "Select Pokemon"

        table = Table()

        table.add_column("Num", justify="center", style="green")
        table.add_column("Name", justify="center", style="cyan", no_wrap=True)
        table.add_column("Base power", justify="center", style="green")

        # Iterate through pokemon_char dictionary and add rows to the table
        for count, (key, value) in enumerate(pokemon_char.items(), start=1):
            table.add_row(str(count), key, str(value))

        # Update the main window with the table and title
        self.update_main_window(table, title_name)



    # User stats ~ Mid Top Left
    def user_stats(self) -> Panel:
        content = f"""Name        : {self.user_name}
Battle No   : {self.battle_no}
Final Power : {self.user_final_power}
C. Pokemon  : {self.current_pokemon}
        """
        return Panel(
            Align.left(content, pad=(1, 2)),
            title="Player Stats",
            border_style="red",
            padding=(1, 2)
        )

    # Buttons ~ Mid Bottom Left
    def mechanics_buttons(self) -> Panel:
        content = """\
[C] Continue    
[P] Pokedex       
[S] Select Pokemon
[B] Battle Records
[X] Exit
        """
        return Panel(
            Align.left(content, pad=(1, 2)),
            title="Buttons",
            padding=(1, 2)
        )

    def battle_footer(self) -> Table:
        # Create a Table with specific column widths
        battle_footer = Table.grid(expand=True)

        # Set column widths
        # Note: Adjust width values according to your requirement
        column_widths = [20, 5, 20]  # Example widths for each column
        for width in column_widths:
            battle_footer.add_column(width=width, justify="center")

        # Add rows with Panels
        battle_footer.add_row(
            Panel(
                "working on it", 
                title="Player", 
                border_style="green",  # Green border for Player layout
                padding=(1, 2)
            ),

            Panel(
                "User win!", 
                border_style="white",  # White border for result message
                padding=(1, 1)
            ),

            Panel(
                "working on it", 
                title="Computer", 
                border_style="red",  # Red border for Computer layout
                padding=(1, 2)
            )
        )
        return battle_footer





class Mechanism:
    def __init__(self, display: Display):
        self.display = display
        self.console = Console()
        self.first_time = True
        self.selecting_pokemon = False 


    def get_user_input(self):
        global exit_flag
        self.display.layout["side"].visible = False
        self.display.layout["footer"].visible = False

        while True:
            user_input = input()
            if user_input.lower() == 'x':
                exit_flag = True
                break

            elif user_input.lower() == 'c':
                self.display.update_main_window("Continue selected")

            elif user_input.lower() == 'p':
                self.display.pokedex()

            elif user_input.lower() == 'q':
                self.display.layout["side"].visible = True

            elif user_input.lower() == 's':
                self.display.select_pokemon()
                self.display.layout["footer"].visible = True
                self.selecting_pokemon = True  # Set to True when selecting Pokemon

            elif user_input.lower() == 'b':
                self.display.update_battle_results(self.get_battle_results())
                
            elif self.selecting_pokemon and user_input.isdigit():
                self.display.handle_pokemon_number(int(user_input))  # Handle number input
            else:
                self.display.invalid_input()

            if not self.selecting_pokemon:
                self.selecting_pokemon = False
                




    def get_battle_results(self):
        # Sample results
        # Normally, this data should be dynamically generated or retrieved from a source
        results = [
            (1, 120, 110, "Player wins"),
            (2, 130, 140, "CPU wins"),
            (3, 150, 150, "Draw"),
            (4, 120, 110, "Player wins"),
            (5, 130, 140, "CPU wins"),
            (6, 150, 150, "Draw"),
            (7, 120, 110, "Player wins"),
            (8, 130, 140, "CPU wins"),
            (9, 150, 150, "Draw"),
            (10, 120, 110, "Player wins")
        ]
        return results



    def Choose_Pokemon(self):
        count = 0
        for key in pokemon_char: # showcase pokemon_char in an organized manner
            count += 1
            print(f"[{count}] {key}", end="\n" if count % 2 == 0 else "\t") # organize display sa terminal
        print()

        try: # handle error kapag mali ni input ni user
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

    def Bot_Pokemon(self): # pokemon ng bot kalaban
        pokemon_list = list(pokemon_char.keys())
        return random.choice(pokemon_list)

    def calculate_power(self, base_power): # Give additional base power sa pokemon on both side
        return base_power + random.randint(1, 100)

    def battle(self, user_pokemon, bot_pokemon): # Battle system calculation basta
        user_base_power = pokemon_char[user_pokemon] # Base power ni user
        bot_base_power = pokemon_char[bot_pokemon] # Base power ni bot

        # Calculate the final power ng dalawa
        user_final_power = self.calculate_power(user_base_power)
        bot_final_power = self.calculate_power(bot_base_power)

        # Determine the result
        result = "Tie"
        if user_final_power > bot_final_power:
            self.user_power += bot_final_power
            result = "User Wins"
        elif user_final_power < bot_final_power:
            result = "Computer Wins"

        # Add battle results to the list
        self.UI.battle_results.append((self.battle_num, user_final_power, bot_final_power, result))

        # Print the battle details
        print(f"Battle {self.battle_num}:")
        print(f"{self.UI.user_name}: {user_pokemon} - Power: {user_final_power}" + " "*20 + f"Bot: {bot_pokemon} - Power: {bot_final_power}")
        print(f"Result: {result}")
        print(f"You absorbed {self.user_power} power!")
        print()    












# Initialize Display and Mechanism
display = Display()
mechanism = Mechanism(display)

# threading kasi nag rerefresh screen every 60secs, para maganda may box box layout
input_thread = threading.Thread(target=mechanism.get_user_input, daemon=True)
input_thread.start()

with Live(display.layout, refresh_per_second=30, screen=True):
    while not exit_flag:
        sleep(0.5)
        display.battle_footer()

        # Update user stats with dynamic data
        display.update_user_stats(display.user_name, display.battle_no, display.user_final_power, display.current_pokemon)
        # Update other components as needed

console.print("Exiting game...", style="bold red")
