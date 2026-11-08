# Changelog

## Unreleased

- Passive mode. The skill writes first from the repository, marks the gaps and leaves its questions in `00-questions.md` / `00-perguntas.md`, which the developer answers when they can. No interview: a question in the chat only when a whole document is blocked (two cases, rule 12). Later runs update only what changed; a document edited by hand is never overwritten. `references/pack-files.md` gives the format of every file of a pack and the contract of the end-of-turn hook (Claude Code `Stop` event) that the plugin will ship.
- Writing rules adapted from ASD-STE100 (Simplified Technical English, Issue 9) to French and Portuguese, as rules 21 to 30 of `references/writing-style.md`, with a table of approved words aligned with the templates. The skill claims no conformance to the standard and no approval by ASD.
- `style_check.py` reads sentences and paragraphs across lines, enforces rule 21 (20 words per sentence in documents 3 and 4, 25 elsewhere) and rule 22 (three sentences per paragraph, list item or table cell; six for a list item or table cell in documents 3 and 4), counts a URL, an e-mail address or a `{{field}}` as one word, and ends no sentence after an abbreviation such as "M." or "Sr.", or before a closing quote. `--max-words N` and `--max-sentences N` replace the limits.
- `coverage_check.py` accepts a draft document 4 with fewer than three symptoms when it points to the pack's questions file, and says so with a warning; it fails when the line names a questions file that is not in the pack.
- `inventory.py` skips the pack's own files by their names, wherever they are, and every `--skip` folder. `style_check.py` and `coverage_check.py` skip the questions file and the proposals written beside documents edited by hand; `secret_scanner.py` reads them.
- Templates: sentences shortened to the new limits; the restore warning now comes before the step; "programme" / "programa" for the program on the machine; plain words for the backup in document 1 (Portuguese) and document 6 (both languages); rule 5 of document 5 back to three sentences; about 380 words for document 1, as in rule 5.
- Known: `examples/estante/` and `tests/fixtures/estante-pack-r3/` predate rules 21 and 22. They will be regenerated in the next test round; until then the unit test checks the round 3 pack with `--max-words 35 --max-sentences 99`.

## Bastão 0.1.0 (2026-10-30)

First version that can be tried.

- Six documents in French and Brazilian Portuguese, from the repository and ten questions, with up to three follow-up questions.
- Four check scripts (standard library, no network): inventory, secret scanner, coverage check with word counts and FR/PT parity, style check.
- A fictional repository, a full simulated run and unit tests, so the skill can be tested without real data.
- A complete example pack in `examples/estante/`.

Tested on a real system (two rounds, private) and on the fictional repository (two rounds, public).
