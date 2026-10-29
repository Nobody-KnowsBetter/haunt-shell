"""Integration tests for Typer CLI commands."""

from typer.testing import CliRunner
from hauntshell.cli import app
from hauntshell import __version__

runner = CliRunner()


def test_cli_version():
    res = runner.invoke(app, ["version"])
    assert res.exit_code == 0
    assert __version__ in res.output


def test_cli_whisper():
    res = runner.invoke(app, ["whisper"])
    assert res.exit_code == 0
    assert "The ghost in the machine whispers:" in res.output


def test_cli_spirits():
    res = runner.invoke(app, ["spirits"])
    assert res.exit_code == 0
    assert "Clippy" in res.output
    assert "Adobe Flash" in res.output
    assert "Mainframe Lich" in res.output


def test_cli_ofrenda_list():
    res = runner.invoke(app, ["ofrenda"])
    assert res.exit_code == 0
    assert "EL GRAN ALTAR DE LOS ANCESTROS DIGITALES" in res.output
    assert "Ada Lovelace" in res.output
    assert "Alan Turing" in res.output


def test_cli_ofrenda_pioneer():
    res = runner.invoke(app, ["ofrenda", "ada", "--offline"])
    assert res.exit_code == 0
    assert "OFRENDA DIGITAL" in res.output
    assert "Ada Lovelace" in res.output
    assert "Calaverita Literaria" in res.output


def test_cli_ofrenda_invalid():
    res = runner.invoke(app, ["ofrenda", "nonexistent_ghost"])
    assert res.exit_code == 1
    assert "not found on the altar" in res.output


def test_cli_ofrenda_add_and_custom():
    user_inputs = "Uncle Carlos\nTio\n1950 – 2020\nPozole, Horchata\nMariachi\nAlways played acoustic guitar at festivals.\n"
    res_add = runner.invoke(app, ["ofrenda", "--add"], input=user_inputs)
    assert res_add.exit_code == 0
    assert "BUILD A PRIVATE DIGITAL OFRENDA" in res_add.output
    assert "Uncle Carlos" in res_add.output

    res_custom = runner.invoke(app, ["ofrenda", "--custom"])
    assert res_custom.exit_code == 0
    assert "TU ALTAR PRIVADO" in res_custom.output
    assert "Uncle Carlos" in res_custom.output
    assert "Pozole" in res_custom.output


def test_cli_seance_no_args():
    res = runner.invoke(app, ["seance"])
    assert res.exit_code == 0
    assert "Choose a spirit to summon" in res.output


def test_cli_seance_with_spirit():
    res = runner.invoke(app, ["seance", "clippy", "--query", "Are you alive?", "--offline"])
    assert res.exit_code == 0
    assert "THE SÉANCE CIRCLE" in res.output
    assert "Clippy the Undead Revenant" in res.output
    assert "paperclip" in res.output.lower()


def test_cli_seance_interactive_farewell():
    # User immediately enters 'farewell' to close circle
    res = runner.invoke(app, ["seance", "clippy", "-i", "--offline"], input="farewell\n")
    assert res.exit_code == 0
    assert "Séance Candles:" in res.output
    assert "dissolves into the ethereal mist" in res.output


def test_cli_chamber_command():
    res = runner.invoke(app, ["chamber", "clippy", "--offline"], input="quit\n")
    assert res.exit_code == 0
    assert "THE SÉANCE CIRCLE" in res.output
    assert "dissolves into the ethereal mist" in res.output


def test_cli_seance_invalid_spirit():
    res = runner.invoke(app, ["seance", "invalid_ghost"])
    assert res.exit_code == 1
    assert "not found in the necro-registry" in res.output


def test_cli_exec_command():
    res = runner.invoke(app, ["exec", "echo 'hello mortal'", "--offline"])
    assert res.exit_code == 0
    assert "Executing in the mortal realm" in res.output
    assert "hello mortal" in res.output
    assert "The Machine Murmurs" in res.output


def test_cli_exec_quiet():
    res = runner.invoke(app, ["exec", "echo 'secret'", "--offline", "--quiet"])
    assert res.exit_code == 0
    assert "STDOUT" not in res.output
    assert "The Machine Murmurs" in res.output


def test_cli_autopsy_command():
    res = runner.invoke(app, ["autopsy", "NullPointerException: pointer was 0x0", "--offline"])
    assert res.exit_code == 0
    assert "DIGITAL CORONER'S SLAB" in res.output
    assert "The Mortal Wound" in res.output
    assert "The Resurrection Rite" in res.output


def test_cli_config_command():
    res = runner.invoke(app, ["config"])
    assert res.exit_code == 0
    assert "HAUNTSHELL CONFIGURATION" in res.output
    assert "gemma" in res.output.lower()
