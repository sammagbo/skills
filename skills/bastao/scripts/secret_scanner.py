#!/usr/bin/env python3
"""Bastão step 4: refuse any secret in a generated pack.

Usage: secret_scanner.py <folder> [--inventory inventory.json] [--repo <repo_path>]

Scans every .md, .yml and .json file in <folder> (answers.yml included).
Exit 1 with "file:line  category  masked excerpt" for each finding, exit 0 otherwise.
It never writes what it finds to a file and never prints a whole value.

--inventory: compares against the digests of inline secret values found by
inventory.py (rule 6). --repo: reads the repository's .env files only to hash
the values of secret-named keys, in memory, and checks that none appears in
the pack (rule 7). Nothing from .env is printed or stored.
"""
from __future__ import annotations

import argparse
import base64
import binascii
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _common import MARKERS, SECRET_WORDS, contains_digest, digest, is_secret_name  # noqa: E402

PLACEHOLDER_VALUES = re.compile(
    r"^(\(|\{\{|\[|<|xxx|\*\*\*|\.\.\.|change[-_]?me|changeme|example|exemple|exemplo|"
    r"your[-_]|votre|seu[-_]|sua[-_]|none|null|vide|vazio|empty|todo|tbd|-|—|\$\{|\$[A-Z_]|"
    r"\"\$|'\$|%|non|não|nao|dans|no |na |em |le |la |o |a )", re.I)
ASSIGN = re.compile(
    r"\b([A-Za-z_][\w.\-]*?(?:" + "|".join(SECRET_WORDS) + r")[\w.\-]*)\s*(?:=|:)\s*([^\s|,;`]+)",
    re.I)
CRED_URL = re.compile(r"\b[a-z][a-z0-9+.\-]*://[^\s/:@]+:([^\s/@]+)@", re.I)
CMD_SECRET = re.compile(
    r"(PGPASSWORD=\S+|MYSQL_PWD=\S+|--password[= ]\S+|\bsshpass\b|curl\s[^|]*-u\s+\S+:\S+|"
    r"Authorization:\s*(Bearer|Basic)\s+[A-Za-z0-9+/=._\-]{8,}|\s-p[^\s\-]\S{3,})", re.I)
KNOWN_FORMATS = re.compile(
    r"(-----BEGIN [A-Z ]*PRIVATE KEY-----|\bAKIA[0-9A-Z]{16}\b|\bghp_[A-Za-z0-9]{20,}|"
    r"\bgithub_pat_\w{20,}|\bglpat-[\w\-]{20,}|\bsk-[A-Za-z0-9]{20,}|\bxox[abp]-[\w\-]{10,}|"
    r"\beyJ[\w\-]+\.eyJ[\w\-]+\.[\w\-]+|ssh-(rsa|ed25519) AAAA)")
TOKEN = re.compile(r"[^\s|`'\"()\[\]{}<>,;]{12,}")


def masked(s: str) -> str:
    s = s.strip()
    return (s[:3] + "…") if len(s) > 3 else "…"


def looks_like_password(tok: str, known_names: set[str]) -> bool:
    t = tok.strip(".:;!?*")
    if len(t) < 12 or t in known_names:
        return False
    if re.fullmatch(r"[0-9a-f]{7,40}", t) or re.fullmatch(r"[\d/:.\-]+", t):
        return False
    if "/" in t or "@" in t or "://" in t or t.startswith(("$", "~", "-")):
        return False
    t = re.sub(r":\d+(-\d+)?$", "", t)  # file:line
    if re.fullmatch(r"[\w.\-]+\.[A-Za-z]{1,5}", t) or t.startswith("+%"):  # file, host, date format
        return False
    if re.fullmatch(r"[A-Z0-9_]+", t) or re.fullmatch(r"[a-z0-9_.\-]+", t):
        return False  # constant name, or lowercase identifier
    if re.fullmatch(r"([A-Za-zÀ-ÿ]+[\-'’])+[A-Za-zÀ-ÿ]+", t):
        return False  # hyphenated words
    classes = sum(bool(re.search(p, t)) for p in (r"[a-z]", r"[A-Z]", r"\d", r"[^\w]"))
    return classes >= 3


