"""Tests for the Día de los Muertos ofrenda registry and Calaveritas."""

from hauntshell.ofrenda import get_pioneer, list_pioneers, PIONEERS


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
