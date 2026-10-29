"""Typer command-line interface for HauntShell 👻."""

from __future__ import annotations

import asyncio
import subprocess
import sys
from typing import Optional
import typer
from rich.table import Table
from rich.panel import Panel

from hauntshell import __version__
from hauntshell.config import HauntConfig, config as global_config
from hauntshell.engine import HauntEngine
from hauntshell.spirits import get_spirit, list_spirits
from hauntshell.ofrenda import (
    get_pioneer,
    list_pioneers,
    Remembrance,
    load_custom_remembrances,
    save_custom_remembrance,
)
from hauntshell.autopsy import prepare_autopsy_subject
from hauntshell.ui import (
    console,
    print_banner,
    print_seance_header,
    print_ofrenda_header,
    print_autopsy_header,
    stream_spooky_tokens,
    print_whisper,
    print_eerie_box,
    CANDLES,
    get_candle_display,
)

app = typer.Typer(
    name="haunt",
    help="HauntShell 👻 - The Ghost in the Machine. Open-weight AI terminal necromancer for Halloween and Día de los Muertos.",
    no_args_is_help=True,
    add_completion=False,
)


def get_configured_engine(offline: bool = False, model: Optional[str] = None) -> HauntEngine:
    """Create a HauntEngine instance honoring CLI flags."""
    cfg = HauntConfig.load()
    if offline:
        cfg.offline = True
    if model:
        cfg.model = model
    return HauntEngine(cfg)


@app.command("exec")
def exec_command(
    command_str: str = typer.Argument(..., help="Shell command to execute under the ghost's watch (e.g. 'kill -9 1234', 'rm test.txt')"),
    offline: bool = typer.Option(False, "--offline", "-o", help="Force local offline lore without calling Ollama"),
    model: Optional[str] = typer.Option(None, "--model", "-m", help="Override AI model (e.g. gemma3, gemma2, llama3.2)"),
    quiet: bool = typer.Option(False, "--quiet", "-q", help="Suppress raw command output and show only the ghost's commentary"),
) -> None:
    """Execute a shell command with the Ghost in the Machine watching over your shoulder."""
    print_banner()

    if not quiet:
        console.print(f"[bold cyan]⚡ Executing in the mortal realm:[/bold cyan] [white]{command_str}[/white]\n")

    # Run the actual command
    try:
        proc = subprocess.run(command_str, shell=True, capture_output=True, text=True)
        stdout = proc.stdout
        stderr = proc.stderr
        returncode = proc.returncode
    except Exception as exc:
        stdout = ""
        stderr = str(exc)
        returncode = 1

    if not quiet:
        if stdout:
            console.print(Panel(stdout.strip(), title="[dim]STDOUT[/dim]", border_style="dim white"))
        if stderr:
            console.print(Panel(stderr.strip(), title="[red]STDERR[/red]", border_style="red"))

    console.print(f"\n[dim purple]* The silicon whispers... exit code {returncode} *[/dim purple]\n")

    engine = get_configured_engine(offline=offline, model=model)

    async def _run():
        tokens = engine.stream_command_commentary(command_str, returncode, stdout, stderr)
        async for token in tokens:
            sys.stdout.write(token)
            sys.stdout.flush()
        sys.stdout.write("\n")

    asyncio.run(_run())


@app.command("run")
def run_command_alias(
    command_str: str = typer.Argument(..., help="Shell command to execute"),
    offline: bool = typer.Option(False, "--offline", "-o", help="Force local offline lore"),
    model: Optional[str] = typer.Option(None, "--model", "-m", help="Override AI model"),
) -> None:
    """Alias for 'haunt exec'."""
    exec_command(command_str=command_str, offline=offline, model=model, quiet=False)