def quoted_sentence(rest: str) -> bool:
    """True when the value is a quoted phrase with spaces, like "kept on Sam's PC"."""
    q = rest[:1]
    if q not in ("'", '"'):
        return False
    end = rest.find(q, 1)
    return end > 0 and " " in rest[1:end]


def b64_hidden_secret(tok: str) -> bool:
    """A base64 blob that decodes to readable text with a secret-ish word."""
    if len(tok) < 16 or not re.fullmatch(r"[A-Za-z0-9+/]+={0,2}", tok):
        return False
    try:
        raw = base64.b64decode(tok + "=" * (-len(tok) % 4), validate=True)
        txt = raw.decode("utf-8")
    except (binascii.Error, UnicodeDecodeError, ValueError):
        return False
    return txt.isprintable() and len(txt) >= 12


def env_digests(repo: Path) -> list[dict]:
    out = []
    for p in repo.rglob("*"):
        if ".git" in p.parts or not p.is_file():
            continue
        n = p.name
        if not (n == ".env" or n.startswith(".env.") or n.endswith(".env")):
            continue
        if re.search(r"(example|sample|template|dist)", n, re.I):
            continue
        for line in p.read_text(encoding="utf-8", errors="replace").splitlines():
            k, sep, v = line.partition("=")
            v = v.strip().strip("'\"")
            if sep and is_secret_name(k.strip()) and len(v) >= 6:
                out.append({"name": k.strip(), "file": str(p.relative_to(repo)), **digest(v)})
    return out


def scan(folder: Path, inv: dict | None, envd: list[dict]) -> list[tuple]:
    findings, warnings = [], []
    known = set((inv or {}).get("variables", {}).keys())
    inline = (inv or {}).get("inline_secret_digests", [])
    files = sorted(p for p in folder.rglob("*")
                   if p.is_file() and p.suffix in (".md", ".yml", ".yaml", ".json")
                   and p.name != "inventory.json")
    for f in files:
        rel = str(f.relative_to(folder))
        for no, line in enumerate(f.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
            if not line.strip():
                continue
            for m in ASSIGN.finditer(line):
                if quoted_sentence(line[m.start(2):]):
                    continue
                value = m.group(2).strip().strip("'\"")
                if value and not PLACEHOLDER_VALUES.match(value) and \
                   not any(value.startswith(x) for x in MARKERS) and value.lower() != "null":
                    findings.append((rel, no, "1 assignment", masked(value)))
            for m in CRED_URL.finditer(line):
                if not m.group(1).startswith(("${", "$", "{{", "[")):
                    findings.append((rel, no, "2 credential URL", masked(m.group(0))))
            for m in CMD_SECRET.finditer(line):
                findings.append((rel, no, "3 secret in command", masked(m.group(0))))
            for m in KNOWN_FORMATS.finditer(line):
                findings.append((rel, no, "4 key format", masked(m.group(0))))
            for m in TOKEN.finditer(line):
                tok = m.group(0)
                if looks_like_password(tok, known):
                    findings.append((rel, no, "5 password-like", masked(tok)))
                elif b64_hidden_secret(tok.strip(".:;")):
                    findings.append((rel, no, "5b base64 value", masked(tok)))
            for d in inline:
                if contains_digest(line, d):
                    if d.get("common_word"):
                        warnings.append((rel, no, f'6 inline value of {d["name"]} equals a service or image '
                                                  f'name: check this line by hand, note it in verification.md', "…"))
                    else:
                        findings.append((rel, no, f'6 inline value of {d["name"]}', "…"))
            for d in envd:
                if contains_digest(line, d):
                    findings.append((rel, no, f'7 .env value of {d["name"]}', "…"))
    return findings, warnings


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("folder")
    ap.add_argument("--inventory")
    ap.add_argument("--repo")
    a = ap.parse_args()
    folder = Path(a.folder)
    inv = json.loads(Path(a.inventory).read_text(encoding="utf-8")) if a.inventory else None
    envd = env_digests(Path(a.repo)) if a.repo else []
    findings, warnings = scan(folder, inv, envd)
    for rel, no, cat, ex in findings:
        print(f"{rel}:{no}  {cat}  {ex}")
    for rel, no, cat, ex in warnings:
        print(f"{rel}:{no}  WARNING {cat}")
    checks = "rules 1-5" + (", 6" if inv else "") + (", 7" if a.repo else "")
    print(f"{len(findings)} finding(s) ({checks})")
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
