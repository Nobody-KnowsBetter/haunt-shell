"""Tests for the autopsy subject preparation and crash classification."""

from pathlib import Path
from hauntshell.autopsy import prepare_autopsy_subject, detect_content_type, build_autopsy_system_prompt


def test_detect_content_type():
    assert detect_content_type("error.py", "Traceback (most recent call last):") == "Python Exception"
    assert detect_content_type("core.dump", "Segmentation fault (core dumped)") == "C/C++ Memory Casualty"
    assert detect_content_type("main.rs", "thread 'main' panicked at 'explicit panic'") == "Rust Panic"
    assert detect_content_type("index.js", "TypeError: Cannot read properties of undefined") == "JavaScript/Node Casualty"
    assert detect_content_type("Main.java", "Exception in thread java.lang.NullPointerException") == "JVM Catastrophe"
    assert detect_content_type("patch.diff", "diff --git a/file b/file") == "Git Commit Demise"
    assert detect_content_type("random.txt", "Some ordinary text") == "Unknown Digital Relic"


def test_prepare_autopsy_subject_inline():
    trace = "Traceback (most recent call last):\n  File 'app.py', line 12\nZeroDivisionError"
    subj = prepare_autopsy_subject(trace)
    assert subj.target_name == "Terminal Exception / Trace"
    assert subj.detected_type == "Python Exception"
    assert "ZeroDivisionError" in subj.content


def test_prepare_autopsy_subject_file(tmp_path: Path):
    f = tmp_path / "crash.log"
    f.write_text("Segmentation fault: 11 at address 0x00000000", encoding="utf-8")
    subj = prepare_autopsy_subject(str(f))
    assert subj.target_name == str(f)
    assert subj.detected_type == "C/C++ Memory Casualty"
    assert "0x00000000" in subj.content


def test_build_autopsy_system_prompt():
    prompt = build_autopsy_system_prompt()
    assert "Dr. Victor von Necro" in prompt
    assert "The Mortal Wound" in prompt
    assert "The Resurrection Rite" in prompt
