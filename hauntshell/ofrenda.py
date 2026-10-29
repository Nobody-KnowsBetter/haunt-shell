"""Día de los Muertos Altar (Ofrenda) & Calaveritas Literarias for HauntShell."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List, Optional


@dataclass
class Pioneer:
    """A departed computing pioneer honored in the digital ofrenda."""

    key: str
    name: str
    lifespan: str
    contribution: str
    altar_tier: int  # 1 to 7 in traditional ofrenda
    offerings: List[str]
    calaverita_offline: str


PIONEERS: Dict[str, Pioneer] = {
    "ada": Pioneer(
        key="ada",
        name="Ada Lovelace (Countess of Lovelace)",
        lifespan="1815 – 1852",
        contribution="The world's first computer programmer; visionary of poetical science.",
        altar_tier=7,
        offerings=[
            "🌼 Fresh Cempasúchil garlands from the English countryside",
            "📜 Bernoulli number computation tables woven on punched cards",
            "☕ Strong Earl Grey tea and fine ink for quill work",
            "🕯️ Glowing beeswax candles illuminating the Analytical Engine",
        ],
        calaverita_offline=(
            "La Muerte arrived with a bony decree,\n"
            "To audit the numbers of young Ada's spree.\n"
            "'Your Engine,' said Death, 'weaves a magical song,\n"
            "Come dance through the ether where spirits belong!'\n"
            "Now Ada writes loops in the starlight above,\n"
            "Her algorithms guided by science and love."
        ),
    ),
    "turing": Pioneer(
        key="turing",
        name="Alan Turing (OBE, FRS)",
        lifespan="1912 – 1954",
        contribution="Father of modern computer science, AI, and cryptanalysis of Enigma.",
        altar_tier=7,
        offerings=[
            "🍎 An untouched sweet apple, unblemished and free of poison",
            "⚙️ Brass Enigma cipher wheels and mechanical relays",
            "🌼 Bright marigold petals tracing Fibonacci phyllotaxis spirals",
            "🕯️ Veladora of deep blue flame guarding the universal machine",
        ],
        calaverita_offline=(
            "The Reaper approached with an Enigma in hand,\n"
            "Saying, 'Solve this decryption across the dark land.'\n"
            "Alan smiled at the cipher, cracked it in three,\n"
            "And asked La Catrina if machines could be free.\n"
            "They shared Pan de Muerto beneath the pale moon,\n"
            "Where code and philosophy sing the same tune."
        ),
    ),
    "dennis": Pioneer(
        key="dennis",
        name="Dennis Ritchie (dmr)",
        lifespan="1941 – 2011",
        contribution="Creator of the C programming language and co-architect of Unix.",
        altar_tier=6,
        offerings=[
            "☕ Endless mug of filter coffee with milk",
            "⌨️ A vintage DEC PDP-11 console terminal",
            "📜 The original 'The C Programming Language' K&R manuscript",
            "🌼 Orange cempasúchil marking the path from NULL to eternity",
        ],
        calaverita_offline=(
            "La Catrina tapped Dennis upon his old desk,\n"
            "Saying, 'Your language is neat, though the pointers grotesque!'\n"
            "Said Ritchie, 'Fear not, the allocation is fine,\n"
            "Just free every struct when you reach the deadline.'\n"
            "Now Unix pipes flow through the heavenly sphere,\n"
            "With Dennis dispensing quiet wisdom down here."
        ),
    ),
    "hopper": Pioneer(
        key="hopper",
        name="Rear Admiral Grace Hopper",
        lifespan="1906 – 1992",
        contribution="Pioneer of computer compilers, COBOL, and legendary Navy admiral.",
        altar_tier=6,
        offerings=[
            "🦋 The original moth from the Harvard Mark II relay (preserved in amber)",
            "📏 A 30cm nanosecond piece of copper wire",
            "☕ Navy black coffee in a heavy porcelain mug",
            "🌼 Golden marigolds saluting a courageous admiral",
        ],
        calaverita_offline=(
            "Death came aboard with an ominous grin,\n"
            "'It's time to set sail where no mortal has been!'\n"
            "Grace handed La Muerte a nanosecond wire,\n"
            "And compiled a new bridge through the cemetery fire.\n"
            "'Dare to change things,' she barked to the skies,\n"
            "And the moth on the altar fluttered and flies!"
        ),
    ),
    "hamilton": Pioneer(
        key="hamilton",
        name="Margaret Hamilton",
        lifespan="1936 – (Honored living ancestor of software engineering)",
        contribution="Director of the Apollo flight software team; coined 'software engineering'.",
        altar_tier=5,
        offerings=[
            "🚀 Stack of Apollo guidance computer listings as tall as herself",
            "🌙 Moonrock replica glowing with lunar luminescence",
            "🌼 Cempasúchil blossoms woven into flight telemetry antennas",
            "🕯️ Everlasting flame of asynchronous priority scheduling",
        ],
        calaverita_offline=(
            "La Catrina flew down to the Apollo 11,\n"
            "Planning to drag the whole module to heaven.\n"
            "Alarm 1202 flickered red on the screen—\n"
            "Yet Hamilton's software kept landing serene!\n"
            "Death paused in amazement: 'Your code is so tight,\n"
            "Even ghosts cannot crash this miraculous flight!'"
        ),
    ),
}


def get_pioneer(key: str) -> Optional[Pioneer]:
    """Look up an honored pioneer by key or alias."""
    key = key.lower().strip()
    aliases = {
        "lovelace": "ada",
        "alan": "turing",
        "ritchie": "dennis",
        "dmr": "dennis",
        "grace": "hopper",
        "gracehopper": "hopper",
        "margaret": "hamilton",
    }
    resolved = aliases.get(key, key)
    return PIONEERS.get(resolved)


def list_pioneers() -> List[Pioneer]:
    """Return all pioneers in the ofrenda registry."""
    return list(PIONEERS.values())
