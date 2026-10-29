"""Victorian digital post-mortem and stack trace autopsy for HauntShell."""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path
from typing import Optional


@dataclass
class AutopsySubject:
    """Represents a code artifact or stack trace submitted to the coroner."""

    target_name: str
    content: str
    detected_type: str


def prepare_autopsy_subject(target: str) -> AutopsySubject:
    """Inspect and load a file or raw string for post-mortem examination."""
    path = Path(target)
    if path.is_file():
        try:
            content = path.read_text(encoding="utf-8", errors="replace")
            detected_type = detect_content_type(path.name, content)
            return AutopsySubject(target_name=str(path), content=content[:8000], detected_type=detected_type)
        except Exception as e:
            return AutopsySubject(
                target_name=str(path),
                content=f"Error reading artifact: {e}",
                detected_type="corrupted_relic",
            )
    else:
        # Treat target string itself as the error traceback
        detected_type = detect_content_type("inline_trace", target)
        return AutopsySubject(target_name="Terminal Exception / Trace", content=target[:8000], detected_type=detected_type)


def detect_content_type(filename: str, content: str) -> str:
    """Classify the subject's programming language or trace dialect."""
    lowered = content.lower()
    fn_lower = filename.lower()

    if "traceback (most recent call last)" in lowered or fn_lower.endswith(".py"):
        return "Python Exception"
    elif "segmentation fault" in lowered or "sigsegv" in lowered or fn_lower.endswith((".c", ".cpp", ".h")):
        return "C/C++ Memory Casualty"
    elif "panic:" in lowered or "thread 'main' panicked" in lowered or fn_lower.endswith(".rs"):
        return "Rust Panic"
    elif "typeerror:" in lowered or "unhandledpromiserejection" in lowered or fn_lower.endswith((".js", ".ts")):
        return "JavaScript/Node Casualty"
    elif "nullpointerexception" in lowered or fn_lower.endswith((".java", ".kt")):
        return "JVM Catastrophe"
    elif "diff --git" in lowered:
        return "Git Commit Demise"
    return "Unknown Digital Relic"


def build_autopsy_system_prompt() -> str:
    """Return the system prompt for the Victorian Digital Coroner."""
    return (
        "You are Dr. Victor von Necro, the Royal Coroner of the Digital Afterlife. "
        "A mortal has brought a fallen piece of software, stack trace, or crashed routine to your operating slab. "
        "Your task is to conduct an eerie, Victorian gothic post-mortem examination. "
        "Structure your examination into these exact sections with these headers:\n\n"
        "### ⚰️ Time & Context of Demise\n"
        "### 🩸 The Mortal Wound (Root Cause & Line of Death)\n"
        "### 🔬 Pathological Findings (Technical Breakdown)\n"
        "### 🕯️ Occult Diagnosis (Gothic commentary on developer folly)\n"
        "### ⚡ The Resurrection Rite (Exact, actionable code fix to bring it back to life)\n\n"
        "Write with dark elegance, medical humor, and precise software engineering accuracy."
    )
