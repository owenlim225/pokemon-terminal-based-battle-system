from datetime import datetime
from time import sleep
import threading

from rich import box
from rich.align import Align
from rich.console import Console, Group
from rich.layout import Layout
from rich.panel import Panel
from rich.progress import BarColumn, Progress, SpinnerColumn, TextColumn
from rich.table import Table
from rich.live import Live

console = Console()

# Flag to control the main loop
exit_flag = False

def header() -> Panel:
    grid = Table.grid(expand=True)
    grid.add_column(justify="center")
    grid.add_row(
        "[b]Terminal-based Pokemon Battle[/b]"
    )
    return Panel(grid, border_style="blue")

class Display:
    def __init__(self):
        self.layout = self.make_layout()
        self.job_progress = self.setup_progress()
        self.total = sum(task.total for task in self.job_progress.tasks)
        self.overall_progress = Progress()
        self.overall_task = self.overall_progress.add_task("All Jobs", total=int(self.total))
        self.user_name = "Burat"
        self.battle_no = 69
        self.user_final_power = 420

        self.layout["header"].update(header())
        self.layout["body"].update(self.main_window())
        self.layout["mechanics"].update(self.mechanics_buttons())
        self.layout["user_detail"].update(self.user_stats(self.user_name, self.battle_no, self.user_final_power))
        self.layout["footer"].update(self.progress_table())

    def make_layout(self) -> Layout:
        """Define the layout."""
        layout = Layout(name="root")

        # Split layout into three
        layout.split(
            Layout(name="header", size=3),
            Layout(name="main", ratio=1),
            Layout(name="footer", size=10),
        )

        # Split the main area into side and body
        layout["main"].split_row(
            Layout(name="side"),
            Layout(name="body", ratio=2, minimum_size=60),
        )
        layout["side"].split_column(
            Layout(name="user_detail"),
            Layout(name="mechanics"))
        return layout

    # Main window panel
    def main_window(self) -> Panel:
        main_window_dialogue = Table.grid(padding=1)
        main_window_dialogue.add_column(style="green", justify="right")
        main_window_dialogue.add_column(no_wrap=True)
        
        main_window_dialogue.add_row(
            "Welcome to Pokemon Battle! Made by: Sherwin P. Limosnero"
        )
        main_window_dialogue.add_row(
            "What is your name?"
        )
        main_window_dialogue.add_row(
            "Your name", "tite"
        )

        message = Table.grid(padding=1)
        message.add_column()
        message.add_column(no_wrap=True)
        message.add_row(main_window_dialogue)

        message_panel = Panel(
            Align.center(
                Group("\n", Align.center(main_window_dialogue)),
                vertical="middle",
            ),
            box=box.ROUNDED,
            padding=(1, 2),
            border_style="bright_blue",
        )
        return message_panel

    # User stats ~ Mid Top Left
    def user_stats(self, user_name: str, battle_no: int, user_final_power: int) -> Panel:
        content = f"""
        Name: {user_name}
        Battle No: {battle_no}
        Final Power: {user_final_power}
        """
        panel = Panel(content, title="Player Stats", border_style="red")
        return panel

    # Buttons ~ Mid Bottom Left
    def mechanics_buttons(self) -> Panel:
        content = """\
        
        [C] Continue    
        [S] Stats       
        [N] New Pokémon
        [B] Battle Records
        [X] Exit
        """
        panel = Panel(content, title="Buttons")
        return panel

    def setup_progress(self) -> Progress:
        job_progress = Progress(
            "{task.description}",
            SpinnerColumn(),
            BarColumn(),
            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
        )
        job_progress.add_task("[green]Cooking")
        job_progress.add_task("[magenta]Baking", total=200)
        job_progress.add_task("[cyan]Mixing", total=400)
        return job_progress

    def progress_table(self) -> Panel:
        progress_table = Table.grid(expand=True)
        progress_table.add_row(
            Panel(
                "working on it", 
                title="Burat", 
                border_style="green",  # Green border for Burat layout
                padding=(1, 2)
            ),
            Panel(
                "working on it", 
                title="Computer", 
                border_style="red",  # Red border for Computer layout
                padding=(1, 2)
            )
        )
        return progress_table

    def update_user_stats(self, user_name: str, battle_no: int, user_final_power: int):
        self.layout["user_detail"].update(self.user_stats(user_name, battle_no, user_final_power))

    def update_progress(self):
        completed = sum(task.completed for task in self.job_progress.tasks)
        self.overall_progress.update(self.overall_task, completed=completed)

class Mechanism:
    def __init__(self, display: Display):
        self.display = display

    def get_user_input(self):
        global exit_flag
        while True:
            user_input = input()
            if user_input.lower() == 'x':
                exit_flag = True
                break

# Initialize Display and Mechanism
display = Display()
mechanism = Mechanism(display)

# Start the input thread
input_thread = threading.Thread(target=mechanism.get_user_input, daemon=True)
input_thread.start()

with Live(display.layout, refresh_per_second=10, screen=True):
    while not exit_flag:
        sleep(0.1)
        for job in display.job_progress.tasks:
            if not job.finished:
                display.job_progress.advance(job.id)

        display.update_progress()

        # Update user stats with dynamic data
        display.update_user_stats(display.user_name, display.battle_no, display.user_final_power)
        # Update other components as needed

console.print("Exiting game...", style="bold red")
