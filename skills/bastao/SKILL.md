---
name: bastao
description: Builds the handover pack (dossier de passation, pasta de passagem) for a system being handed to a non-technical organization: what it is and what it does not do, who does what, routines, what to do if it breaks, access custody without secrets, and a reception checklist, in French and Portuguese, generated from the repository and verified against it. Use when the user mentions passagem, passation, handover to a client or school, final delivery, successor, "who stays responsible", leaving a project, or documentation for the IT team that will keep the system. Not for agent-to-agent session handoffs.
---

# Bastão

Bastão produces the folder a non-technical organization needs to keep a system running after its developer leaves: six Markdown documents, in French and/or Brazilian Portuguese, filled from the repository and from ten questions, checked against the repository, written the way a careful person writes, with no secret inside.

## When to use it, and when not

Use it when the user is delivering a running system to the people who will keep it (a school, an association, a small business), is leaving a project, or needs documentation for the IT person who inherits a system.

Do not use it for passing a session from one agent to another (that is a handoff, not a handover), for developer onboarding (point to the README or a code tour skill), for an incident in progress (if the pack exists, open its document 4; otherwise help directly), or for a system not yet in production (the pack describes what runs, not plans).

## What you produce

A folder named by the user (default `passation/` for French, `passagem/` for Portuguese) containing, per language requested:

| Nº | File (FR) | File (PT) | Size |
|---|---|---|---|
| 1 | 01-ce-que-cest.md | 01-o-que-e.md | one page |
| 2 | 02-qui-fait-quoi.md | 02-quem-faz-o-que.md | two pages at most |
| 3 | 03-routine.md | 03-rotina.md | free |
| 4 | 04-si-ca-casse.md | 04-se-quebrar.md | one page |
| 5 | 05-garde-des-acces.md | 05-custodia-de-acessos.md | free; restricted distribution |
| 6 | 06-checklist-reception.md | 06-checklist-de-recepcao.md | one page |

