#!/usr/bin/env python3
"""Bastão step 4: check that a pack covers what the repository revealed.

Usage: coverage_check.py <inventory.json> <folder> [--pair <other_language_folder>] [--merged]

With --merged, a proposal (proposition-0N-... / proposta-0N-...) stands in for the document
it sits beside: the check is made on the pack as it will be once the user has merged.
While proposals are pending, this is the result to record.

Fails (exit 1) when:
- a variable name from the inventory is not explained in document 5;
- a scheduled job (its time or its command) is missing from document 3;
- a service is missing from document 1 (only when the repository has one compose file;
  with several, missing services are warnings);
- a secret found in clear in the repository is not an open point in document 6;
- a {{field}} or a template comment is left;
- document 1 or 4 is over 400 words, or document 6 over 450 (it holds two parts and the
  signatures; counted on the text a reader reads:
  no code blocks, no Markdown syntax, no table separators);
- document 4 has more than 4 symptoms, or fewer than 3 without a line that sends
  the reader to the questions file (00-questions.md or 00-perguntas.md, in this
  folder or in the --pair folder); with that line, fewer than 3 is a warning:
  the pack is a draft; a line that names a questions file that does not exist
  fails;
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

WORD_LIMIT = {1: 400, 4: 400, 6: 450}  # one page each; document 6 holds two parts and the signatures
FIXED_DOC4 = re.compile(r"^(avant tout|antes de tudo|qui appeler|quem chamar|après|depois|"
                        r"ce qu'il ne faut jamais|o que nunca|à ne jamais|nunca)", re.I)
QUESTIONS_FILE = re.compile(r"00-(questions|perguntas)\.md")


def docs_by_number(folder: Path, merged: bool = False) -> dict[int, Path]:
    return {doc_number(p): p for p in iter_docs(folder, merged)}


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


def check(inv: dict, folder: Path, problems: list, warnings: list,
          other: Path | None = None, merged: bool = False) -> dict[int, str]:
    docs = docs_by_number(folder, merged)
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
            if not any(re.search(rf"(?<![\w-]){re.escape(x)}(?![\w-])", texts[1], re.I) for x in names):
                msg = f'{docs[1].name}: service {s["name"]} ({s["compose_file"]}) not in "where it runs"'
                (problems if compose_count == 1 else warnings).append(msg)
    if 6 in texts:
        for sec in {s["name"] for s in inv.get("secrets_in_clear", [])}:
            if sec not in texts[6]:
                problems.append(f"{docs[6].name}: secret in clear {sec} is not an open point")
    if 4 in texts:
        symptoms = [h for h in headings(texts[4]) if h.startswith("## ")
                    and not FIXED_DOC4.match(h[3:].strip())]
        pointer = QUESTIONS_FILE.search(texts[4])
        if pointer and not any((f / pointer.group(0)).is_file() for f in (folder, other) if f):
            problems.append(f"{docs[4].name}: names {pointer.group(0)}, which is not in the pack")
        if len(symptoms) > 4 or (len(symptoms) < 3 and not pointer):
            problems.append(f"{docs[4].name}: {len(symptoms)} symptom(s), 3 or 4 expected")
        elif len(symptoms) < 3:
            warnings.append(f"{docs[4].name}: {len(symptoms)} symptom(s), the others wait in the "
                            f"questions file; the pack is a draft")
    rows = {}
    for n, t in sorted(texts.items()):
        w = count_words(t)
        status = "ok"
        if n in WORD_LIMIT and w > WORD_LIMIT[n]:
            status = f"over {WORD_LIMIT[n]}"
            problems.append(f"{docs[n].name}: {w} words, limit {WORD_LIMIT[n]}")
        rows[n] = f"| {docs[n].name} | {w} | {count_markers(t)} | {status} |"
    return rows


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("inventory")
    ap.add_argument("folder")
    ap.add_argument("--pair")
    ap.add_argument("--merged", action="store_true",
                    help="check the proposals in place of the documents they sit beside")
    a = ap.parse_args()
    for given in (a.inventory, a.folder, a.pair):
        if given and not Path(given).exists():
            print(f"not found: {given} (give an absolute path)", file=sys.stderr)
            return 2
    inv = json.loads(Path(a.inventory).read_text(encoding="utf-8"))
    problems, warnings = [], []
    first, second = Path(a.folder), Path(a.pair) if a.pair else None
    for folder, other in [(first, second)] + ([(second, first)] if second else []):
        rows = check(inv, folder, problems, warnings, other, a.merged)
        print(f"\n{folder}\n| Document | Words | Markers | Status |\n|---|---|---|---|")
        print("\n".join(rows.values()))
    if a.pair:
        d1, d2 = docs_by_number(Path(a.folder), a.merged), docs_by_number(Path(a.pair), a.merged)
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
