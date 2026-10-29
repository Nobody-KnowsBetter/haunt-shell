"""Async HTTP client for local Ollama open-weight AI inference."""

from __future__ import annotations

import json
from typing import AsyncIterator, List, Optional
import httpx
from hauntshell.config import HauntConfig


class OllamaClient:
    """Async client communicating with local Ollama runtime."""

    def __init__(self, config: Optional[HauntConfig] = None):
        self.config = config or HauntConfig.load()
        self.base_url = self.config.ollama_url.rstrip("/")
        self.timeout = self.config.timeout
        self._client: Optional[httpx.AsyncClient] = None

    async def get_client(self) -> httpx.AsyncClient:
        """Get or initialize the persistent async HTTP client."""
        if self._client is None or self._client.is_closed:
            self._client = httpx.AsyncClient(base_url=self.base_url, timeout=self.timeout)
        return self._client

    async def close(self) -> None:
        """Close client session."""
        if self._client and not self._client.is_closed:
            await self._client.aclose()

    async def is_available(self) -> bool:
        """Check if local Ollama daemon is reachable."""
        try:
            client = await self.get_client()
            resp = await client.get("/api/tags", timeout=3.0)
            return resp.status_code == 200
        except Exception:
            return False

    async def list_models(self) -> List[str]:
        """Fetch list of locally installed open-weight models."""
        try:
            client = await self.get_client()
            resp = await client.get("/api/tags")
            if resp.status_code == 200:
                data = resp.json()
                return [m.get("name", "") for m in data.get("models", [])]
        except Exception:
            pass
        return []

    async def has_model(self, model_name: str) -> bool:
        """Check if a specific model or base tag exists locally."""
        installed = await self.list_models()
        model_name = model_name.lower().split(":")[0]
        return any(model_name in m.lower() for m in installed)

    async def stream_generate(
        self, prompt: str, system: str = "", model: Optional[str] = None
    ) -> AsyncIterator[str]:
        """Stream tokens from Ollama /api/generate endpoint."""
        target_model = model or self.config.model
        client = await self.get_client()
        payload = {
            "model": target_model,
            "prompt": prompt,
            "system": system,
            "stream": True,
            "options": {
                "temperature": 0.8,
                "top_p": 0.9,
            },
        }

        async with client.stream("POST", "/api/generate", json=payload) as resp:
            resp.raise_for_status()
            async for line in resp.aiter_lines():
                if not line:
                    continue
                try:
                    chunk = json.loads(line)
                    token = chunk.get("response", "")
                    if token:
                        yield token
                    if chunk.get("done", False):
                        break
                except json.JSONDecodeError:
                    continue

    async def generate(self, prompt: str, system: str = "", model: Optional[str] = None) -> str:
        """Generate full response without streaming."""
        tokens: List[str] = []
        async for token in self.stream_generate(prompt, system=system, model=model):
            tokens.append(token)
        return "".join(tokens)
