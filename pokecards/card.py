from rich import box, print
from rich.align import Align
from rich.console import Console, Group
from rich.layout import Layout
from rich.panel import Panel
from rich.progress import BarColumn, Progress, SpinnerColumn, TextColumn
from rich.syntax import Syntax
from rich.table import Table

from pokecards.model import Pokemon


def make_layout() -> Layout:
    """Define the layout."""
    layout = Layout(name="root", size=-1)

    layout.split(
        Layout(name="spacer", size=3),
        Layout(name="header", size=3),
        Layout(name="main", ratio=1),
        # Layout(name="footer", size=7),
    )
    layout["main"].split_row(
        Layout(name="side"),
        Layout(name="body", ratio=2, minimum_size=60),
    )
    layout["side"].split(Layout(name="box1"), Layout(name="box2"))
    return layout


class Header:
    def __init__(self, pkmn: Pokemon):
        self.name = pkmn.name.title()
        self.flavor = pkmn.flavor

    def __rich__(self) -> Panel:
        title = self.name
        text = self.flavor
        return Panel(Align.center(text), title=title, style="black on red")


def display_card(pokemon: Pokemon):
    layout = make_layout()
    layout["header"].update(Header(pokemon))
    print(layout)
