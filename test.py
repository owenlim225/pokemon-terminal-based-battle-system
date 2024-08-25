from rich import print
from rich.layout import Layout
from rich.console import Console, Group

console = Console()



layout = make_layout()
layout["header"].update(Header())
layout["body"].update(make_sponsor_message())
layout["box2"].update(Panel(make_syntax(), border_style="green"))
layout["box1"].update(Panel(layout.tree, border_style="red"))
layout["footer"].update(progress_table)



layout.split_column(
    Layout(name="upper"),
    Layout(name="lower")
)
layout["lower"].split_row(
    Layout(name="left"),
    Layout(name="right"),
)

def make_layout() -> Layout:
    """Define the layout."""
    layout = Layout(name="root")

    layout.split(
        Layout(name="header", size=3),
        Layout(name="main", ratio=1),
        Layout(name="footer", size=7),
    )
    layout["main"].split_row(
        Layout(name="side"),
        Layout(name="body", ratio=2, minimum_size=60),
    )
    layout["side"].split(Layout(name="box1"), Layout(name="box2"))
    return layout
