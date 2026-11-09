#!/usr/bin/env python3
"""Bastão step 4: flag what makes a document read like a machine wrote it.

Usage: style_check.py <folder> [--lang fr|pt] [--max-words N] [--max-sentences N]

Checks every 0N-*.md document and every proposition-0N-* / proposta-0N-* proposal
outside code blocks, comments and inline code,
with the rule numbers of references/writing-style.md. Exit 1 with
"file:line  rule N  detail" when something is flagged, exit 0 otherwise. It
flags; the agent decides and rewrites, and notes in verification.md any
flagged word kept on purpose.

Rules 21 and 22 (adapted from ASD-STE100) are read on blocks, not on lines: a
paragraph is its consecutive prose lines, a list item is its line and the
lines that continue it, a table cell is a block of its own. Sentence limit:
20 words in documents 3 and 4, 25 in the others (--max-words N replaces both).
Paragraph limit: 3 sentences, and 6 for a list item or a table cell in
documents 3 and 4, where it can hold a short procedure (--max-sentences N
replaces every limit). A URL, an e-mail address and a {{field}} count as one
word; inline code counts as none. A period after a title or a reference
abbreviation ("M.", "Sr.", "Dr.", "n.", "p.") ends no sentence, nor does a
mark followed by a lowercase word or a closing quote (« Erreur ! » quand...).

Rule 31 (the skill's own): documents 1, 4 and 6 hold no technical term of the
jargon lists of writing-style.md; a product name with what it does is for you to judge.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _common import doc_language, doc_number, iter_docs, iter_proposals, prose_lines  # noqa: E402

STYLE_FILE = Path(__file__).resolve().parent.parent / "references" / "writing-style.md"
PROCEDURE_DOCS = (3, 4)
PLAIN_DOCS = (1, 4, 6)  # no technical term (rule 31)
PROCEDURE_LIMIT = 20
DESCRIPTIVE_LIMIT = 25
PROSE_SENTENCES = 3
PROCEDURE_ITEM_SENTENCES = 6  # a list item or a table cell in documents 3 and 4
EMOJI = re.compile("[\U0001F300-\U0001FAFF☀-➿⭐⬆↔-⇿·•]")
RHETORIC = {"fr": re.compile(r"\bnon seulement\b|\bce n'est pas \w+, c'est\b", re.I),
            "pt": re.compile(r"\bnão só\b|\bnão apenas\b|\bnão é \w+, é\b", re.I)}
SMALL = {"de", "du", "des", "la", "le", "les", "et", "à", "a", "o", "os", "as", "e", "do", "da",
         "dos", "das", "em", "no", "na", "un", "une", "um", "uma", "par", "por", "pour", "para",
         "en", "ou", "qui", "que", "ce", "se", "si"}

# A period after these ends no sentence: titles before a name, references before a number.
ABBREVIATIONS = ("M", "Dr", "Dra", "Sr", "Sra", "Srta", "Prof", "Profa", "Eng", "ex", "p", "n", "art", "cf")
SENTENCE_END = re.compile("".join(rf"(?<!\b{a}\.)" for a in ABBREVIATIONS)
                          + r"(?<=[.!?])\s+(?![a-zà-öø-ÿ»”’)\]])")
WORD = re.compile(r"https?://\S+|[\w.+-]+@[\w-]+(?:\.[\w-]+)+|\{\{[^}]*\}\}|[^\W_]+(?:['’][^\W_]+)*")
LIST_ITEM = re.compile(r"^\s*([-*+]|\d+[.)])\s+(\[[ xX]\]\s*)?")
CODE = "\x00"  # inline code: not a word, not a lowercase letter, not a space
TABLE_SEPARATOR = re.compile(r"\|?[\s:|-]+\|?")
THEMATIC_BREAK = re.compile(r"(-{3,}|\*{3,}|_{3,})")


def load_words() -> dict[str, list[str]]:
    """The flagged phrases, read from the 'Words the checker flags' sections."""
    out: dict[str, list[str]] = {"fr": [], "pt": [], "jargon_fr": [], "jargon_pt": []}
    lang = None
    sections = {"## Words the checker flags in French": "fr",
                "## Words the checker flags in Portuguese": "pt",
                "## Jargon the checker flags in documents 1, 4 and 6, in French": "jargon_fr",
                "## Jargon the checker flags in documents 1, 4 and 6, in Portuguese": "jargon_pt"}
    for line in STYLE_FILE.read_text(encoding="utf-8").splitlines():
        if line in sections:
            lang = sections[line]
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


def word_count(sentence: str) -> int:
    return len(WORD.findall(sentence))


def without_code(line: str) -> str:
    """One-line comments and inline code out; code leaves a mark that is neither a word nor a space."""
    return re.sub(r"`[^`]*`", CODE, re.sub(r"<!--.*?-->", " ", line))


def blocks(lines):
    """Group (line_number, text) pairs into (kind, [(line_number, text), ...]).

    kind is "para" (consecutive prose lines), "item" (a list item and the lines
    that continue it), "cell" (one table cell) or "heading".
    """
    out, cur, prev = [], None, None
    for no, line in lines:
        s = line.strip()
        contiguous = prev is not None and no == prev + 1
        prev = no
        if not s or THEMATIC_BREAK.fullmatch(s):
            cur = None
            continue
        if s.startswith("#"):
            cur = None
            out.append(("heading", [(no, s.lstrip("#").strip())]))
            continue
        if s.startswith(">") and not s.lstrip(">").strip():
            cur = None  # an empty quote line ends the quoted paragraph
            continue
        if s.startswith("|"):
            cur = None
            if not TABLE_SEPARATOR.fullmatch(s):
                out.extend(("cell", [(no, c.strip())]) for c in s.strip("|").split("|") if c.strip())
            continue
        m = LIST_ITEM.match(line)
        if m:
            cur = ("item", [(no, line[m.end():].strip())])
            out.append(cur)
            continue
        text = s.lstrip(">").strip()
        if cur is not None and contiguous:
            cur[1].append((no, text))  # a continuation line, or a lazy one after a list item
            continue
        cur = ("para", [(no, text)])
        out.append(cur)
    return out


def block_sentences(parts):
    """The sentences of a block read across its lines, each with the line it starts on."""
    joined, starts = "", []
    for no, text in parts:
        if joined:
            joined += " "
        starts.append((len(joined), no))
        joined += text
    pos = 0
    for m in list(SENTENCE_END.finditer(joined)) + [None]:
        end = m.start() if m else len(joined)
        sentence = joined[pos:end]
        if word_count(sentence):
            yield max(no for off, no in starts if off <= pos), sentence
        if m:
            pos = m.end()


def check_file(path: Path, lang: str, words: dict[str, list[str]],
               max_words: int | None = None, max_sentences: int | None = None) -> list[tuple]:
    out = []
    patterns = [(w, re.compile(rf"(?<![\w-]){re.escape(w)}(?![\w-])", re.I)) for w in words[lang]]
    jargon = ([(w, re.compile(rf"(?<![\w-]){re.escape(w)}(?![\w-])", re.I)) for w in words["jargon_" + lang]]
              if doc_number(path) in PLAIN_DOCS else [])
    limit = max_words or (PROCEDURE_LIMIT if doc_number(path) in PROCEDURE_DOCS else DESCRIPTIVE_LIMIT)
    text = path.read_text(encoding="utf-8")
    lines = []
    for no, raw in prose_lines(text):
        line = without_code(raw)
        lines.append((no, line))
        if "—" in line:
            out.append((no, 1, "long dash"))
        if re.match(r"^\s*([-*+]|\d+[.)])\s+\*\*", line):
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
        for w, pat in jargon:
            if pat.search(line):
                out.append((no, 31, f'technical term "{w}", use the plain expression'))
        if RHETORIC[lang].search(line):
            out.append((no, 9, "rhetorical pair"))
    for kind, parts in blocks(lines):
        found = list(block_sentences(parts))
        for no, sentence in found:
            n = word_count(sentence)
            if n > limit:
                out.append((no, 21, f"sentence of {n} words, limit {limit}"))
        if kind == "heading":
            continue
        procedure = kind != "para" and doc_number(path) in PROCEDURE_DOCS
        cap = max_sentences or (PROCEDURE_ITEM_SENTENCES if procedure else PROSE_SENTENCES)
        if len(found) > cap:
            name = {"para": "paragraph", "item": "list item", "cell": "table cell"}[kind]
            out.append((parts[0][0], 22, f"{name} of {len(found)} sentences, limit {cap}"))
    return sorted(out, key=lambda f: (f[0], f[1]))


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("folder")
    ap.add_argument("--lang", choices=["fr", "pt"])
    ap.add_argument("--max-words", type=int, default=None,
                    help="one sentence limit for every document, instead of 20/25")
    ap.add_argument("--max-sentences", type=int, default=None,
                    help="one paragraph limit for every block, instead of 3 (6 for items in documents 3 and 4)")
    a = ap.parse_args()
    if not Path(a.folder).is_dir():
        print(f"not a folder: {a.folder} (give an absolute path)", file=sys.stderr)
        return 2
    words = load_words()
    total = 0
    # The six documents and the proposals: a proposal is the agent's own text, so it is checked too.
    for path in sorted(iter_docs(Path(a.folder)) + iter_proposals(Path(a.folder)), key=lambda p: p.name):
        lang = a.lang or doc_language(path)
        for no, rule, detail in check_file(path, lang, words, a.max_words, a.max_sentences):
            print(f"{path.name}:{no}  rule {rule}  {detail}")
            total += 1
    print(f"{total} flag(s)")
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main())
