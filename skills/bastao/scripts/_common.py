"""Shared helpers for the Bastão scripts. Standard library only."""
from __future__ import annotations

import hashlib
import re
from pathlib import Path

MARKERS = ("[À CONFIRMER", "[A CONFIRMAR")
SECRET_WORDS = (
    "PASSWORD", "PASSWD", "PWD", "SECRET", "TOKEN", "API_KEY", "APIKEY",
    "PRIVATE_KEY", "ACCESS_KEY", "CLIENT_SECRET", "JWT", "PIN", "SENHA",
    "MOT_DE_PASSE", "CLE", "CREDENTIAL",
)
_SECRET_NAME_RE = re.compile(
    r"(^|[_.\-])(" + "|".join(SECRET_WORDS) + r")([_.\-]|$)", re.IGNORECASE
)

PT_NAMES = ("01-o-que-e", "02-quem-faz-o-que", "03-rotina", "04-se-quebrar",
            "05-custodia-de-acessos", "06-checklist-de-recepcao")


def is_secret_name(name: str) -> bool:
    """True when a variable name suggests it holds a secret."""
    return bool(_SECRET_NAME_RE.search(name))


def digest(value: str) -> dict:
    """Length and SHA-256 of a value. The value itself is never stored."""
    return {"len": len(value), "sha256": hashlib.sha256(value.encode("utf-8")).hexdigest()}


def contains_digest(text: str, d: dict) -> bool:
    """Slide a window of the digest's length over the text and compare hashes."""
    n = d["len"]
    if n < 6 or len(text) < n:
        return False
    target = d["sha256"]
    for i in range(len(text) - n + 1):
        if hashlib.sha256(text[i:i + n].encode("utf-8")).hexdigest() == target:
            return True
    return False


def doc_language(path: Path) -> str:
    stem = path.stem
    if stem in PT_NAMES or "passagem" in path.parts:
        return "pt"
    return "fr"


def iter_docs(folder: Path):
    """The Markdown documents of a pack folder, sorted."""
    return sorted(p for p in folder.glob("*.md") if re.match(r"0[1-6]-", p.name))


def doc_number(path: Path) -> int:
    return int(path.name[:2])


def prose_lines(text: str):
    """Yield (line_number, line) outside fenced code blocks and HTML comments."""
    in_code = False
    in_comment = False
    for no, line in enumerate(text.splitlines(), 1):
        stripped = line.strip()
        if stripped.startswith("```"):
            in_code = not in_code
            continue
        if in_code:
            continue
        if in_comment:
            if "-->" in line:
                in_comment = False
            continue
        if "<!--" in line and "-->" not in line:
            in_comment = True
            continue
        yield no, line


def strip_inline_code(line: str) -> str:
    return re.sub(r"`[^`]*`", " ", line)


def count_words(text: str) -> int:
    """Words a reader reads: no code blocks, no Markdown syntax, no table separators."""
    words = 0
    for _, line in prose_lines(text):
        s = line.strip()
        if re.fullmatch(r"\|?[\s:|-]+\|?", s) or s == "---":
            continue
        s = strip_inline_code(s)
        s = re.sub(r"^#+\s*", "", s)
        s = re.sub(r"^[-*]\s+\[[ xX]\]\s*", "", s)
        s = re.sub(r"^[-*]\s+", "", s)
        s = re.sub(r"^\d+\.\s+", "", s)
        s = s.replace("|", " ").replace("**", " ")
        words += len(re.findall(r"[^\W_]+(?:['’][^\W_]+)*", s))
    return words


def count_markers(text: str) -> int:
    return sum(text.count(m) for m in MARKERS)