@app.command("seance")
def seance_command(
    spirit_name: Optional[str] = typer.Argument(None, help="Spirit to summon (clippy, flash, cobol, netscape, ada, dennis, turing)"),
    query: Optional[str] = typer.Option(None, "--query", "-q", help="Inquiry for the spirit across the veil"),
    interactive: bool = typer.Option(False, "--interactive", "-i", help="Enter multi-turn interactive séance chamber"),
    offline: bool = typer.Option(False, "--offline", "-o", help="Force local offline lore without Ollama"),
    model: Optional[str] = typer.Option(None, "--model", "-m", help="Override AI model"),
) -> None:
    """Hold an offline séance with the digital ghost of a departed technology or computing pioneer."""
    print_banner()

    if not spirit_name:
        console.print("[bold purple]🕯️ Choose a spirit to summon from the veil:[/bold purple]\n")
        spirits_command()
        console.print("\n[italic dim]Usage: haunt seance <spirit_name> --query \"your question\"[/italic dim]\n")
        return

    spirit = get_spirit(spirit_name)
    if not spirit:
        console.print(f"[bold red]❌ Spirit '{spirit_name}' not found in the necro-registry.[/bold red]")
        console.print("[dim]Use 'haunt spirits' to view summonable entities.[/dim]")
        raise typer.Exit(code=1)

    print_seance_header(spirit.name, spirit.era)
    console.print(f"[italic cyan]Epitaph: \"{spirit.epitaph}\"[/italic cyan]\n")

    engine = get_configured_engine(offline=offline, model=model)

    # Multi-turn interactive mode
    if interactive or not query:
        console.print("[dim gold1]* Type 'farewell', 'exit', or 'quit' to close the séance circle *[/dim gold1]\n")
        max_turns = 5
        turn = 0

        while turn < max_turns:
            candle_status = get_candle_display(turn, max_turns)
            console.print(f"[bold gold1]Séance Candles:[/bold gold1] {candle_status}")
            user_input = typer.prompt("🔮 Inquire of the spirit")

            if user_input.lower().strip() in ("exit", "quit", "farewell", "goodbye", "bye", "adios"):
                console.print(f"\n[italic purple]* You bid farewell. {spirit.name} dissolves into the ethereal mist. *[/italic purple]\n")
                return

            console.print(f"\n[bold white]Mortal Inquiry:[/bold white] [italic]\"{user_input}\"[/italic]\n")
            console.print(f"[dim purple]* Chanting hex incantations... {spirit.avatar} responds *[/dim purple]\n")

            async def _run_turn(q=user_input):
                tokens = engine.stream_seance_dialogue(spirit, q)
                async for token in tokens:
                    sys.stdout.write(token)
                    sys.stdout.flush()
                sys.stdout.write("\n\n")

            asyncio.run(_run_turn())
            turn += 1

        console.print("[italic red]💨 The last candle has burned out. The veil between worlds seals shut.[/italic red]\n")
        return

    # Single-query mode
    console.print(f"\n[bold white]Mortal Inquiry:[/bold white] [italic]\"{query}\"[/italic]\n")
    console.print(f"[dim purple]* Chanting hex incantations... {spirit.avatar} materializes *[/dim purple]\n")

    async def _run():
        tokens = engine.stream_seance_dialogue(spirit, query)
        async for token in tokens:
            sys.stdout.write(token)
            sys.stdout.flush()
        sys.stdout.write("\n\n")

    asyncio.run(_run())


@app.command("chamber")
def chamber_command(
    spirit_name: Optional[str] = typer.Argument(None, help="Spirit to summon in the interactive chamber"),
    offline: bool = typer.Option(False, "--offline", "-o", help="Force local offline lore"),
    model: Optional[str] = typer.Option(None, "--model", "-m", help="Override AI model"),
) -> None:
    """Enter the interactive multi-turn séance chamber with burning candle physics."""
    seance_command(spirit_name=spirit_name, query=None, interactive=True, offline=offline, model=model)


