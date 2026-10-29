"""Tests for the Día de los Muertos ofrenda registry and Calaveritas."""

from pathlib import Path
from hauntshell.ofrenda import (
    get_pioneer,
    list_pioneers,
    PIONEERS,
    Remembrance,
    save_custom_remembrance,
    load_custom_remembrances,
)


def test_list_pioneers():
    pioneers = list_pioneers()
    assert len(pioneers) >= 5
    keys = [p.key for p in pioneers]
    assert "ada" in keys
    assert "turing" in keys
    assert "dennis" in keys
    assert "hopper" in keys
    assert "hamilton" in keys


def test_get_pioneer_exact():
    ada = get_pioneer("ada")
    assert ada is not None
    assert "Lovelace" in ada.name
    assert len(ada.offerings) >= 3
    assert "La Muerte" in ada.calaverita_offline or "Death" in ada.calaverita_offline


def test_get_pioneer_aliases():
    hopper = get_pioneer("gracehopper")
    assert hopper is not None and hopper.key == "hopper"

    dmr = get_pioneer("dmr")
    assert dmr is not None and dmr.key == "dennis"

    alan = get_pioneer("alan")
    assert alan is not None and alan.key == "turing"


def test_get_pioneer_nonexistent():
    assert get_pioneer("nonexistent_pioneer") is None


def test_custom_remembrance_lifecycle(tmp_path: Path):
    storage = tmp_path / "test_ofrendas.json"
    rem = Remembrance(
        name="Grandmother Elena",
        relationship="Abuela",
        lifespan="1930 – 2015",
        foods=["Tamales", "Pan dulce"],
        songs=["Cielito Lindo"],
        story="Taught us to cherish family every Sunday.",
        calaverita="La Catrina came dancing with flowers so sweet...",
    )
    save_custom_remembrance(rem, storage_path=storage)

    loaded = load_custom_remembrances(storage_path=storage)
    assert len(loaded) == 1
    assert loaded[0].name == "Grandmother Elena"
    assert loaded[0].foods == ["Tamales", "Pan dulce"]
    assert "Cielito Lindo" in loaded[0].songs

    # Update or duplicate check
    rem2 = Remembrance(
        name="Grandmother Elena",
        relationship="Abuela querida",
        lifespan="1930 – 2015",
        foods=["Tamales"],
        songs=["Cielito Lindo"],
        story="Updated story",
    )
    save_custom_remembrance(rem2, storage_path=storage)
    reloaded = load_custom_remembrances(storage_path=storage)
    assert len(reloaded) == 1
    assert reloaded[0].relationship == "Abuela querida"

