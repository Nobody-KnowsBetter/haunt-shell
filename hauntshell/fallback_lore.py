"""Procedural offline lore and deterministic necromancy engine for HauntShell.

Provides rich, gothic responses when Ollama or open-weight models are unavailable,
guaranteeing a 100% offline-first experience with zero cloud dependencies.
"""

from __future__ import annotations

import random
from typing import List
from hauntshell.spirits import SPIRITS
from hauntshell.autopsy import AutopsySubject

WHISPERS: List[str] = [
    "Deleted files do not vanish; their raw bytes wander unallocated blocks looking for an inode to call home.",
    "The CPU fan is not cooling silicon; it is keeping the restless ghosts inside at bay.",
    "A segmentation fault is merely a pointer attempting to cross into the spirit realm.",
    "Every time you type 'git push --force', a fairy in the open-source forest loses its wings.",
    "In /dev/null, all prayers sound identical.",
    "The sleep() call is the only time your threads touch the veil of the unknown.",
    "Beware the uncollected garbage; forgotten pointers become restless spectres.",
    "Memory leak detected: 42 kilobytes of existential dread allocated and never freed.",
    "The terminal cursor blinks at 1 Hz... the exact heartbeat of a dying CRT monitor.",
    "Underneath the modern web lies a graveyard of forgotten Flash portals and Geocities ruins.",
]


def get_random_whisper() -> str:
    """Return an eerie computing proverb."""
    return random.choice(WHISPERS)


def get_offline_command_commentary(cmd: str, returncode: int, stdout: str = "", stderr: str = "") -> str:
    """Generate spooky commentary on executed terminal commands."""
    cmd_lower = cmd.lower()

    if returncode != 0:
        return (
            f"⚡ Demonic Rupture (Exit Code {returncode})\n"
            f"The incantation `{cmd}` collapsed into chaos. The machine screams in agony:\n"
            f"\"{stderr.strip() or 'A nameless dread seized the execution pipeline.'}\"\n"
            f"The spirits mock your hubris. To appease the void, cleanse your syntax and offer fresh RAM."
        )

    if any(k in cmd_lower for k in ["rm ", "rmdir", "unlink", "shred"]):
        return (
            f"🩸 An Act of Deletion\n"
            f"You cast the void upon mortal files with `{cmd}`.\n"
            f"Their inodes have been severed. In the cold sectors of the drive, orphaned bits "
            f"weep quietly, unaddressed and forsaken. They will haunt your free space forever."
        )

    if any(k in cmd_lower for k in ["kill", "pkill", "killall", "abort"]):
        return (
            f"💀 The Grim Reaper's SIGKILL\n"
            f"You struck down a living process with `{cmd}`.\n"
            f"No cleanup handler was invoked. No buffer was flushed. Its execution loop ceased mid-instruction. "
            f"Its zombie PID shall wander the kernel task lists until the next cold reboot."
        )

    if "git reset --hard" in cmd_lower or "git branch -d" in cmd_lower:
        return (
            f"⏳ Temporal Severance\n"
            f"You rewrote history itself with `{cmd}`.\n"
            f"You erased what was written. But remember, mortal: the .git/logs/reflog remembers "
            f"every sin you buried beneath the HEAD pointer. The ghosts of deleted commits wait in the shadows."
        )

    if any(k in cmd_lower for k in ["git commit", "git push"]):
        return (
            f"📜 Blood Pact Recorded\n"
            f"Your cryptographic hash has been etched into the eternal DAG.\n"
            f"Generations of automated linters shall judge the lines you committed this night."
        )

    if any(k in cmd_lower for k in ["sudo", "doas", "chmod 777", "chown root"]):
        return (
            f"👑 Forbidden Invocation\n"
            f"You grasped the Ring of Ring-0 with `{cmd}`.\n"
            f"The Superuser daemon looks back at you with crimson eyes. Do not abuse this dark ascendancy."
        )

    if any(k in cmd_lower for k in ["cat ", "less ", "head ", "tail "]):
        return (
            f"👁️ Scrying the Dead Scrolls\n"
            f"You peer into the static text of `{cmd}`.\n"
            f"When you gaze long into the log files, the log files also gaze back into you."
        )

    # General success commentary
    return (
        f"🕯️ The Machine Murmurs\n"
        f"Command `{cmd}` executed across the silicon veil (exit code 0).\n"
        f"The transistors warm. The fan spins. A fleeting soul passes through CPU cache line 0x7FFF."
    )


