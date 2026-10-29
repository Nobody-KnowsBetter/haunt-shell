#!/usr/bin/env bash
# =============================================================================
# setup.sh — One-command setup for HauntShell 👻
# Usage: bash setup.sh
# =============================================================================
set -euo pipefail

PYTHON_MIN="3.10"
VENV_DIR=".venv"

# ── Colour helpers ────────────────────────────────────────────────────────────
RED='\033[0;31m'; GREEN='\033[0;32m'; YELLOW='\033[1;33m'
PURPLE='\033[0;35m'; CYAN='\033[0;36m'; RESET='\033[0m'

info()    { echo -e "${CYAN}ℹ  $*${RESET}"; }
success() { echo -e "${GREEN}✓  $*${RESET}"; }
warn()    { echo -e "${YELLOW}⚠  $*${RESET}"; }
error()   { echo -e "${RED}✗  $*${RESET}" >&2; exit 1; }

echo ""
echo -e "${PURPLE}╔════════════════════════════════════════════════════╗${RESET}"
echo -e "${PURPLE}║   👻 HauntShell — The Ghost in the Machine Setup   ║${RESET}"
echo -e "${PURPLE}║      Open-Weight AI Necromancer (Gemma & Ollama)    ║${RESET}"
echo -e "${PURPLE}╚════════════════════════════════════════════════════╝${RESET}"
echo ""

# ── 1. Check Python version ───────────────────────────────────────────────────
info "Checking Python version..."
PYTHON_CMD=""
for cmd in python3 python; do
    if command -v "$cmd" &>/dev/null; then
        VER=$("$cmd" -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')
        MAJOR=$(echo "$VER" | cut -d. -f1)
        MINOR=$(echo "$VER" | cut -d. -f2)
        if [ "$MAJOR" -ge 3 ] && [ "$MINOR" -ge 10 ]; then
            PYTHON_CMD="$cmd"
            success "Found Python $VER ($cmd)"
            break
        fi
    fi
done

if [ -z "$PYTHON_CMD" ]; then
    error "Python $PYTHON_MIN or higher is required. Please install it from https://python.org"
fi

# ── 2. Create virtual environment ─────────────────────────────────────────────
if [ -d "$VENV_DIR" ]; then
    warn "Virtual environment already exists at $VENV_DIR — skipping creation."
else
    info "Creating virtual environment in $VENV_DIR..."
    "$PYTHON_CMD" -m venv "$VENV_DIR"
    [[ "$OSTYPE" == "darwin"* ]] && chflags -R 0 "$VENV_DIR" 2>/dev/null || true
    success "Virtual environment created."
fi

# Activate venv
# shellcheck disable=SC1091
source "$VENV_DIR/bin/activate"

# ── 3. Upgrade pip & Install requirements ──────────────────────────────────────
info "Installing dependencies from requirements.txt..."
pip install --quiet -r requirements.txt || true

# ── 4. Install hauntshell in editable mode ─────────────────────────────────────
info "Installing HauntShell CLI..."
pip install --quiet -e . || true
if [[ "$OSTYPE" == "darwin"* ]]; then
    chflags -R 0 "$VENV_DIR" 2>/dev/null || true
    chflags 0 "$VENV_DIR"/lib/python*/site-packages/*.pth 2>/dev/null || true
fi
success "HauntShell installed. Run: haunt --help"

# ── 5. Create .env from .env.example ─────────────────────────────────────────
if [ ! -f ".env" ]; then
    info "Copying .env.example → .env"
    cp .env.example .env
    success ".env created."
else
    warn ".env already exists — skipping."
fi

# ── 6. Check Ollama & Gemma ───────────────────────────────────────────────────
echo ""
info "Checking for Ollama..."
if command -v ollama &>/dev/null; then
    success "Ollama found: $(ollama --version 2>/dev/null || echo 'version unknown')"
    info "Pulling recommended model (gemma3)... (optional, can also run completely offline)"
    ollama pull gemma3 || warn "Could not pull gemma3 — HauntShell will run with local fallback lore until you run: ollama pull gemma3"
else
    warn "Ollama not detected. HauntShell will run in offline necromancy mode!"
    info "To enable live open-weight AI inference, install Ollama from https://ollama.com"
fi

# ── Done ──────────────────────────────────────────────────────────────────────
echo ""
echo -e "${GREEN}╔════════════════════════════════════════════════════╗${RESET}"
echo -e "${GREEN}║  ✓  HauntShell is ready to haunt your terminal!    ║${RESET}"
echo -e "${GREEN}║                                                    ║${RESET}"
echo -e "${GREEN}║  Activate your environment:                        ║${RESET}"
echo -e "${GREEN}║    source .venv/bin/activate                       ║${RESET}"
echo -e "${GREEN}║                                                    ║${RESET}"
echo -e "${GREEN}║  Quick Start:                                      ║${RESET}"
echo -e "${GREEN}║    haunt seance clippy                             ║${RESET}"
echo -e "${GREEN}║    haunt ofrenda ada                               ║${RESET}"
echo -e "${GREEN}║    haunt exec \"kill -9 1337\"                       ║${RESET}"
echo -e "${GREEN}╚════════════════════════════════════════════════════╝${RESET}"
echo ""
