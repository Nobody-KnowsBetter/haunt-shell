"""Tests for the offline procedural lore engine."""

from hauntshell.fallback_lore import (
    get_random_whisper,
    get_offline_command_commentary,
    get_offline_seance_reply,
    get_offline_autopsy_report,
)
from hauntshell.autopsy import prepare_autopsy_subject


def test_random_whisper():
    whisper = get_random_whisper()
    assert isinstance(whisper, str)
    assert len(whisper) > 10


def test_offline_command_commentary_destructive():
    c1 = get_offline_command_commentary("rm -rf src/old", 0)
    assert "Act of Deletion" in c1
    assert "inodes" in c1.lower()

    c2 = get_offline_command_commentary("kill -9 5432", 0)
    assert "Grim Reaper" in c2
    assert "SIGKILL" in c2

    c3 = get_offline_command_commentary("git reset --hard HEAD~1", 0)
    assert "Temporal Severance" in c3
    assert "reflog" in c3


def test_offline_command_commentary_failure():
    c = get_offline_command_commentary("unknown_cmd", 127, "", "command not found")
    assert "Demonic Rupture" in c
    assert "Exit Code 127" in c
    assert "command not found" in c


def test_offline_seance_reply_spirits():
    for spirit_key in ["clippy", "flash", "cobol", "netscape", "ada", "dennis", "turing"]:
        reply = get_offline_seance_reply(spirit_key, "What is the meaning of life?")
        assert len(reply) > 50
        assert "meaning of life" in reply.lower() or "IDENTIFICATION DIVISION" in reply


def test_offline_autopsy_report():
    subject = prepare_autopsy_subject("Segmentation fault (core dumped)")
    report = get_offline_autopsy_report(subject)
    assert "Time & Context of Demise" in report
    assert "The Mortal Wound" in report
    assert "The Resurrection Rite" in report
