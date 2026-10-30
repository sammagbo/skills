#!/usr/bin/env python3
"""Bastão step 4: check that a pack covers what the repository revealed.

Usage: coverage_check.py <inventory.json> <folder> [--pair <other_language_folder>]

Fails (exit 1) when:
- a variable name from the inventory is not explained in document 5;
- a scheduled job (its time or its command) is missing from document 3;
- a service is missing from document 1 (only when the repository has one compose file;
  with several, missing services are warnings);
- a secret found in clear in the repository is not an open point in document 6;
- a {{field}} or a template comment is left;
- document 1, 4 or 6 is over 400 words (counted on the text a reader reads:
  no code blocks, no Markdown syntax, no table separators);
- document 4 has fewer than 3 or more than 4 symptoms;
- with --pair: headings, markers, checkboxes or table rows differ between languages.
Prints a table per document: words, markers, status.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _common import count_markers, count_words, doc_number, iter_docs  # noqa: E402

WORD_LIMIT = 400
FIXED_DOC4 = re.compile(r"^(avant tout|antes de tudo|qui appeler|quem chamar|après|depois|"
                        r"ce qu'il ne faut jamais|o que nunca|à ne jamais|nunca)", re.I)


def docs_by_number(folder: Path) -> dict[int, Path]:
    return {doc_number(p): p for p in iter_docs(folder)}


def headings(text: str) -> list[str]:
    return [ln for ln in text.splitlines() if re.match(r"^#{1,6}\s", ln)]


def shape(text: str) -> dict:
    return {
        "headings": len(headings(text)),
        "markers": count_markers(text),
        "checkboxes": len(re.findall(r"^\s*[-*]\s+\[[ xX]\]", text, re.M)),
        "table_rows": len([ln for ln in text.splitlines()
                           if ln.strip().startswith("|") and not re.fullmatch(r"\|?[\s:|-]+\|?", ln.strip())]),
    }


def check(inv: dict, folder: Path, problems: list, warnings: list) -> dict[int, str]:
    docs = docs_by_number(folder)
    texts = {n: p.read_text(encoding="utf-8") for n, p in docs.items()}
    for n in range(1, 7):
        if n not in docs:
            problems.append(f"document {n} missing in {folder}")
    for n, t in texts.items():
        if "{{" in t:
            problems.append(f"{docs[n].name}: unfilled {{{{field}}}}")
        if "<!--" in t:
            problems.append(f"{docs[n].name}: template comment left")
    if 5 in texts:
        for name in inv.get("variables", {}):
            if not re.search(rf"(?<![\w]){re.escape(name)}(?![\w])", texts[5]):
                problems.append(f"{docs[5].name}: variable {name} not explained")
    if 3 in texts:
        for job in inv.get("scheduled_jobs", []):
            cmd = job.get("command", "")
            base = re.sub(r"\.(sh|py|js|rb|php|pl)$", "", cmd)
            candidates = [job.get("time", ""), cmd, base, base.split(".")[-1]]
            hit = any(c and len(c) > 3 and c in texts[3] for c in candidates)
            if not hit:
                problems.append(f'{docs[3].name}: scheduled job {job.get("time") or job.get("schedule")} '
                                f'{cmd} ({job.get("source")}) not described')
    if 1 in texts:
        compose_count = len(inv.get("compose_files", []))
        for s in inv.get("services", []):
            names = [x for x in (s.get("name"), s.get("container_name")) if x]
            if not any(re.search(rf"(?<![\w-]){re.escape(x)}(?![\w-])", texts[1]) for x in names):
                msg = f'{docs[1].name}: service {s["name"]} ({s["compose_file"]}) not in "where it runs"'
                (problems if compose_count == 1 else warnings).append(msg)
    if 6 in texts:
        for sec in {s["name"] for s in inv.get("secrets_in_clear", [])}:
            if sec not in texts[6]:
                problems.append(f"{docs[6].name}: secret in clear {sec} is not an open point")
    if 4 in texts:
        symptoms = [h for h in headings(texts[4]) if h.startswith("## ")
                    and not FIXED_DOC4.match(h[3:].strip())]
        if not 3 <= len(symptoms) <= 4:
            problems.append(f"{docs[4].name}: {len(symptoms)} symptom(s), 3 or 4 expected")
    rows = {}
    for n, t in sorted(texts.items()):
        w = count_words(t)
        status = "ok"
        if n in (1, 4, 6) and w > WORD_LIMIT:
            status = f"over {WORD_LIMIT}"
            problems.append(f"{docs[n].name}: {w} words, limit {WORD_LIMIT}")
        rows[n] = f"| {docs[n].name} | {w} | {count_markers(t)} | {status} |"
    return rows


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("inventory")
    ap.add_argument("folder")
    ap.add_argument("--pair")
    a = ap.parse_args()
    inv = json.loads(Path(a.inventory).read_text(encoding="utf-8"))
    problems, warnings = [], []
    for folder in [Path(a.folder)] + ([Path(a.pair)] if a.pair else []):
        rows = check(inv, folder, problems, warnings)
        print(f"\n{folder}\n| Document | Words | Markers | Status |\n|---|---|---|---|")
        print("\n".join(rows.values()))
    if a.pair:
        d1, d2 = docs_by_number(Path(a.folder)), docs_by_number(Path(a.pair))
        for n in sorted(set(d1) & set(d2)):
            s1 = shape(d1[n].read_text(encoding="utf-8"))
            s2 = shape(d2[n].read_text(encoding="utf-8"))
            for k in s1:
                if s1[k] != s2[k]:
                    problems.append(f"parity document {n}: {k} {s1[k]} vs {s2[k]}")
    print()
    for w in warnings:
        print(f"WARNING {w}")
    for p in problems:
        print(f"FAIL {p}")
    print(f"{len(problems)} problem(s), {len(warnings)} warning(s)")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