Plus `answers.yml` (the developer's answers, no secrets), `inventory.json` (what the repository revealed, names only) and `verification.md` (the result of step 4). PDF export is optional, through the host's document skill, once the Markdown is approved.

## Rules that never bend

1. Never read, store or print a secret value. Read variable names from `.env.example`, `docker-compose*.yml`, systemd units and scripts; never open `.env`; never reproduce a value found inline in a compose file or a script. A value found in clear in the repository becomes an open point in document 6 ("secret in clear in the repository: NAME").
2. No address with credentials (`user:password@host`, token in a URL), no command with a password as argument or environment variable. When a procedure needs a secret, write "(the password is in {{vault}})" in the document's language.
3. Never invent. Anything the repository does not prove and the user did not answer is marked `[À CONFIRMER]` (FR) or `[A CONFIRMAR]` (PT). A marked gap beats a plausible sentence. Four fields keep the marker until the owner confirms them in person, whatever the repository suggests: `vault`, `last_restore_date`, `backup_offsite`, `backup_encrypted`.
4. Plain language for non-technical readers: every technical term is translated the first time it appears (`references/plain-language.md`). Names, dates, numbers; no adjectives.
5. One page for documents 1, 4 and 6 (about 350 to 380 words). Document 4 has three symptoms, four at most, taken from incidents that happened or almost happened.
6. French first, then Portuguese, when both are requested; identical section structure. `templates/<lang>/` is the only source of structure; field keys are identical in both languages (`references/fields.md`).
7. Everything stays local; nothing is sent to any service. The user reviews before delivering. Document 5 goes only to its two recipients.
8. Template comments (`<!-- -->`) are instructions to you: follow them, then strip them from the delivered documents.
9. If the user types a secret in the conversation, do not write it anywhere; say where it belongs and continue.
10. Write like a person, not like a model. Every sentence you put in a document follows `references/writing-style.md`: short sentences, simple verbs, the same word for the same thing, no long dash, no bold labels, no inflated vocabulary, no rhetorical pairs or triads, no closing pep talk. Step 4 includes a style pass. A document that fails it is not finished.

## Workflow

### Step 1: inventory the repository

Run `scripts/inventory.py <repo_path>` (until the script exists, do the same by reading). It writes `inventory.json`: project name (README title, compose project name), services and images, ports, volumes, scheduled jobs (cron files, compose labels, systemd timers, scripts named like backup, import or sync), deploy documentation, variable names per service, git remote and current tag or commit, the README's first paragraph. It never reads `.env` and never records a value.

Show the user the inventory in ten lines and ask what is wrong before going on. The inventory decides which questions still need asking.

### Step 2: ask the ten questions, one at a time

The questions are in `references/questions.md`, in French and Portuguese, each with its reason and the fields it fills. Ask in the user's language, one question per message, and wait for the answer; never presume it. Shorten a question when the inventory already answers part of it ("I found a backup script scheduled at 19:00. Is that the backup you rely on, and when was it last restored?"). Write the answers to `answers.yml` as you go. An answer that contains a secret is not written: say where it belongs instead.

### Step 3: fill the templates

Map answers and inventory to fields with `references/fields.md`. Fill `templates/fr/*.md` first, then `templates/pt/*.md`. Repeated rows (features, tasks, symptoms) come from repeating the template line. Unknown field: the language's marker, never an empty cell, never a guess. Rows marked fixed in the templates stay as they are. Write each sentence as you would say it to the reader across a table. Strip the comments. Keep the footer.

### Step 4: check, in this order, fixing before moving on

- `scripts/secret_scanner.py <folder>`: fails on any token that looks like a password, key, credential URL or inline value (`references/secret-patterns.md`).
- `scripts/coverage_check.py inventory.json <folder>`: every variable name explained in document 5, every scheduled job present in document 3, every service mentioned in document 1 ("where it runs"), no `{{field}}` left unfilled, markers counted per document.
- Length: estimate words for documents 1, 4 and 6. Above the limit, cut: in document 4 drop the least frequent symptom; in document 6 never drop a checkbox, shorten the wording.
- Parity: when two languages were produced, the same number of headings in the same order in both, the fixed headings with the same meaning, and the same markers in both.
- Style: `scripts/style_check.py <folder>` for the mechanical part (long dashes, bold labels, curly quotes in Portuguese, the word lists, sentences over 35 words). Then read every document as its reader, with the checklist in `references/writing-style.md`: "what here sounds like a machine wrote it?" Fix those lines. Then: "would this person know what to do at 8 a.m. with people waiting?"

Write `verification.md`: what passed, what was fixed, what remains marked, which flagged words were kept on purpose.

### Step 5: hand back

Tell the user, in five lines: the folder; how many markers remain and where; the open points that went into document 6; and the three things only a human can do: deliver document 5 to its two recipients only, walk through one incident of document 4 with the successor without touching the system, collect the signatures of document 6.

## Updating an existing pack

When the folder already exists, regenerate into `<folder>-<date>/`, show the differences per document, and let the user merge. Never overwrite a document that was edited by hand since the last generation.

## Writing

The short version; `references/writing-style.md` has the word lists and the examples.

- You write for the organization's people, not for developers: "the program on the server", not "the backend".
- Sentences under 25 words. A short one after a long one. One idea per line in lists. Paragraphs of three sentences at most.
- Simple verbs: is, has, does, serves to. Never "constitutes", "represents", "ensures" when "is" or "does" says it.
- The same word for the same thing every time. The owner is "le propriétaire" / "o dono" in every document; the technical referent is "le référent technique" / "a referência técnica". Synonyms confuse a successor.
- Specifics: names, dates, numbers, screens, buttons. Not "the relevant equipment" but "the entrance camera, the one with the green light".
- Punctuation: commas, periods, colons, parentheses. No long dash. French quotes « » in French, straight quotes in Portuguese. No emoji, no bold inside lists, headings in sentence case.
- Register: French "vous", Portuguese "você". Document 3 procedures in the infinitive; document 4 in the imperative (Vérifiez, Verifique); document 6 in the first person without gendered forms. Dates as DD/MM/YYYY; times with the zone when server time and local time differ.
- Nothing a chatbot would say: no "hope this helps", no "feel free", no upbeat closing line, no "let's look at".

## Scripts (contracts; written after the templates are approved)

- `scripts/inventory.py <repo_path> [--out inventory.json]`: exit 0; prints a ten-line summary; reads names only; never opens `.env`.
- `scripts/secret_scanner.py <folder>`: exit 1 with file and line when a secret-like token, a credential URL or a compose inline value is found; exit 0 otherwise.
- `scripts/coverage_check.py <inventory.json> <folder>`: exit 1 when a name, job or service is unexplained or a `{{field}}` is unfilled; prints a table per document.
- `scripts/style_check.py <folder>`: exit 1 with file, line and rule number when it finds a long dash outside code blocks, a bold label at the start of a list item, curly quotes in a Portuguese file, an emoji or middle dot, a heading in Title Case, a word from the lists in `references/writing-style.md`, a rhetorical pair, or a sentence over 35 words; exit 0 otherwise. It flags; the agent decides and rewrites.

Python 3.10+, standard library (PyYAML optional, with a fallback). No network.

## References

- `references/questions.md`: the ten questions, FR and PT, with reason and fields.
- `references/fields.md`: field dictionary: key, meaning, source, documents.
- `references/plain-language.md`: jargon to plain language, FR and PT.
- `references/writing-style.md`: how to write like a person, with the word lists the checker uses.
- `references/successor-needs.md`: what a successor needs on day one, from real handovers.
- `references/secret-patterns.md`: what the scanner refuses.
- `templates/fr/`, `templates/pt/`: the six documents per language.

## Failure modes seen in real handovers

- A deploy README without the word "migrations": the successor cannot redeploy. Document 3 names every step, including the ones that run once a year.
- A licence or certificate that expires and nobody knew; the organization discovers it through a banner. Documents 1 and 5 carry every date with an owner.
- A handover written the day before leaving, obsolete a week later. Document 3 contains the yearly re-read; see "Updating an existing pack".
- Passwords in an envelope nobody can find. Document 5 names the place, the keeper and the deputy; never the password.
- A document 4 made of imagined incidents. Only incidents that happened or almost happened.
- Documents that read like a machine wrote them, so nobody reads them. Rule 10.
