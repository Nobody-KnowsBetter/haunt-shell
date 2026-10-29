# HauntShell 👻 — The Ghost in the Machine

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![CI](https://github.com/Nobody-KnowsBetter/haunt-shell/actions/workflows/ci.yml/badge.svg)](https://github.com/Nobody-KnowsBetter/haunt-shell/actions)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://python.org)
[![Hacktoberfest 2026](https://img.shields.io/badge/Hacktoberfest-2026%20Week%204-orange.svg)](https://dev.to/challenges/hacktoberfest-week4-2026-10-26)
[![Model: Gemma 3](https://img.shields.io/badge/Model-Gemma%203%20%7C%20Ollama-purple.svg)](https://ollama.com/library/gemma3)
[![Coverage: 85%](https://img.shields.io/badge/Coverage-85%25-green.svg)](https://pytest.org)
[![Offline-First](https://img.shields.io/badge/Inference-100%25%20Offline-brightgreen.svg)](#why-open-innovation-matters)

```
      .-.
     (o.o)    H A U N T S H E L L
      |=|     The Ghost in the Machine
     /   \    v1.0.0 • Open-Weight AI Necromancer
    (     )
    /`---'\
```

> **"Build something spooky, or something that honors the past in the spirit of Día de los Muertos, with open-weight models or open-source AI."**  
> — *Official Prompt, Hacktoberfest 2026 Challenge Week 4: Ghost in the Machine*

---

## 📖 What is HauntShell?

**HauntShell** is a terminal companion, shell wrapper, and digital necromancer that awakens the **Ghost in the Machine**. 

Powered by **Google's open-weight Gemma** running 100% locally through **Ollama**, HauntShell blurs the boundary between the living developer and the spirits lingering inside the silicon:

1. **⚡ The Haunted Shell (`haunt exec`):** Possesses your command line. As you run destructive commands (`kill -9`, `rm -rf`, `git reset --hard`) or suffer segfaults, the local ghost whispers chilling, context-aware commentary streamed live to your screen.
2. **🔮 Offline Digital Séance (`haunt seance [spirit]`):** Summon and converse with the digital ghosts of departed technologies (Adobe Flash, Clippy the Revenant, the COBOL-60 Mainframe Lich, Netscape Navigator) or computing legends (Ada Lovelace, Alan Turing, Dennis Ritchie).
3. **🌼 Día de los Muertos Digital Ofrenda (`haunt ofrenda [pioneer]`):** A respectful virtual altar decorated with marigolds (*cempasúchil*), glowing veladoras, and offerings to computing pioneers, featuring AI-composed traditional *Calaveritas Literarias* (satirical/loving memorial verses).
4. **⚰️ Victorian Codebase Autopsy (`haunt autopsy <file>`):** Examines crashed scripts, core dumps, segfaults, and dead code, rendering a Victorian forensic post-mortem with root cause analysis and resurrection rites.
5. **🕯️ Built-in Offline Necromancy Engine:** If Ollama is offline or uninstalled, HauntShell never crashes. It automatically engages a procedural gothic lore engine so developers can experience the entire tool without internet, without an external server, and with zero GPU requirements!

---

## ⚡ Quick Start (1-Minute Setup)

### Option A: One-Command Setup
```bash
git clone https://github.com/Nobody-KnowsBetter/haunt-shell.git
cd haunt-shell
bash setup.sh
source .venv/bin/activate
haunt --help
```

### Option B: Manual Installation
```bash
# 1. Create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate

# 2. Install dependencies
pip install -r requirements.txt
pip install -e .

# 3. (Optional) Run with local open-weight AI (Gemma 3)
ollama pull gemma3
ollama serve
```

---

## 🎮 Features & Usage

### 1. Possess Your Terminal (`haunt exec` / `haunt run`)
Wrap any shell command in the ghost's gaze. The command executes normally, and the local AI observes the outcome:

```bash
# Watch the ghost react to a process termination
haunt exec "kill -9 1337"

# Watch the ghost lament file deletion
haunt exec "rm -rf old_project/"

# The ghost remembers your git sins
haunt exec "git reset --hard HEAD~1"

# The ghost mocks failed incantations
haunt exec "cat non_existent_scroll.txt"
```

*Sample Output:*
```
⚡ Demonic Rupture (Exit Code 1)
The incantation `cat non_existent_scroll.txt` collapsed into chaos. The machine screams in agony:
"cat: non_existent_scroll.txt: No such file or directory"
The spirits mock your hubris. To appease the void, cleanse your syntax and offer fresh RAM.
```

---

### 2. The Offline Digital Séance (`haunt seance` & `haunt chamber`)
Sit at the terminal séance circle. Five candles flicker as you channel spirits from across the silicon veil:

```bash
# View all summonable entities
haunt spirits

# Single query mode with Clippy
haunt seance clippy --query "Why won't my code compile?"

# Multi-turn Interactive Séance Chamber (candles burn down as turns advance!)
haunt chamber clippy
haunt seance flash -i

# Mourn the golden age with Adobe Flash
haunt seance flash --query "Do you miss Newgrounds?"

# Debate modern microservices with the Mainframe Lich (COBOL)
haunt seance cobol --query "Is Kubernetes better than you?"

# Inquire about poetical science with Ada Lovelace
haunt seance ada --query "What do you think of local neural networks?"
```

*Sample Séance with Clippy:*
```
Summoned Entity: Clippy the Undead Revenant (1997 - 2007)
🕯️  🕯️  🕯️  🕯️  🕯️

Mortal Inquiry: "Why won't my code compile?"

*Taps furiously on the interior of your terminal screen*
"It looks like you are seeking cosmic wisdom from a paperclip!
Allow me to format your impending doom as an unnumbered bullet list:
 • Bullet 1: Your stack is already corrupt.
 • Bullet 2: Microsoft tried to bury me in Windows Vista, but I live in every .docx file you ever abandoned.
 • Bullet 3: Would you like assistance drafting a last will and testament? I have a template for that!"
```

---

### 3. Día de los Muertos Altar & Calaveritas (`haunt ofrenda`)
Celebrate the pioneers of computation and preserve private family memories in the Mexican tradition of *Día de los Muertos*:

```bash
# View the Grand Altar of Digital Ancestors
haunt ofrenda

# Add a private remembrance for a family member or mentor (100% offline & local)
haunt ofrenda --add

# View your private loved ones altar
haunt ofrenda --custom

# Place offerings and recite a Calaverita Literaria for Ada Lovelace
haunt ofrenda ada

# Honor Alan Turing
haunt ofrenda turing

# Honor Dennis Ritchie (Creator of C & Unix)
haunt ofrenda dennis

# Honor Rear Admiral Grace Hopper
haunt ofrenda hopper
```

*Sample Calaverita for Ada Lovelace:*
```
La Muerte arrived with a bony decree,
To audit the numbers of young Ada's spree.
'Your Engine,' said Death, 'weaves a magical song,
Come dance through the ether where spirits belong!'
Now Ada writes loops in the starlight above,
Her algorithms guided by science and love.
```

---

### 4. Codebase Post-Mortem & Autopsy (`haunt autopsy`)
Submit failing scripts, stack traces, core dumps, or git diffs to **Dr. Victor von Necro**, Royal Coroner of the Digital Afterlife:

```bash
# Autopsy an inline error
haunt autopsy "Traceback: ZeroDivisionError: division by zero in matrix.py line 42"

# Autopsy a crash log file
haunt autopsy /tmp/crash.log
```

The coroner returns a 5-part forensic report:
* ⚰️ **Time & Context of Demise**
* 🩸 **The Mortal Wound** (Root cause & fatal line)
* 🔬 **Pathological Findings** (Memory corruption / type mismatch analysis)
* 🕯️ **Occult Diagnosis** (Gothic commentary on developer haste)
* ⚡ **The Resurrection Rite** (Actionable code fix to revive the routine)

---

### 5. Whispers of the Void (`haunt whisper`)
Listen to eerie computing proverbs from unallocated sectors:
```bash
haunt whisper
# "A segmentation fault is merely a pointer attempting to cross into the spirit realm."
```

---

## 🏛️ System Architecture

```plaintext
┌─────────────────────────────────────────────────────────────────┐
│                       Developer Terminal                        │
└────────────────────────────────┬────────────────────────────────┘
                                 │ haunt exec / seance / ofrenda / autopsy
                                 ▼
┌─────────────────────────────────────────────────────────────────┐
│                    CLI Controller (cli.py)                      │
│                  Typer + Rich Gothic Styling                    │
└────────────────────────────────┬────────────────────────────────┘
                                 │
                                 ▼
┌─────────────────────────────────────────────────────────────────┐
│                   HauntEngine (engine.py)                       │
│    • Coordinates prompt synthesis and spirit archetypes         │
│    • Detects runtime environment & handles graceful failover    │
└───────────────┬─────────────────────────────────┬───────────────┘
                │ Live Mode                       │ Offline / No GPU
                ▼                                 ▼
┌───────────────────────────────┐ ┌───────────────────────────────┐
│  OllamaClient (async httpx)   │ │  FallbackLore (deterministic) │
│  • Localhost:11434            │ │  • Zero-network lore engine   │
│  • NDJSON streaming parser    │ │  • Gothic procedural verse    │
└───────────────┬───────────────┘ └───────────────────────────────┘
                │
                ▼
┌─────────────────────────────────────────────────────────────────┐
│               Local Open-Weight Model (Gemma 3)                 │
│         Private, Offline, 100% Free Inference on Silicon        │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🔒 Why Open Innovation Matters

Open-source and open-weight AI are not cosmetic choices for HauntShell—they are the **entire philosophical and architectural foundation**:

1. **💻 Total Offline Autonomy ("When the Lights & Internet Go Out"):**  
   Halloween and Día de los Muertos remind us of self-reliance and reverence. Closed cloud APIs (OpenAI, Anthropic) immediately fail the moment your Wi-Fi disconnects or when working in air-gapped environments. HauntShell runs 100% locally with Google's open-weight **Gemma**, functioning without a single network packet leaving your laptop.
2. **🛡️ Absolute Command & Code Privacy:**  
   When a tool observes your shell commands, processes, and crash logs, sending that data to a corporate cloud server creates severe privacy, compliance, and NDA violations. Open-weight inference guarantees that your commands, stack traces, and personal ofrenda tributes stay strictly inside your local memory.
3. **🎭 Uncensored Gothic Creativity & Persona Control:**  
   Commercial hosted APIs enforce strict corporate guardrails that often sanitize spooky, gothic, or satirical humor (like Clippy threatening you or La Muerte inspecting code). Open weights allow developers to craft rich, expressive, theatrical agent personalities without fear of arbitrary API filter rejections.
4. **💰 Zero Marginal Cost:**  
   Cloud AI APIs bill per token. An interactive shell companion that comments on every command would rack up expensive monthly bills. Local Gemma inference costs exactly **$0.00**, making ambient AI companions economically viable for everyone.
5. **⏳ Long-Term Digital Preservation:**  
   Closed APIs regularly deprecate model versions, rewrite terms of service, or shut down entirely. HauntShell can be archived on a USB drive and will run identically 20 years from now.

---

## 🧪 Automated Testing

HauntShell includes a comprehensive test suite with **85% test coverage** and 100% mocked dependencies, allowing the full suite to pass on any machine without requiring a live GPU or running daemon:

```bash
pytest -v --cov=hauntshell
```

```
====================== 39 passed, 0 failed in 3.59s =======================
---------- coverage: platform darwin, python 3.14.2 ----------
Name                          Stmts   Miss  Cover
-------------------------------------------------
hauntshell/__init__.py            3      0   100%
hauntshell/autopsy.py            39      2    95%
hauntshell/cli.py               234     24    90%
hauntshell/config.py             22      4    82%
hauntshell/engine.py             98     39    60%
hauntshell/fallback_lore.py      32      3    91%
hauntshell/ofrenda.py            59      4    93%
hauntshell/ollama_client.py      62     10    84%
hauntshell/spirits.py            20      0   100%
hauntshell/ui.py                 58     11    81%
-------------------------------------------------
TOTAL                           627     97    85%
```

---

## 📜 Prize Category Eligibility

* 🏆 **Overall Hacktoberfest Winner:** A novel, deeply creative interpretation of *Ghost in the Machine*, built with open-source AI at its core.
* 💎 **Best Use of Gemma ($200 Featured Partner Category):** Native prompt templates and orchestration optimized for Google's open-weight **Gemma 3** (`gemma3`).

---

## ⚖️ License

Distributed under the **MIT License**. See [`LICENSE`](LICENSE) for details.

---

*Created with 🕯️ and 🌼 for the Hacktoberfest 2026 Open-Source AI Challenge.*