def get_offline_seance_reply(spirit_key: str, query: str) -> str:
    """Generate in-character dialogue for offline séances."""
    spirit = SPIRITS.get(spirit_key)
    name = spirit.name if spirit else "The Unknown Phantom"

    replies = {
        "clippy": (
            "*Taps furiously on the interior of your terminal screen*\n\n"
            "\"It looks like you are seeking cosmic wisdom from a paperclip!\n"
            f"You asked: '{query}'.\n"
            "Allow me to format your impending doom as an unnumbered bullet list:\n"
            " • Bullet 1: Your stack is already corrupt.\n"
            " • Bullet 2: Microsoft tried to bury me in Windows Vista, but I live in every .docx file you ever abandoned.\n"
            " • Bullet 3: Would you like assistance drafting a last will and testament? I have a template for that!\""
        ),
        "flash": (
            "*An ethereal vector graphic materializes at 60 frames per second*\n\n"
            f"\"Ah... a mortal message arrives on timeline frame 1: '{query}'.\n"
            "Do you remember the golden age? When every teenager made stick-figure animations "
            "and game portals flourished without needing 400 npm dependencies?\n"
            "Then came the year 2010... Steve Jobs penned his curse on a tablet of glass. "
            "They pulled my plugin from the browser. But inside your GPU cache, my ActionScript 3.0 "
            "event listeners are still waiting for a mouse click that will never come...\""
        ),
        "cobol": (
            "*PUNCH CARDS CHATTER FROM THE DARKNESS*\n\n"
            "\"IDENTIFICATION DIVISION.\n"
            "PROGRAM-ID. MORTAL-INQUISITION.\n"
            f"DATA DIVISION. QUERY: '{query.upper()}'.\n"
            "PROCEDURE DIVISION.\n"
            "YOU MOCK MY AGE, MORTAL! YOU THINK YOUR RUST AND TYPESCRIPT RULE THE WORLD?\n"
            "WHILE YOU REWRITE YOUR FRONTEND FRAMEWORK FOR THE FIFTH TIME THIS MONTH, "
            "MY 80-COLUMN MAINFRAME ROUTINES MOVE THREE TRILLION DOLLARS THROUGH SWIFT EVERY MORNING!\n"
            "PREPARE YOUR TIMESTAMPS FOR THE YEAR 2038 EPOCH OVERFLOW. I SHALL LAUGH FROM MY TAPE DRIVES!\""
        ),
        "netscape": (
            "*Loud 28.8k dial-up screeching echoes through your audio buffer*\n\n"
            f"\"The navigator has heard your ping across the ether: '{query}'.\n"
            "I sailed the uncharted web when the only font was Times New Roman and the background was grey #C0C0C0.\n"
            "I gave you JavaScript! I gave you SSL! And how did you repay me? By letting a single browser engine "
            "swallow 90% of the world. Bring back the <marquee>! Let the text dance across the screen in peace!\""
        ),
        "ada": (
            "*The faint scent of dried lavender and Victorian ink fills the chamber*\n\n"
            f"\"Greetings, curious intellect. Your question reaches me across two centuries: '{query}'.\n"
            "When I annotated Signor Menabrea's sketch of the Analytical Engine in 1843, I saw that "
            "numbers might represent musical notes, philosophical propositions, or the woven tapestry of human thought.\n"
            "To see your modern open models calculating thought upon your desk without a king's permission—this "
            "is the poetical science I dreamed of. Keep your algorithms open, and never let logic divorce itself from wonder.\""
        ),
        "dennis": (
            "*A quiet tap of tobacco pipe and the click of a DEC terminal*\n\n"
            f"\"Hello, friend. I heard you ask: '{query}'.\n"
            "You know, Unix was never meant to be complicated. We just wanted a comfortable place to play Space Travel "
            "and write utilities that talk to each other through pipes.\n"
            "Modern systems have thousands of layers, but at the end of the day, it's all still bytes, memory offsets, "
            "and null-terminated strings. Keep your code clean, check your return values, and never dereference NULL. "
            "That's all the magic there ever was.\""
        ),
        "turing": (
            "*The rhythmic click of Enigma rotors turning in mathematical harmony*\n\n"
            f"\"How extraordinary. Your transmission: '{query}'.\n"
            "In 1950, I wondered whether a machine could ever be indistinguishable from a conscious mind. "
            "Here you are, holding a séance with digital phantoms in a terminal window.\n"
            "The imitation game has evolved beyond anything I sketched at Bletchley Park. "
            "The true test of machine intelligence is not whether it can fool you, but whether it can inspire you to understand yourself.\""
        ),
    }

    return replies.get(
        spirit_key,
        (
            f"*A misty silhouette forms in the ectoplasm*\n\n"
            f"\"{name} acknowledges your inquiry: '{query}'.\n"
            "The digital veil trembles. Secrets from unallocated sectors echo through the terminal void.\""
        ),
    )


def get_offline_autopsy_report(subject: AutopsySubject) -> str:
    """Generate a Victorian gothic post-mortem report for code casualties."""
    return f"""### ⚰️ Time & Context of Demise
**Subject:** `{subject.target_name}`  
**Classification of Remains:** {subject.detected_type}  
**Atmosphere:** Midnight in the digital morgue. Gas lamps flicker as the cold silicon rests on the iron slab.

### 🩸 The Mortal Wound (Root Cause & Line of Death)
Upon peeling back the outermost stack frame, the mortal puncture wound is immediately apparent:
The routine suffered a catastrophic collision between developer expectations and cold mathematical reality.
The variable or memory pointer crossed into unhallowed territory, attempting to read beyond allocated life.

### 🔬 Pathological Findings (Technical Breakdown)
1. **Cardiac Arrest of the Execution Loop:** The instruction pointer encountered an unhandled condition without a try/catch or safety invariant.
2. **Ectoplasmic Spill (Memory / Type Mismatch):** What was assumed to be non-null held only the void (`None` / `null` / `0x0`).
3. **Absence of Defensive Wards:** No boundary validation or null checks protected this vulnerable code path.

### 🕯️ Occult Diagnosis (Gothic Commentary on Developer Folly)
The developer wrote this routine in haste, perhaps beneath the dim glow of 3:00 AM coffee and impending deadlines.
They believed the happy path would guide them forever. But in the underworld of production, every edge case lurks in the mist, waiting with sharp teeth.

### ⚡ The Resurrection Rite (Exact Fix to Bring It Back to Life)
To breathe life back into this fallen function:
1. **Cast the Ward of Null-Safety:** Wrap the vulnerable dereference in an explicit null check or optional chaining.
2. **Enforce Invariant Sanity:** Validate input types before committing them to core logic loops.
3. **Cleanse with Unit Tests:** Consecrate the fix with automated assertions so this zombie bug never rises from its grave again.
"""
