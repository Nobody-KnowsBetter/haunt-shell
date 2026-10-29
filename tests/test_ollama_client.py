"""Tests for OllamaClient streaming and availability checks."""

import json
import pytest
from unittest.mock import AsyncMock, patch, MagicMock
from hauntshell.config import HauntConfig
from hauntshell.ollama_client import OllamaClient


@pytest.mark.asyncio
async def test_ollama_client_is_available_true():
    client = OllamaClient()
    mock_resp = MagicMock()
    mock_resp.status_code = 200

    with patch("httpx.AsyncClient.get", new_callable=AsyncMock) as mock_get:
        mock_get.return_value = mock_resp
        assert await client.is_available() is True
    await client.close()


@pytest.mark.asyncio
async def test_ollama_client_is_available_false():
    client = OllamaClient()

    with patch("httpx.AsyncClient.get", new_callable=AsyncMock) as mock_get:
        mock_get.side_effect = Exception("Connection refused")
        assert await client.is_available() is False
    await client.close()


@pytest.mark.asyncio
async def test_ollama_client_list_models():
    client = OllamaClient()
    mock_resp = MagicMock()
    mock_resp.status_code = 200
    mock_resp.json.return_value = {
        "models": [{"name": "gemma3:latest"}, {"name": "llama3.2:latest"}]
    }

    with patch("httpx.AsyncClient.get", new_callable=AsyncMock) as mock_get:
        mock_get.return_value = mock_resp
        models = await client.list_models()
        assert "gemma3:latest" in models
        assert await client.has_model("gemma3") is True
        assert await client.has_model("codellama") is False
    await client.close()


@pytest.mark.asyncio
async def test_ollama_stream_generate():
    client = OllamaClient()

    ndjson_lines = [
        json.dumps({"response": "The ", "done": False}),
        json.dumps({"response": "veil ", "done": False}),
        json.dumps({"response": "thins.", "done": True}),
    ]

    class FakeStreamContext:
        def __init__(self, lines):
            self.lines = lines

        async def __aenter__(self):
            resp = MagicMock()
            resp.raise_for_status = MagicMock()

            async def fake_iter_lines():
                for line in self.lines:
                    yield line

            resp.aiter_lines = fake_iter_lines
            return resp

        async def __aexit__(self, exc_type, exc_val, exc_tb):
            pass

    with patch("httpx.AsyncClient.stream", return_value=FakeStreamContext(ndjson_lines)):
        tokens = []
        async for token in client.stream_generate("Summon spirit"):
            tokens.append(token)
        assert "".join(tokens) == "The veil thins."

    await client.close()