@app.command("ofrenda")
def ofrenda_command(
    pioneer_name: Optional[str] = typer.Argument(None, help="Pioneer to honor (ada, turing, dennis, hopper, hamilton)"),
    add: bool = typer.Option(False, "--add", "-a", help="Interactively add a private remembrance for a loved one"),
    custom: bool = typer.Option(False, "--custom", "-c", help="View personal family and loved one remembrances"),
    offline: bool = typer.Option(False, "--offline", "-o", help="Force local offline lore without Ollama"),
    model: Optional[str] = typer.Option(None, "--model", "-m", help="Override AI model"),
) -> None:
    """Visit the Día de los Muertos digital ofrenda and read traditional Calaveritas Literarias."""
    print_banner()

    # 1. Handle adding private remembrance
    if add:
        console.print("[bold gold1]🌼 BUILD A PRIVATE DIGITAL OFRENDA (100% OFFLINE) 🌼[/bold gold1]\n")
        console.print("[italic dim]Your memories, favorite foods, and stories remain 100% on your own device.[/italic dim]\n")
        name = typer.prompt("Name of your loved one or mentor")
        relationship = typer.prompt("Relationship (e.g. Grandmother, Father, Mentor, Friend)")
        lifespan = typer.prompt("Lifespan or dates (e.g. 1935 – 2018)")
        foods_raw = typer.prompt("Favorite foods, treats, or offerings (comma-separated)")
        songs_raw = typer.prompt("Favorite songs, hymns, or melodies (comma-separated)")
        story = typer.prompt("A cherished memory or story to preserve")

        foods = [f.strip() for f in foods_raw.split(",") if f.strip()]
        songs = [s.strip() for s in songs_raw.split(",") if s.strip()]

        default_calaverita = (
            f"La Catrina arrived with bright marigolds in hand,\n"
            f"Seeking dear {name} across the quiet land.\n"
            f"With songs of {songs[0] if songs else 'the guitar'} and plates of {foods[0] if foods else 'sweet bread'},\n"
            f"Their laughter still echoes where memories tread.\n"
            f"Now resting in peace where bright spirits belong,\n"
            f"Forever remembered in story and song."
        )

        rem = Remembrance(
            name=name,
            relationship=relationship,
            lifespan=lifespan,
            foods=foods,
            songs=songs,
            story=story,
            calaverita=default_calaverita,
        )
        save_custom_remembrance(rem)
        console.print(f"\n[bold green]✓ A place of honor for {name} has been lovingly prepared on your altar.[/bold green]")
        console.print("[dim]View your personal altar anytime with: haunt ofrenda --custom[/dim]\n")
        return

    # 2. Handle viewing private remembrances
    if custom:
        rems = load_custom_remembrances()
        if not rems:
            console.print("[dim yellow]No personal remembrances on your altar yet. Add one with: haunt ofrenda --add[/dim yellow]\n")
            return
        console.print("[bold gold1]🌼 🕯️  TU ALTAR PRIVADO DE SERES QUERIDOS  🕯️ 🌼[/bold gold1]\n")
        for r in rems:
            foods_str = ", ".join(r.foods) if r.foods else "None recorded"
            songs_str = ", ".join(r.songs) if r.songs else "None recorded"
            table = Table(show_header=False, box=None)
            table.add_row("[bold gold1]Loved One:[/bold gold1]", f"[bold white]{r.name}[/bold white] ({r.relationship})")
            table.add_row("[bold gold1]Years:[/bold gold1]", f"[dim]{r.lifespan}[/dim]")
            table.add_row("[bold gold1]Offerings / Foods:[/bold gold1]", f"[italic]{foods_str}[/italic]")
            table.add_row("[bold gold1]Favorite Music:[/bold gold1]", f"[italic]{songs_str}[/italic]")
            table.add_row("[bold gold1]Story Kept:[/bold gold1]", f"\"{r.story}\"")
            console.print(Panel(table, border_style="gold1", title=f"[bold gold1]🕯️ {r.name} ({r.lifespan}) 🕯️[/bold gold1]"))
            if r.calaverita:
                console.print(f"[italic gold1]{r.calaverita}[/italic gold1]\n")
        return

    if not pioneer_name:
        # Show all pioneers on the altar
        console.print("[bold gold1]🌼 🕯️  EL GRAN ALTAR DE LOS ANCESTROS DIGITALES  🕯️ 🌼[/bold gold1]\n")
        table = Table(border_style="gold1")
        table.add_column("Key", style="bold magenta")
        table.add_column("Ancestor", style="bold white")
        table.add_column("Lifespan", style="italic dim")
        table.add_column("Historic Contribution", style="cyan")

        for p in list_pioneers():
            table.add_row(p.key, p.name, p.lifespan, p.contribution)

        console.print(table)

        # Check if user has personal tributes
        custom_rems = load_custom_remembrances()
        if custom_rems:
            console.print(f"\n[italic gold1]🕯️ You have {len(custom_rems)} personal loved ones on your private altar. View with: haunt ofrenda --custom[/italic gold1]")

        console.print("\n[bold gold1]To honor an ancestor or add a loved one:[/bold gold1]")
        console.print("[italic white]haunt ofrenda <key>     (e.g. 'haunt ofrenda ada')[/italic white]")
        console.print("[italic white]haunt ofrenda --add     (add a personal loved one)[/italic white]\n")
        return

    pioneer = get_pioneer(pioneer_name)
    if not pioneer:
        console.print(f"[bold red]❌ Pioneer '{pioneer_name}' not found on the altar.[/bold red]")
        console.print("[dim]Use 'haunt ofrenda' to list honored ancestors.[/dim]")
        raise typer.Exit(code=1)

    offerings_str = "\n".join(pioneer.offerings)
    print_ofrenda_header(pioneer.name, pioneer.lifespan, offerings_str)

    console.print(f"\n[bold gold1]💀 Calaverita Literaria for {pioneer.name}:[/bold gold1]\n")

    engine = get_configured_engine(offline=offline, model=model)

    async def _run():
        tokens = engine.stream_ofrenda_calaverita(pioneer)
        async for token in tokens:
            sys.stdout.write(token)
            sys.stdout.flush()
        sys.stdout.write("\n\n")

    asyncio.run(_run())


