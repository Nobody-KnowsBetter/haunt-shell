---
title: "I Built a Haunted Terminal Possessed by an Open-Weight AI (And It Works 100% Offline) 👻"
published: false
description: "HauntShell: A terminal necromancer and ghost in the machine powered by open-weight Gemma and Ollama, featuring offline séances, possessed shell commands, and a Día de los Muertos ofrenda."
tags: "hf26challenge, gemma, opensource, ai"
---

*This is a submission for the [Hacktoberfest Open-Source AI Challenge Week 4: Ghost in the Machine](https://dev.to/challenges/hacktoberfest-week4-2026-10-26)*

***

## What I Built

I built **HauntShell** 👻 — an offline-first terminal companion, shell wrapper, and digital necromancer powered by Google's open-weight **Gemma 3** running locally on your own machine.

```
      .-.
     (o.o)    H A U N T S H E L L
      |=|     The Ghost in the Machine
     /   \    v1.0.0 • Open-Weight AI Necromancer
    (     )
    /`---'\
```

### The Concept & Inspiration
Between Halloween (October 31) and Día de los Muertos (November 1–2), the boundary between the living and the past grows thin. In computing, we interact with phantoms every single day:
* We spawn `daemon` processes (named after Maxwell's demon).
* We terminate processes with `kill -9` without granting them a chance to flush their buffers.
* We let orphan and zombie processes linger in kernel tables.
* We bury deleted code underneath `git reflog` pointers.
* We build upon the intellectual foundations laid by computing ancestors whose names are too often forgotten.

**HauntShell gives voice to the ghost living inside your silicon.** It provides four distinct capabilities:

1. **⚡ Possessed Terminal Watcher (`haunt exec "<cmd>"`):** Intercepts your shell commands and exit codes. When you execute destructive actions (`kill -9`, `rm -rf`, `git reset --hard`) or suffer fatal crashes, the local Gemma model manifests as an eerie spirit whispering live commentary on your actions.
2. **🔮 Interactive Digital Séance Chamber (`haunt chamber [spirit]`):** Enter a multi-turn terminal séance with burning candle physics (`🕯️ 🕯️ 🕯️ 🕯️ 🕯️`). As conversation turns advance, candles melt and burn down while you converse with trapped digital spirits:
   * **Clippy the Undead Revenant** (unhinged paperclip spirit resurrected from Office 97)
   * **Adobe Flash / ActionScript 3.0** (bitterly mourning Steve Jobs' 2010 open letter at 60 FPS)
   * **The Mainframe Lich (COBOL-60)** (cackling about how modern fintech still runs on 80-column punch cards while warning of the Y2K38 epoch overflow)
   * **Netscape Navigator 4.0** (wandering the Chromium monoculture seeking `<blink>` and `<marquee>`)
   * **Ada Lovelace, Alan Turing & Dennis Ritchie** (gentle spirits reflecting on the evolution of machine intelligence and systems programming)
3. **🌼 Día de los Muertos Digital Ofrenda (`haunt ofrenda`):** An altar decorated with glowing veladoras (candles) and marigolds (*cempasúchil*), offering coffee and punch cards to computing ancestors, accompanied by traditional **Calaveritas Literarias** (satirical and loving memorial poems in verse). Includes a private local builder (`haunt ofrenda --add`) to record remembrances for your own family and mentors that remain 100% private on your machine.
4. **⚰️ Victorian Codebase Autopsy (`haunt autopsy <file>`):** Submit stack traces, core dumps, segfaults, or dead code to Dr. Victor von Necro, Royal Digital Coroner, for a gothic post-mortem with exact resurrection rituals.

---

## Demo

### 1. Possessing Terminal Commands

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

### 2. Multi-Turn Interactive Séance Chamber with Burning Candle Physics

```bash
haunt chamber clippy
```

```
        .---.
       / /"\ \      * The veil thins... summoning digital spirit *
      | | | | |     🕯️  🕯️  🕯️  Offline Séance Chamber  🕯️  🕯️  🕯️
       \ \_/ /
        `---`

   Summoned Entity: Clippy the Undead Revenant (1997 - 2007)
   🕯️  🕯️  🕯️  🕯️  🕯️

* Type 'farewell', 'exit', or 'quit' to close the séance circle *

Séance Candles: 🕯️  🕯️  🕯️  🕯️  🕯️
🔮 Inquire of the spirit: Why won't my code compile?

Mortal Inquiry: "Why won't my code compile?"
* Chanting hex incantations... 📎 👁️ responds *

*Taps furiously on the interior of your terminal screen*

"It looks like you are seeking cosmic wisdom from a paperclip!
You asked: 'Why won't my code compile?'.
Allow me to format your impending doom as an unnumbered bullet list:
 • Bullet 1: Your stack is already corrupt.
 • Bullet 2: Microsoft tried to bury me in Windows Vista, but I live in every .docx file you ever abandoned.
 • Bullet 3: Would you like assistance drafting a last will and testament? I have a template for that!"

Séance Candles: 🕯️  🕯️  🕯️  🔥  💨
🔮 Inquire of the spirit: farewell

* You bid farewell. Clippy the Undead Revenant dissolves into the ethereal mist. *
```

---

### 3. Día de los Muertos Altar: Honoring Ada Lovelace & Family

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

You can also preserve personal family remembrances locally:
```bash
haunt ofrenda --add     # Record loved ones, favorite foods, songs, and memories
haunt ofrenda --custom  # View your private family altar
```

---

### 4. Codebase Autopsy of a Crash

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

## Code

HauntShell is 100% open-source under the MIT License:

{% github Nobody-KnowsBetter/haunt-shell %}

**GitHub Repository:** [https://github.com/Nobody-KnowsBetter/haunt-shell](https://github.com/Nobody-KnowsBetter/haunt-shell)

### Quick Start (1-Minute Installation)
```bash
git clone https://github.com/Nobody-KnowsBetter/haunt-shell.git
cd haunt-shell
bash setup.sh
source .venv/bin/activate
haunt --help
```

---

## How I Built It

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

### Key Technical Details

* **Google's Gemma 3 via Ollama (`ollama_client.py`):**
  We chose Google's open-weight **Gemma 3** (`gemma3`) as the core inference engine. Gemma 3 provides exceptional instruction following and creative nuance. We built an asynchronous HTTP client using `httpx` that parses chunked NDJSON streaming tokens from Ollama's `/api/generate` endpoint, delivering live token streaming with zero perceived delay.
* **The Procedural Necromancy Fallback (`fallback_lore.py`):**
  A core design tenet was: **never fail if the user has no GPU or Ollama is offline.** HauntShell embeds a deterministic procedural necromancy engine containing hundreds of lines of gothic lore, spirit interactions, and Calaveritas. If Ollama isn't running, HauntShell automatically falls back to offline mode seamlessly.
* **Persona Archetypes (`spirits.py` & `ofrenda.py`):**
  Each summoned entity is given strict linguistic constraints (e.g. COBOL speaking in ALL CAPS and mainframe divisions; Flash speaking in 60 FPS timeline tweens; Clippy using unnumbered bullet points).
* **Terminal Aesthetics (`ui.py`):**
  Built with **Typer** and **Rich**, featuring custom ASCII art (altars, sugar skulls, candles, tombstones) and gothic ANSI palettes.
* **Tested & Automated CI:**
  Includes **39 unit and integration tests (85% coverage)** that execute in under 4 seconds with 100% mocked dependencies, backed by automated GitHub Actions CI testing on Python 3.10 through 3.13.

---

## Why Does Open Innovation Matter?

Open-source AI and open-weight models are not cosmetic add-ons for HauntShell — **they are the entire architectural foundation**:

1. **🕯️ It Works When the Lights (and Internet) Go Off:**
   The spirit of Halloween and Día de los Muertos evokes stormy nights, candlelight, and quiet reflection. A cloud AI that fails when WiFi disconnects is an illusion of intelligence. Because Gemma 3 runs directly on your laptop's silicon, HauntShell functions seamlessly in an off-grid cabin, on a flight, or during a late-night power outage on Halloween.
2. **🛡️ Absolute Privacy: Keeping Your Terminal's Soul Private:**
   HauntShell inspects shell commands (`rm`, `kill`, `git`, `sudo`), environment variables, and stack traces. Sending command history and crash logs to a third-party cloud API creates massive data privacy and NDA liabilities. With open-weight models running on localhost, **not a single byte leaves your machine**.
3. **🎭 Uncensored Gothic Creativity & Persona Freedom:**
   Commercial cloud APIs enforce corporate safety filters that often sterilize gothic humor, dark comedy, or spooky roleplay. A closed API might refuse to simulate an "undead revenant paperclip" or a "coroner performing an autopsy on code". Open-weight models like Gemma allow developers to build expressive artistic software without arbitrary corporate censorship.
4. **💰 Zero Marginal Cost: An Ambient Ghost Costs $0.00:**
   Cloud APIs charge per token. An ambient shell companion that observes your command line would quickly rack up expensive bills. Local inference with Gemma turns ambient AI from an expensive subscription into a **free, permanent utility**.
5. **⏳ Long-Term Digital Preservation:**
   Closed APIs deprecate models and shut down endpoints every few months. What happens to your software when the vendor alters pricing or disappears? An open-weight model saved to disk will run identically today, tomorrow, or in 2046. Just as Día de los Muertos ensures our ancestors are never forgotten, open-source AI ensures our software is preserved forever.

---

## My Agent Session

I developed HauntShell using Antigravity and DevRelay. You can inspect the full interactive agent session transcript directly on DEV:

{% agent_session building-hauntshell-the-ghost-in-the-machine-tutefr %}

**Direct Session Link:** [https://dev.to/agent_sessions/building-hauntshell-the-ghost-in-the-machine-tutefr](https://dev.to/agent_sessions/building-hauntshell-the-ghost-in-the-machine-tutefr)

---

## The Spirit of It

What moved me most while building this was the intersection of **Halloween** and **Día de los Muertos**. 

We often treat software as disposable. We rewrite frameworks, delete old repos, and deprecate protocols without a second thought. But our entire digital world rests on the shoulders of giants who came before us:
* **Ada Lovelace**, who saw poetry in algebra.
* **Alan Turing**, who cracked Enigma and asked if machines could think.
* **Dennis Ritchie**, whose quiet C pointers and Unix pipes power nearly every device on Earth.
* **Grace Hopper**, who taught computers to speak human language.

Running `haunt ofrenda ada` or placing an offering for a beloved family member with `haunt ofrenda --add` brings warmth to the cold silicon of a terminal. It reminds us that technology is human, that memory is sacred, and that the ghost in the machine is simply the reflection of the minds that built it.

---

## Prize Categories

* 🏆 **Overall Hacktoberfest Open-Source AI Winner:** An original, production-grade interpretation of the *Ghost in the Machine* theme.
* 💎 **Best Use of Gemma ($200 Featured Partner Category):** Architected natively for Google's open-weight **Gemma 3** (`gemma3`) running via Ollama.
