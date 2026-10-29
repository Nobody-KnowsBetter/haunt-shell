"""Tests for HauntEngine coordination and streaming."""

import pytest
from hauntshell.config import HauntConfig
from hauntshell.engine import HauntEngine
from hauntshell.spirits import get_spirit
from hauntshell.ofrenda import get_pioneer
from hauntshell.autopsy import prepare_autopsy_subject


@pytest.mark.asyncio
async def test_engine_offline_mode():
    cfg = HauntConfig(offline=True)
    engine = HauntEngine(cfg)

    assert not await engine.can_use_ollama()

    # Test command commentary streaming
    tokens = []
    async for chunk in engine.stream_command_commentary("rm -rf temp", 0):
        tokens.append(chunk)
    result = "".join(tokens)
    assert "Act of Deletion" in result

    # Test seance dialogue streaming
    spirit = get_spirit("clippy")
    assert spirit is not None
    tokens = []
    async for chunk in engine.stream_seance_dialogue(spirit, "Hello"):
        tokens.append(chunk)
    result = "".join(tokens)
    assert "paperclip" in result.lower()

    # Test ofrenda calaverita streaming
    pioneer = get_pioneer("ada")
    assert pioneer is not None
    tokens = []
    async for chunk in engine.stream_ofrenda_calaverita(pioneer):
        tokens.append(chunk)
    result = "".join(tokens)
    assert "Ada" in result

    # Test autopsy streaming
    subject = prepare_autopsy_subject("ValueError: null pointer")
    tokens = []
    async for chunk in engine.stream_autopsy(subject):
        tokens.append(chunk)
    result = "".join(tokens)
    assert "The Mortal Wound" in result
