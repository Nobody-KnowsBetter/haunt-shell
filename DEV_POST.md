---
title: "I Built a Haunted Terminal Possessed by an Open-Weight AI (And It Works 100% Offline) 👻"
published: false
description: "HauntShell: A terminal necromancer and ghost in the machine powered by open-weight Gemma and Ollama, featuring offline séances, possessed shell commands, and a Día de los Muertos ofrenda."
tags: "hf26challenge, gemma, ai, opensource"
---

*This is a submission for the [Hacktoberfest Open-Source AI Challenge Week 4: Ghost in the Machine](https://dev.to/challenges/hacktoberfest-week4-2026-10-26)*

***

## 👻 What I Built

I built **HauntShell** 👻 — an offline-first terminal companion, shell wrapper, and digital necromancer powered by Google's open-weight **Gemma 3** running locally on your own machine.

```
      .-.
     (o.o)    H A U N T S H E L L
      |=|     The Ghost in the Machine
     /   \    v1.0.0 • Open-Weight AI Necromancer
    (     )
    /`---'\
```

### The Concept: Ghost in the Machine
Between Halloween (October 31) and Día de los Muertos (November 1–2), the boundary between the living and the past grows thin. In computing, we constantly interact with phantoms:
* We spawn `daemon` processes (named after Maxwell's demon).
* We terminate processes with `kill -9` without giving them a chance to flush their buffers.
* We let orphan and zombie processes linger in process tables.
* We bury deleted code under `git reflog` pointers.
* We build upon the intellectual foundations laid by computing ancestors whose names are too often forgotten.

**HauntShell gives voice to the ghost living inside your silicon.** 

It does this across four distinct modes:

1. **⚡ Possessed Terminal Watcher (`haunt exec "<cmd>"`):** Intercepts your shell commands and exit codes. When you execute destructive actions (`kill -9`, `rm -rf`, `git reset --hard`) or suffer fatal crashes, the local Gemma model manifests as an eerie spirit whispering live commentary on your actions.
2. **🔮 Offline Digital Séance Parlor (`haunt seance [spirit]`):** Summon and converse with the trapped spirits of deceased technologies and computing legends:
   * **Clippy the Undead Revenant** (unhinged paperclip spirit resurrected from Office 97)
   * **Adobe Flash / ActionScript 3.0** (bitterly mourning Steve Jobs' 2010 open letter at 60 FPS)
   * **The Mainframe Lich (COBOL-60)** (cackling about how modern fintech still runs on 80-column punch cards while warning of the Y2K38 epoch overflow)
   * **Netscape Navigator 4.0** (wandering the Chromium monoculture seeking `<blink>` and `<marquee>`)
   * **Ada Lovelace, Alan Turing & Dennis Ritchie** (gentle spirits reflecting on the evolution of machine intelligence and systems programming)
3. **🌼 Día de los Muertos Digital Ofrenda (`haunt ofrenda [pioneer]`):** An altar decorated with glowing veladoras (candles) and marigolds (*cempasúchil*), offering coffee and punch cards to computing ancestors, accompanied by traditional **Calaveritas Literarias** (humorous and loving satirical poems in verse).
4. **⚰️ Victorian Codebase Autopsy (`haunt autopsy <file>`):** Submit stack traces, core dumps, segfaults, or dead code to Dr. Victor von Necro, Royal Digital Coroner, for a gothic post-mortem with exact resurrection rituals.

---

## 🎥 Demo

### 1. The Possessed Shell in Action

Run any command under the ghost's watch:

```bash
haunt exec "rm -rf old_build/"
```

```
⚡ Executing in the mortal realm: rm -rf old_build/

* The silicon whispers... exit code 0 *

🩸 An Act of Deletion
You cast the void upon mortal files with `rm -rf old_build/`.
Their inodes have been severed. In the cold sectors of the drive, orphaned bits
weep quietly, unaddressed and forsaken. They will haunt your free space forever.
```

Or when an incantation fails:

```bash
haunt exec "cat missing_file.txt"
```

```
⚡ Demonic Rupture (Exit Code 1)
The incantation `cat missing_file.txt` collapsed into chaos. The machine screams in agony:
"cat: missing_file.txt: No such file or directory"
The spirits mock your hubris. To appease the void, cleanse your syntax and offer fresh RAM.
```

---

### 2. Holding an Offline Séance with Clippy

```bash
haunt seance clippy --query "Why won't my code compile?"
```

```
        .---.
       / /"\ \      * The veil thins... summoning digital spirit *
      | | | | |     🕯️  🕯️  🕯️  Offline Séance Chamber  🕯️  🕯️  🕯️
       \ \_/ /
        `---`

   Summoned Entity: Clippy the Undead Revenant (1997 - 2007)
   🕯️  🕯️  🕯️  🕯️  🕯️

Mortal Inquiry: "Why won't my code compile?"

* Chanting hex incantations... 📎 👁️ materializes *

*Taps furiously on the interior of your terminal screen*

"It looks like you are seeking cosmic wisdom from a paperclip!
You asked: 'Why won't my code compile?'.
Allow me to format your impending doom as an unnumbered bullet list:
 • Bullet 1: Your stack is already corrupt.
 • Bullet 2: Microsoft tried to bury me in Windows Vista, but I live in every .docx file you ever abandoned.
 • Bullet 3: Would you like assistance drafting a last will and testament? I have a template for that!"
```

---

### 3. Día de los Muertos Ofrenda: Honoring Ada Lovelace

```bash
haunt ofrenda ada
```

```
     ╭━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╮
     │   🌼 🕯️  OFRENDA DIGITAL • DÍA DE LOS MUERTOS  🕯️ 🌼         │
     ╰━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╯

           .-''''-.
          /  _  _  \     Calavera de Azúcar
         |  (o)(o)  |    Honor a nuestros ancestros digitales
         |    /\    |
          \  \__/  /
           `'----'`

   Honored Ancestor: Ada Lovelace (Countess of Lovelace)
   Era of Impact:    1815 – 1852
   Altar Offerings:  🌼 Fresh Cempasúchil garlands from the English countryside
                     📜 Bernoulli number computation tables woven on punched cards
                     ☕ Strong Earl Grey tea and fine ink for quill work
                     🕯️ Glowing beeswax candles illuminating the Analytical Engine

💀 Calaverita Literaria for Ada Lovelace:

La Muerte arrived with a bony decree,
To audit the numbers of young Ada's spree.
'Your Engine,' said Death, 'weaves a magical song,
Come dance through the ether where spirits belong!'
Now Ada writes loops in the starlight above,
Her algorithms guided by science and love.
```

---

### 4. Codebase Autopsy of a Stack Trace

```bash
haunt autopsy "Traceback (most recent call last): File 'server.py', line 54, in handle_client: ZeroDivisionError"
```

```
           .---.
          / RIP \
         |       |       CODEBASE POST-MORTEM
         |  ✝    |       Coroner's Examination of Dead Code & Crashes
         |       |
      ___|_______|___

### ⚰️ Time & Context of Demise
**Subject:** `Terminal Exception / Trace`
**Classification of Remains:** Python Exception
**Atmosphere:** Midnight in the digital morgue. Gas lamps flicker as the cold silicon rests on the iron slab.

### 🩸 The Mortal Wound (Root Cause & Line of Death)
Upon peeling back the outermost stack frame, the mortal puncture wound is immediately apparent:
The routine suffered a catastrophic collision between developer expectations and cold mathematical reality.
The denominator collapsed into the void (0), ripping a hole through the CPU ALU registers.

### 🔬 Pathological Findings
1. **Cardiac Arrest of the Execution Loop:** The instruction pointer encountered an unhandled condition without a defensive guard.
2. **Absence of Defensive Wards:** Zero validation checks guarded the denominator input.

### ⚡ The Resurrection Rite
1. Wrap the calculation in an explicit zero check: `if denominator != 0: ...`
2. Fallback to a safe identity default or raise a domain-specific error.
3. Cleanse with an automated unit test so this zombie exception never haunts production again.
```

---

## 💻 Code & Repository

HauntShell is 100% open-source under the permissive MIT License:

**GitHub:** [https://github.com/Nobody-KnowsBetter/haunt-shell](https://github.com/Nobody-KnowsBetter/haunt-shell)

### Quick Start (1-Minute Installation)
```bash
git clone https://github.com/Nobody-KnowsBetter/haunt-shell.git
cd haunt-shell
bash setup.sh
source .venv/bin/activate
haunt --help
```

---

## 🛠️ How I Built It

HauntShell was engineered from the ground up to make local open-weight models behave with theatrical precision, zero network latency, and high resiliency:

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

### Key Engineering Pillars

1. **Google's Gemma 3 via Ollama (`ollama_client.py`):**
   * Defaulted to Google's open-weight **Gemma 3** (`gemma3`), which delivers state-of-the-art instruction following, sharp wit, and concise literary prose on consumer hardware.
   * Built an async streaming HTTP client using `httpx` that parses chunked NDJSON streams from Ollama's `/api/generate` endpoint, delivering token-by-token live output with zero perceived latency.

2. **The Procedural Necromancy Fallback (`fallback_lore.py`):**
   * One of my core design principles was: **never let the tool fail if the user is completely offline or doesn't have a local GPU running.**
   * If Ollama is not installed or the daemon is paused, HauntShell smoothly falls back to an embedded procedural necromancy engine containing hundreds of lines of hand-crafted gothic lore, spirit dialogues, and Mexican Calaveritas.

3. **Strict Archetype Prompt Engineering (`spirits.py` & `ofrenda.py`):**
   * Open models shine brightest when given deeply defined theatrical personas.
   * Each spirit has distinct memory constraints, emotional baggage, and vocabulary (e.g. COBOL speaking in ALL CAPS and mainframe divisions; Flash speaking in 60 FPS tweens; Clippy using unnumbered bullet points).

4. **Atmospheric Terminal UX (`ui.py`):**
   * Built with **Typer** and **Rich**.
   * Employs gothic color palettes (spectral cyans, ectoplasm purples, cempasúchil marigold golds) and ASCII art representing altars, sugar skulls, tombstones, and candles.

5. **Test Suite with 85% Coverage:**
   * 35 unit and integration tests across CLI commands, spirit resolution, autopsy parsing, and async Ollama streaming.
   * 100% mocked dependencies, so the entire test suite runs and passes in under 4 seconds without needing an internet connection or GPU!

---

## 🔒 Why Open Innovation Matters

Open-source and open-weight AI are not cosmetic choices for HauntShell — **they are the entire architectural and philosophical foundation**:

### 1. 🕯️ It Works When the Lights (and Internet) Go Off
The theme of Halloween and Día de los Muertos evokes midnight storms, flickering candlelight, and quiet remembrance. A cloud-tethered AI that stops working the moment your WiFi drops or the power flickers is an illusion of intelligence. Because Gemma 3 runs directly on your laptop's silicon, HauntShell functions seamlessly in an off-grid cabin, on an airplane, or during a late-night power outage on Halloween.

### 2. 🛡️ Terminal Privacy: Keeping Your Machine's Soul Private
HauntShell observes shell commands (`rm`, `kill`, `git`, `sudo`), environment variables, and stack traces. Sending command history and crash logs to a third-party cloud API like OpenAI or Anthropic is a major security risk and violation of developer trust. With open-weight models, **every token stays inside localhost socket memory**.

### 3. 🎭 Uncensored Gothic Creativity & Persona Freedom
Commercial cloud APIs have strict corporate safety filters that often sterilize gothic humor, dark comedy, or spooky roleplay. A closed API might refuse to simulate an "undead revenant paperclip" or a "coroner performing an autopsy on code" because it misinterprets gothic terminology. Open-weight models like Gemma empower developers to build expressive artistic software without arbitrary corporate censorship.

### 4. 💰 Zero Marginal Cost: An Ambient Ghost Costs $0.00
Cloud APIs bill per token. An ambient shell companion that generates commentary on every command you run would quickly burn through paid API quotas. Local inference with Gemma turns ambient AI from an expensive SaaS recurring fee into a **free, permanent utility**.

### 5. ⏳ Digital Preservation
Closed APIs deprecate models and shut down endpoints every few months. What happens to your software when the vendor changes its pricing or goes out of business? An open-weight model saved to a disk will run identically today, tomorrow, or in 2046. Just as Día de los Muertos honors our ancestors so they are never forgotten, open-source AI ensures our software is preserved forever.

---

## 🏆 Prize Categories

* 🥇 **Overall Hacktoberfest Open-Source AI Winner:** An original, production-ready interpretation of the *Ghost in the Machine* theme.
* 💎 **Best Use of Gemma ($200 Featured Partner Category):** Architected natively for Google's open-weight **Gemma 3** (`gemma3`) running via Ollama.

---

## 🖤 Acknowledgments

Dedicated with love and reverence to the digital ancestors who laid the foundation of modern computing: **Ada Lovelace**, **Alan Turing**, **Dennis Ritchie**, **Grace Hopper**, and **Margaret Hamilton**.

*¡Feliz Día de los Muertos y Feliz Halloween!* 🎃🌼🕯️