@app.command("autopsy")
def autopsy_command(
    target: str = typer.Argument(..., help="Path to a crashed script, stack trace file, or inline error text"),
    offline: bool = typer.Option(False, "--offline", "-o", help="Force local offline lore without Ollama"),
    model: Optional[str] = typer.Option(None, "--model", "-m", help="Override AI model"),
) -> None:
    """Perform a Victorian digital post-mortem on a stack trace, segfault, or dead code."""
    print_banner()
    print_autopsy_header(target)

    subject = prepare_autopsy_subject(target)
    console.print(f"[dim white]Classification: [bold cyan]{subject.detected_type}[/bold cyan][/dim white]\n")

    engine = get_configured_engine(offline=offline, model=model)

    async def _run():
        tokens = engine.stream_autopsy(subject)
        async for token in tokens:
            sys.stdout.write(token)
            sys.stdout.flush()
        sys.stdout.write("\n\n")

    asyncio.run(_run())


@app.command("spirits")
def spirits_command() -> None:
    """List all summonable spirits in the digital séance registry."""
    table = Table(title="[bold purple]🔮 PANTHEON OF SUMMONABLE DIGITAL SPIRITS[/bold purple]", border_style="purple")
    table.add_column("Key", style="bold magenta", width=10)
    table.add_column("Spirit", style="bold white", width=28)
    table.add_column("Era of Demise", style="italic dim cyan", width=28)
    table.add_column("Epitaph", style="dim", width=40)

    for s in list_spirits():
        table.add_row(s.key, f"{s.avatar} {s.name}", s.era, s.epitaph)

    console.print(table)


@app.command("whisper")
def whisper_command() -> None:
    """Listen to an eerie whisper from unallocated sectors of your machine."""
    engine = get_configured_engine()
    whisper = engine.get_whisper()
    print_whisper(whisper)


@app.command("config")
def config_command() -> None:
    """Display current HauntShell configuration and test local Ollama connectivity."""
    print_banner()
    cfg = HauntConfig.load()

    table = Table(title="[bold cyan]⚙️ HAUNTSHELL CONFIGURATION[/bold cyan]", border_style="cyan")
    table.add_column("Setting", style="bold white")
    table.add_column("Value", style="cyan")

    table.add_row("Open-Weight Model", cfg.model)
    table.add_row("Ollama Base URL", cfg.ollama_url)
    table.add_row("Offline Mode Enforced", str(cfg.offline))
    table.add_row("Atmosphere Level", cfg.atmosphere)
    table.add_row("Inference Timeout", f"{cfg.timeout}s")

    console.print(table)

    # Test connectivity
    console.print("\n[dim]Testing local Ollama daemon connection...[/dim]")
    engine = HauntEngine(cfg)

    async def _check():
        available = await engine.ollama.is_available()
        if available:
            models = await engine.ollama.list_models()
            console.print(f"[bold green]✅ Connected to Ollama at {cfg.ollama_url}[/bold green]")
            console.print(f"[dim]Available local models: {', '.join(models) if models else '(none installed yet)'}[/dim]")
        else:
            console.print(f"[bold yellow]⚠️  Ollama daemon not detected at {cfg.ollama_url}[/bold yellow]")
            console.print("[dim]HauntShell will automatically use its built-in offline necromancy engine.[/dim]")
            console.print("[dim]To run local open-weight AI: start Ollama with 'ollama serve' and run 'ollama pull gemma3'[/dim]")

    asyncio.run(_check())


@app.command("version")
def version_command() -> None:
    """Show HauntShell version."""
    console.print(f"[bold magenta]HauntShell[/bold magenta] version [bold cyan]{__version__}[/bold cyan]")
