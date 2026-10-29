"""Tests for the spirits catalog and alias resolution."""

from hauntshell.spirits import get_spirit, list_spirits, SPIRITS


def test_list_spirits():
    spirits = list_spirits()
    assert len(spirits) >= 7
    keys = [s.key for s in spirits]
    assert "clippy" in keys
    assert "flash" in keys
    assert "cobol" in keys
    assert "netscape" in keys
    assert "ada" in keys
    assert "dennis" in keys
    assert "turing" in keys


def test_get_spirit_exact():
    clippy = get_spirit("clippy")
    assert clippy is not None
    assert "Clippy" in clippy.name
    assert "1997" in clippy.era
    assert len(clippy.catchphrases) > 0
    assert "paperclip" in clippy.system_prompt.lower()


def test_get_spirit_aliases():
    flash1 = get_spirit("actionscript")
    flash2 = get_spirit("flashplayer")
    assert flash1 is not None and flash1.key == "flash"
    assert flash2 is not None and flash2.key == "flash"

    ada = get_spirit("lovelace")
    assert ada is not None and ada.key == "ada"

    dennis = get_spirit("dmr")
    assert dennis is not None and dennis.key == "dennis"

    turing = get_spirit("alan")
    assert turing is not None and turing.key == "turing"

    cobol = get_spirit("mainframe")
    assert cobol is not None and cobol.key == "cobol"


def test_get_spirit_nonexistent():
    assert get_spirit("phantom_nonexistent_99") is None
