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
from hauntshell.ofrenda import get_pioneer, list_pioneers
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

    if not query:
        query = typer.prompt("🔮 Inquire of the spirit")

    console.print(f"\n[bold white]Mortal Inquiry:[/bold white] [italic]\"{query}\"[/italic]\n")
    console.print(f"[dim purple]* Chanting hex incantations... {spirit.avatar} materializes *[/dim purple]\n")

    engine = get_configured_engine(offline=offline, model=model)

    async def _run():
        tokens = engine.stream_seance_dialogue(spirit, query)
        async for token in tokens:
            sys.stdout.write(token)
            sys.stdout.flush()
        sys.stdout.write("\n\n")

    asyncio.run(_run())


@app.command("ofrenda")
def ofrenda_command(
    pioneer_name: Optional[str] = typer.Argument(None, help="Pioneer to honor (ada, turing, dennis, hopper, hamilton)"),
    offline: bool = typer.Option(False, "--offline", "-o", help="Force local offline lore without Ollama"),
    model: Optional[str] = typer.Option(None, "--model", "-m", help="Override AI model"),
) -> None:
    """Visit the Día de los Muertos digital ofrenda and read traditional Calaveritas Literarias."""
    print_banner()

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
        console.print("\n[bold gold1]To place offerings and hear a Calaverita Literaria for a pioneer:[/bold gold1]")
        console.print("[italic white]haunt ofrenda <key>  (e.g. 'haunt ofrenda ada')[/italic white]\n")
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
