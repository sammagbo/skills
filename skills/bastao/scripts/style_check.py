#!/usr/bin/env python3
"""Bastão step 4: flag what makes a document read like a machine wrote it.

Usage: style_check.py <folder> [--lang fr|pt]

Checks every 0N-*.md document outside code blocks and inline code, with the rule
numbers of references/writing-style.md. Exit 1 with "file:line  rule N  detail"
when something is flagged, exit 0 otherwise. It flags; the agent decides and
rewrites, and notes in verification.md any flagged word kept on purpose.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _common import doc_language, iter_docs, prose_lines, strip_inline_code  # noqa: E402

STYLE_FILE = Path(__file__).resolve().parent.parent / "references" / "writing-style.md"
EMOJI = re.compile("[\U0001F300-\U0001FAFF☀-➿⭐⬆↔-⇿·•]")
RHETORIC = {"fr": re.compile(r"\bnon seulement\b|\bce n'est pas \w+, c'est\b", re.I),
            "pt": re.compile(r"\bnão só\b|\bnão apenas\b|\bnão é \w+, é\b", re.I)}
SMALL = {"de", "du", "des", "la", "le", "les", "et", "à", "a", "o", "os", "as", "e", "do", "da",
         "dos", "das", "em", "no", "na", "un", "une", "um", "uma", "par", "por", "pour", "para",
         "en", "ou", "qui", "que", "ce", "se", "si"}


def load_words() -> dict[str, list[str]]:
    """The flagged phrases, read from the 'Words the checker flags' sections."""
    out: dict[str, list[str]] = {"fr": [], "pt": []}
    lang = None
    for line in STYLE_FILE.read_text(encoding="utf-8").splitlines():
        if line.startswith("## Words the checker flags in French"):
            lang = "fr"
            continue
        if line.startswith("## Words the checker flags in Portuguese"):
            lang = "pt"
            continue
        if line.startswith("## "):
            lang = None
        if lang and ":" in line:
            items = line.split(":", 1)[1]
            for item in items.split(","):
                item = re.sub(r"\([^)]*\)", "", item).strip().rstrip(".")
                if item:
                    out[lang].append(item)
    return out


def title_case(heading: str) -> bool:
    words = [w for w in re.findall(r"[^\W\d_][\w'’-]*", heading) if w.lower() not in SMALL]
    if len(words) < 3:
        return False
    caps = sum(w[0].isupper() for w in words[1:])
    return caps >= max(2, (len(words) - 1) * 0.6)


def sentences(line: str):
    text = re.sub(r"^\s*([-*]\s+(\[[ xX]\]\s*)?|\d+\.\s+|#+\s*)", "", line)
    if text.strip().startswith("|"):
        cells = [c for c in text.split("|") if c.strip()]
    else:
        cells = [text]
    for cell in cells:
        for s in re.split(r"(?<=[.!?])\s+", cell):
            yield s


def check_file(path: Path, lang: str, words: dict[str, list[str]]) -> list[tuple]:
    out = []
    patterns = [(w, re.compile(rf"(?<![\w-]){re.escape(w)}(?![\w-])", re.I)) for w in words[lang]]
    text = path.read_text(encoding="utf-8")
    for no, raw in prose_lines(text):
        line = strip_inline_code(raw)
        if "—" in line:
            out.append((no, 1, "long dash"))
        if re.match(r"^\s*([-*]|\d+\.)\s+\*\*", line):
            out.append((no, 2, "bold label at the start of a list item"))
        heading = line.lstrip("# ")
        if line.startswith("# ") and ":" in heading:
            heading = heading.split(":", 1)[1]  # "<system name>: <title>", names keep their case
        if line.startswith("#") and title_case(heading):
            out.append((no, 3, "heading in Title Case"))
        if lang == "pt" and re.search("[“”‘’]", line):
            out.append((no, 4, "curly quotes in Portuguese"))
        if lang == "fr" and re.search("[“”]", line):
            out.append((no, 4, "English quotes in French, use « »"))
        if EMOJI.search(line):
            out.append((no, 5, "emoji, symbol or middle dot"))
        for w, pat in patterns:
            if pat.search(line):
                out.append((no, 7, f'flagged word "{w}"'))
        if RHETORIC[lang].search(line):
            out.append((no, 9, "rhetorical pair"))
        for s in sentences(line):
            n = len(re.findall(r"[^\W_]+(?:['’][^\W_]+)*", s))
            if n > 35:
                out.append((no, 17, f"sentence of {n} words"))
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("folder")
    ap.add_argument("--lang", choices=["fr", "pt"])
    a = ap.parse_args()
    words = load_words()
    total = 0
    for path in iter_docs(Path(a.folder)):
        lang = a.lang or doc_language(path)
        for no, rule, detail in check_file(path, lang, words):
            print(f"{path.name}:{no}  rule {rule}  {detail}")
            total += 1
    print(f"{total} flag(s)")
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main())
