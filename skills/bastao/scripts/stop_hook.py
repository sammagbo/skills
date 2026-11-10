#!/usr/bin/env python3
"""Bastão end-of-turn hook for Claude Code (the Stop event).

Reads the hook input, a JSON object, on stdin. When a handover pack exists in the
repository and a file it depends on, or its questions file, is newer than the
pack's verification.md, it prints one JSON object that hands Claude a line to act
on, and Claude goes on with it. Otherwise it prints nothing. It always exits 0.

It stays fast: file times only. No model, no network, and no file is opened: the
hook never reads a .env file, or any other file, only looks at names and times.

Contract: references/pack-files.md, section "Hook contract".
"""
from __future__ import annotations

import json
import os
import re
import subprocess
import sys
from pathlib import Path

SKIP_DIRS = {".git", "node_modules", "target", "build", "dist", ".venv", "venv",
             "__pycache__", ".idea", ".gradle"}
MAX_FILES = 20000  # a very large repository: stop looking, stay fast
QUESTIONS = ("00-questions.md", "00-perguntas.md")

COMPOSE = re.compile(r"^(docker-)?compose.*\.ya?ml$|^Dockerfile.*$", re.I)
CRON_SYSTEMD = re.compile(r"cron|\.timer$|\.service$", re.I)
ENV_EXAMPLE = re.compile(r"^\.env\.(.*\.)?(example|sample|template|dist|defaults?)$|^.*\.env\.example$", re.I)
OPS_DOC = re.compile(r"(deploy|install|operac|operat|runbook|handoff|handover|passation|passagem|backup|"
                     r"restor|incident|procedure|setup)", re.I)
JOB_SCRIPT = re.compile(r"(backup|import|sync|export|restore|cleanup|purge|renew|migrat)", re.I)
README = re.compile(r"^README(\..*)?$", re.I)
SPRING = re.compile(r"^application.*\.properties$", re.I)


def repo_root(cwd: Path) -> Path:
    try:
        out = subprocess.run(["git", "-C", str(cwd), "rev-parse", "--show-toplevel"],
                             capture_output=True, text=True, timeout=5)
        if out.returncode == 0 and out.stdout.strip():
            return Path(out.stdout.strip())
    except (OSError, subprocess.SubprocessError):
        pass
    return cwd


def is_pack(folder: Path) -> bool:
    return (folder / "inventory.json").is_file() and (folder / "verification.md").is_file()


def find_packs(repo: Path) -> list[Path]:
    """passation/ and passagem/ first, then every first-level folder of the repository."""
    seen, packs = set(), []
    names = ["passation", "passagem"] + sorted(p.name for p in repo.iterdir()
                                              if p.is_dir() and p.name not in SKIP_DIRS and not p.name.startswith("."))
    for name in names:
        folder = repo / name
        if name not in seen and folder.is_dir() and is_pack(folder):
            packs.append(folder)
        seen.add(name)
    return packs


def mtime(path: Path) -> float:
    try:
        return path.stat().st_mtime
    except OSError:
        return 0.0


def in_successor_list(path: Path, rel_parts: tuple[str, ...]) -> bool:
    """The files a handover pack depends on, judged by name only."""
    name = path.name
    if COMPOSE.match(name) or ENV_EXAMPLE.match(name) or README.match(name) or SPRING.match(name):
        return True
    if CRON_SYSTEMD.search(name) or "cron.d" in rel_parts:
        return True
    suffix = path.suffix.lower()
    if suffix in (".md", ".txt", ".rst") and OPS_DOC.search("/".join(rel_parts)):
        return True
    if suffix in (".sh", ".py", ".ps1", ".bat", ".js", ".sql") and JOB_SCRIPT.search(path.stem):
        return True
    return False


def newer_file(repo: Path, pack_dirs: set[Path], since: float) -> Path | None:
    """The first file of the successor list that changed after `since`, or None."""
    seen = 0
    for root, dirs, files in os.walk(repo):
        here = Path(root)
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS and (here / d) not in pack_dirs]
        for f in files:
            seen += 1
            if seen > MAX_FILES:
                return None
            p = here / f
            rel = p.relative_to(repo).parts
            if mtime(p) > since and in_successor_list(p, rel):
                return p
    return None


def main() -> int:
    try:
        data = json.loads(sys.stdin.read() or "{}")
        if not isinstance(data, dict):
            data = {}
    except ValueError:
        data = {}
    if data.get("stop_hook_active"):
        return 0  # Claude is already going on because of this hook: never loop
    cwd = Path(data.get("cwd") or os.environ.get("CLAUDE_PROJECT_DIR") or os.getcwd())
    if not cwd.is_dir():
        return 0
    repo = repo_root(cwd)
    packs = find_packs(repo)
    if not packs:
        return 0  # no pack yet: the first run always comes from the user
    pack_dirs = {p.resolve() for p in packs}
    # A second-language folder is a sibling without inventory.json: skip it too.
    for name in ("passation", "passagem"):
        if (repo / name).is_dir():
            pack_dirs.add((repo / name).resolve())
    for pack in packs:
        since = mtime(pack / "verification.md")
        changed = next((pack / q for q in QUESTIONS if mtime(pack / q) > since), None)
        changed = changed or newer_file(repo.resolve(), pack_dirs, since)
        if changed:
            text = (f"Bastão hook: repository {repo}, pack {pack}. "
                    f"Use the bastao skill to update the pack: files it describes changed, whatever this session did.")
            print(json.dumps({"hookSpecificOutput": {"hookEventName": "Stop", "additionalContext": text}},
                             ensure_ascii=False))
            return 0
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception:  # a hook must never break the session
        sys.exit(0)
