"""Rich terminal UI and gothic ASCII aesthetics for HauntShell."""

from __future__ import annotations

import sys
import time
from typing import Iterable
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich.live import Live

console = Console()

GHOST_BANNER = r"""[bold magenta]
      .-.
     (o.o)    [bold bright_white]H A U N T S H E L L[/bold bright_white]
      |=|     [italic cyan]The Ghost in the Machine[/italic cyan]
     /   \    [dim purple]v1.0.0 • Open-Weight AI Necromancer[/dim purple]
    (     )
    /`---'\
[/bold magenta]"""

SEANCE_CIRCLE = r"""[bold purple]
        .---.
       / /"\ \      [italic bright_white]* The veil thins... summoning digital spirit *[/italic bright_white]
      | | | | |     [dim cyan]🕯️  🕯️  🕯️  Offline Séance Chamber  🕯️  🕯️  🕯️[/dim cyan]
       \ \_/ /
        `---`
[/bold purple]"""

OFRENDA_BANNER = r"""[bold yellow]
     ╭━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╮
     │   🌼 🕯️  OFRENDA DIGITAL • DÍA DE LOS MUERTOS  🕯️ 🌼         │
     ╰━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╯
[/bold yellow]"""

SUGAR_SKULL = r"""[bold bright_yellow]
           .-''''-.
          /  _  _  \     [bold gold1]Calavera de Azúcar[/bold gold1]
         |  (o)(o)  |    [italic orange3]Honor a nuestros ancestros digitales[/italic orange3]
         |    /\    |
          \  \__/  /
           `'----'`
[/bold bright_yellow]"""

TOMBSTONE_ART = r"""[bold dim white]
           .---.
          / RIP \
         |       |       [bold red]CODEBASE POST-MORTEM[/bold red]
         |  ✝    |       [italic bright_black]Coroner's Examination of Dead Code & Crashes[/italic bright_black]
         |       |
      ___|_______|___
[/bold dim white]"""

CANDLES = "🕯️  🕯️  🕯️  🕯️  🕯️"


def get_candle_display(turn: int, max_turns: int = 5) -> str:
    """Return candle status indicating flame consumption over séance turns."""
    remaining = max(0, max_turns - turn)
    if remaining == 0:
        return "💨  💨  💨  💨  💨  [italic red]*The candles are extinguished. The veil closes.*[/italic red]"
    icons = []
    for i in range(max_turns):
        if i < remaining - 1:
            icons.append("🕯️")
        elif i == remaining - 1:
            icons.append("🔥")
        else:
            icons.append("💨")
    return "  ".join(icons)


def print_banner() -> None:
    """Print main HauntShell banner."""
    console.print(GHOST_BANNER)


def print_seance_header(spirit_name: str, era: str) -> None:
    """Print the séance summoning header."""
    console.print(SEANCE_CIRCLE)
    msg = Text.from_markup(
        f"   [bold white]Summoned Entity:[/bold white] [bold magenta]{spirit_name}[/bold magenta] [italic dim cyan]({era})[/italic dim cyan]\n"
        f"   [bold gold1]{CANDLES}[/bold gold1]\n"
    )
    console.print(Panel(msg, border_style="magenta", title="[bold purple]🔮 THE SÉANCE CIRCLE[/bold purple]"))


def print_ofrenda_header(name: str, era: str, offering: str) -> None:
    """Print the Día de los Muertos ofrenda altar header."""
    console.print(OFRENDA_BANNER)
    console.print(SUGAR_SKULL)
    table = Table(show_header=False, box=None, padding=(0, 2))
    table.add_row("[bold gold1]Honored Ancestor:[/bold gold1]", f"[bold white]{name}[/bold white]")
    table.add_row("[bold gold1]Era of Impact:[/bold gold1]", f"[italic dim white]{era}[/italic dim white]")
    table.add_row("[bold gold1]Altar Offerings:[/bold gold1]", f"[italic bright_yellow]{offering}[/italic bright_yellow]")
    console.print(Panel(table, border_style="gold1", title="[bold gold1]🌼 VELADORAS & CEMPASÚCHIL 🌼[/bold gold1]"))


def print_autopsy_header(target: str) -> None:
    """Print the post-mortem autopsy header."""
    console.print(TOMBSTONE_ART)
    console.print(
        Panel(
            f"[bold red]Subject of Autopsy:[/bold red] [white]{target}[/white]\n"
            f"[dim italic]Commencing Victorian digital post-mortem examination...[/dim italic]",
            border_style="red",
            title="[bold red]⚰️ DIGITAL CORONER'S SLAB[/bold red]",
        )
    )


def stream_spooky_tokens(token_generator: Iterable[str]) -> str:
    """Stream tokens live to terminal with typewriter atmospheric pacing."""
    collected: list[str] = []
    for token in token_generator:
        collected.append(token)
        sys.stdout.write(token)
        sys.stdout.flush()
    sys.stdout.write("\n")
    sys.stdout.flush()
    return "".join(collected)


def print_eerie_box(title: str, content: str, border_style: str = "purple") -> None:
    """Print a styled gothic panel."""
    console.print(Panel(content, title=f"[bold]{title}[/bold]", border_style=border_style, padding=(1, 2)))


def print_whisper(whisper: str) -> None:
    """Print an eerie whisper from the machine."""
    console.print(f"\n[bold purple]👁️ [italic]The ghost in the machine whispers:[/italic][/bold purple] [bold cyan]\"{whisper}\"[/bold cyan]\n")
