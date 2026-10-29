"""Configuration module for HauntShell."""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path
from dotenv import load_dotenv

# Load local .env if present
load_dotenv()


@dataclass
class HauntConfig:
    """Runtime configuration for HauntShell."""

    model: str = os.getenv("HAUNT_MODEL", "gemma3")
    ollama_url: str = os.getenv("HAUNT_OLLAMA_URL", "http://localhost:11434")
    offline: bool = os.getenv("HAUNT_OFFLINE", "false").lower() in ("true", "1", "yes")
    atmosphere: str = os.getenv("HAUNT_ATMOSPHERE", "high")  # low, medium, high
    timeout: float = float(os.getenv("HAUNT_TIMEOUT", "45.0"))

    @classmethod
    def load(cls) -> HauntConfig:
        """Load configuration from environment."""
        return cls()

    def update(self, **kwargs) -> HauntConfig:
        """Return a copy with updated attributes."""
        for key, value in kwargs.items():
            if hasattr(self, key) and value is not None:
                setattr(self, key, value)
        return self


# Global default configuration instance
config = HauntConfig.load()
