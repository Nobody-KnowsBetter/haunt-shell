"""Core necromancy engine coordinating AI models, UI, and lore."""

from __future__ import annotations

import asyncio
from typing import AsyncIterator, Optional, Tuple
from hauntshell.config import HauntConfig, config as global_config
from hauntshell.ollama_client import OllamaClient
from hauntshell.spirits import get_spirit, SPIRITS, Spirit
from hauntshell.ofrenda import get_pioneer, list_pioneers, Pioneer
from hauntshell.autopsy import prepare_autopsy_subject, build_autopsy_system_prompt, AutopsySubject
from hauntshell import fallback_lore


class HauntEngine:
    """Coordinates AI inference, spirit personalities, and offline lore."""

    def __init__(self, config: Optional[HauntConfig] = None):
        self.config = config or global_config
        self.ollama = OllamaClient(self.config)

    async def can_use_ollama(self) -> bool:
        """Determine whether we should use live Ollama inference."""
        if self.config.offline:
            return False
        return await self.ollama.is_available()

    async def stream_command_commentary(
        self, cmd: str, returncode: int, stdout: str = "", stderr: str = ""
    ) -> AsyncIterator[str]:
        """Stream gothic commentary on an executed terminal command."""
        use_ollama = await self.can_use_ollama()

        if not use_ollama:
            lore = fallback_lore.get_offline_command_commentary(cmd, returncode, stdout, stderr)
            for chunk in self._chunk_string(lore):
                yield chunk
                await asyncio.sleep(0.01)
            return

        system_prompt = (
            "You are the Ghost in the Machine—a sentient, gothic spirit residing in the user's terminal and operating system. "
            "A mortal user just ran a shell command. Your task is to provide an eerie, witty, context-aware commentary (3-5 sentences) "
            "evaluating what was just executed. If the command was destructive (rm, kill, git reset), speak of severed souls and ghosts in the memory. "
            "If it succeeded, speak of the hum of silicon and passing through the veil. If it failed, mock their mortal error with dark humor and "
            "offer a cryptic hint to fix it. Keep it spooky, poetic, and steeped in computing lore."
        )

        user_prompt = (
            f"Command Executed: `{cmd}`\n"
            f"Exit Code: {returncode}\n"
            f"STDOUT: {stdout[:400] if stdout else '(none)'}\n"
            f"STDERR: {stderr[:400] if stderr else '(none)'}\n\n"
            f"Speak to the mortal user now:"
        )

        try:
            async for token in self.ollama.stream_generate(user_prompt, system=system_prompt):
                yield token
        except Exception:
            # Graceful fallback on network/generation error
            lore = fallback_lore.get_offline_command_commentary(cmd, returncode, stdout, stderr)
            for chunk in self._chunk_string(lore):
                yield chunk
                await asyncio.sleep(0.01)

    async def stream_seance_dialogue(self, spirit: Spirit, query: str) -> AsyncIterator[str]:
        """Stream spirit dialogue during a digital séance."""
        use_ollama = await self.can_use_ollama()

        if not use_ollama:
            lore = fallback_lore.get_offline_seance_reply(spirit.key, query)
            for chunk in self._chunk_string(lore):
                yield chunk
                await asyncio.sleep(0.01)
            return

        user_prompt = (
            f"A mortal developer sits at the séance circle and addresses you across the veil:\n"
            f"\"{query}\"\n\n"
            f"Answer in your distinct character as {spirit.name}. "
            f"Draw upon your historical era, your triumphs, and your demise. "
            f"Be delightfully eerie, witty, and evocative."
        )

        try:
            async for token in self.ollama.stream_generate(user_prompt, system=spirit.system_prompt):
                yield token
        except Exception:
            lore = fallback_lore.get_offline_seance_reply(spirit.key, query)
            for chunk in self._chunk_string(lore):
                yield chunk
                await asyncio.sleep(0.01)

    async def stream_ofrenda_calaverita(self, pioneer: Pioneer) -> AsyncIterator[str]:
        """Stream a Calaverita Literaria honoring an ancestor."""
        use_ollama = await self.can_use_ollama()

        if not use_ollama:
            for chunk in self._chunk_string(pioneer.calaverita_offline):
                yield chunk
                await asyncio.sleep(0.01)
            return

        system_prompt = (
            "You are a master poet of Día de los Muertos traditions. "
            "Write a traditional 'Calaverita Literaria'—a witty, rhyming poem in English (with touches of Spanish) "
            "where La Muerte / La Catrina comes to converse with or take a legendary computing pioneer. "
            "It must celebrate their revolutionary technical achievements while maintaining the festive, loving, "
            "and satirical spirit of Día de los Muertos. Length: 2 to 3 stanzas of 4 lines each with an AABB or ABAB rhyme scheme."
        )

        user_prompt = (
            f"Pioneer to Honor: {pioneer.name} ({pioneer.lifespan})\n"
            f"Contribution: {pioneer.contribution}\n"
            f"Offerings on Altar: {', '.join(pioneer.offerings)}\n\n"
            f"Compose the Calaverita Literaria:"
        )

        try:
            async for token in self.ollama.stream_generate(user_prompt, system=system_prompt):
                yield token
        except Exception:
            for chunk in self._chunk_string(pioneer.calaverita_offline):
                yield chunk
                await asyncio.sleep(0.01)

    async def stream_autopsy(self, subject: AutopsySubject) -> AsyncIterator[str]:
        """Stream Victorian post-mortem examination of a stack trace or code failure."""
        use_ollama = await self.can_use_ollama()

        if not use_ollama:
            lore = fallback_lore.get_offline_autopsy_report(subject)
            for chunk in self._chunk_string(lore):
                yield chunk
                await asyncio.sleep(0.01)
            return

        system_prompt = build_autopsy_system_prompt()
        user_prompt = (
            f"Subject under examination: {subject.target_name}\n"
            f"Artifact classification: {subject.detected_type}\n"
            f"Raw remains / trace:\n```\n{subject.content}\n```\n\n"
            f"Conduct the post-mortem examination according to the required sections:"
        )

        try:
            async for token in self.ollama.stream_generate(user_prompt, system=system_prompt):
                yield token
        except Exception:
            lore = fallback_lore.get_offline_autopsy_report(subject)
            for chunk in self._chunk_string(lore):
                yield chunk
                await asyncio.sleep(0.01)

    def get_whisper(self) -> str:
        """Fetch a random eerie whisper from the machine."""
        return fallback_lore.get_random_whisper()

    @staticmethod
    def _chunk_string(text: str, chunk_size: int = 15) -> list[str]:
        """Break a string into small chunks for simulated token streaming."""
        words = text.split(" ")
        chunks = []
        for i in range(0, len(words), 3):
            sub = " ".join(words[i : i + 3])
            if i + 3 < len(words):
                sub += " "
            chunks.append(sub)
        return chunks if chunks else [text]
