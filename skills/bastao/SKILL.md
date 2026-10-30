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
3. Never invent. Anything the repository does not prove and the user did not answer is marked `[À CONFIRMER]` (FR) or `[A CONFIRMAR]` (PT). A marked gap beats a plausible sentence. Four fields keep the marker until the owner confirms them in person, whatever the repository suggests: `vault`, `last_restore_date`, `backup_offsite`, `backup_encrypted`. When the developer named the place, write the place followed by the marker ("le Bitwarden de l'école [À CONFIRMER]"), never the marker alone. A repository fact that describes a state and is more than 30 days old ("since 25/08 the gate recognises 46 students") is written with its date and asked again ("is this still true?"); unconfirmed, it carries the marker.
4. Plain language for non-technical readers: every technical term is translated the first time it appears (`references/plain-language.md`). Names, dates, numbers; no adjectives.
5. One page for documents 1, 4 and 6: aim for 380 words, never more than 400, as counted by `scripts/coverage_check.py` (the text a reader reads, without Markdown syntax). Document 4 has three symptoms, four at most, taken from incidents that happened or almost happened. A symptom enters document 4 only if it has a check without risk and a "fixed when"; an open investigation with no safe gesture is an open point in document 6.
6. When both languages are requested, the readers' main language first (ask in question 10; French when nobody says), then the other one, translated from the checked first version rather than written again; identical section structure. `templates/<lang>/` is the only source of structure; field keys are identical in both languages (`references/fields.md`).
7. Everything stays local; nothing is sent to any service. The user reviews before delivering. Document 5 goes only to its two recipients.
8. Template comments (`<!-- -->`) are instructions to you: follow them, then strip them from the delivered documents.
9. If the user types a secret in the conversation, do not write it anywhere; say where it belongs and continue.
10. Never write an example PIN, password or key, not even as a recommendation, a factory default or "for instance". Commands read user and database names from the container's own variables (`"$POSTGRES_USER"`), not from literal values.
11. Write like a person, not like a model. Every sentence you put in a document follows `references/writing-style.md`: short sentences, simple verbs, the same word for the same thing, no long dash, no bold labels, no inflated vocabulary, no rhetorical pairs or triads, no closing pep talk. Step 4 includes a style pass. A document that fails it is not finished.

## Workflow

### Step 1: inventory the repository

Run `python3 <skill>/scripts/inventory.py <repo_path> --out <folder>/inventory.json`. It writes `inventory.json`: project name (README title, compose project name), services and images, ports, volumes, scheduled jobs (cron files, compose labels, systemd timers, scripts named like backup, import or sync), deploy documentation, variable names per service, git remote, current tag or commit and the git authors (to confirm the developer's name), secret names found with a value in clear, the README's first paragraph. It never reads `.env` and never records a value: for an inline secret it keeps only a length and a hash, for the scanner.

Show the user the inventory in ten lines and ask what is wrong before going on. The inventory decides which questions still need asking. When the repository already holds handover or operation documents, read them too: they can answer part of the questions, with their source and their date.

### Step 2: ask the ten questions, one at a time

The questions are in `references/questions.md`, in French and Portuguese, each with its reason and the fields it fills. Ask in the user's language, one question per message, and wait for the answer; never presume it. Shorten a question when the inventory already answers part of it ("I found a backup script scheduled at 19:00. Is that the backup you rely on, and when was it last restored?"). Write the answers to `answers.yml` as you go, each with its source (the user, or a file and line). An answer that contains a secret is not written: say where it belongs instead.

Question 1 separates two people: the one handing over and the owner afterwards. If the user names themselves as owner, ask whether they stay in the organization after the handover; never write the leaving developer as owner without that confirmation.

After the ten, ask at most three follow-up questions on the gaps that block the most cells (usually: contacts of the people in document 2, who does the daily check, what to do if the system stops in the middle of the day). Then fill.

If the user says to fill the answers yourself, do it only from the repository and from what the user wrote earlier, with the source of each line; everything else stays marked. Say at the top of `verification.md` and in the hand-back that no answer came from the owner and that the pack is a draft, not a deliverable.

### Step 3: fill the templates

Map answers and inventory to fields with `references/fields.md`. Fill the templates of the first language (`templates/fr/` or `templates/pt/`), then translate into the second from the first version once step 4 passes on it. Repeated rows (features, tasks, symptoms) come from repeating the template line. Unknown field: the language's marker, never an empty cell, never a guess. A table row where every cell would be a marker becomes one sentence under the table instead ("À définir avec Marcia Okafor : ce que la bibliothécaire peut faire seule."), so the reader sees what is known. In document 3, a procedure of more than five steps goes to the commands section at the end, and the routine tables keep one line pointing to it. A rule that depends on a person available until a date ("never without the developer") carries that date. Rows marked fixed in the templates stay as they are; their wording may be shortened to fit the page, never their meaning. Write each sentence as you would say it to the reader across a table. Strip the comments. Keep the footer.

### Step 4: check, in this order, fixing before moving on

Run the scripts; never replace them with a check improvised in the session, and never report a number you estimated.

- `python3 <skill>/scripts/secret_scanner.py <folder> --inventory <folder>/inventory.json --repo <repo_path>`: fails on any token that looks like a password, key, credential URL, inline value or `.env` value (`references/secret-patterns.md`). A WARNING (a value equal to a service name) is checked by hand and noted in `verification.md`.
- `python3 <skill>/scripts/coverage_check.py <folder>/inventory.json <first_language_folder> --pair <second_language_folder>`: every variable name explained in document 5, every scheduled job in document 3, every service in document 1 ("where it runs"), every secret in clear as an open point in document 6, no `{{field}}` or comment left, documents 1, 4 and 6 within 400 words, 3 or 4 symptoms in document 4, and parity of headings, markers, checkboxes and table rows between the two languages. It prints words and markers per document. Above the limit, cut: in document 4 drop the least frequent symptom; in document 6 never drop a checkbox, shorten the wording.
- `python3 <skill>/scripts/style_check.py <folder>` for the mechanical part of the style. Then read every document as its reader, with the checklist in `references/writing-style.md`: "what here sounds like a machine wrote it?" Fix those lines. Then: "would this person know what to do at 8 a.m. with people waiting?"

Write `verification.md`: what passed, what was fixed, the script outputs (word and marker counts copied from `coverage_check.py`), what remains marked, which flagged words were kept on purpose, and a section "Contradictions found" with both sides cited (file and line, or the user's answer). Each contradiction is also an open point in document 6.

### Step 5: hand back

Tell the user, in five lines: the full path of every file written; how many markers remain and where; the open points that went into document 6; and the three things only a human can do: deliver document 5 to its two recipients only, walk through one incident of document 4 with the successor without touching the system, collect the signatures of document 6.

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

## Scripts

Run them with Python 3.10+, standard library only (PyYAML is used when present). No network. Tests: `python3 -m unittest discover -s <skill>/tests`, on the fictional repository in `tests/fixtures/estante`.

- `scripts/inventory.py <repo_path> [--out inventory.json]`: exit 0; prints a ten-line summary; reads names only; never opens `.env`.
- `scripts/secret_scanner.py <folder> [--inventory inventory.json] [--repo <repo_path>]`: exit 1 with file and line when a secret-like token, a credential URL or a compose inline value is found; exit 0 otherwise.
- `scripts/coverage_check.py <inventory.json> <folder> [--pair <folder>]`: exit 1 when a name, job, service or secret in clear is not covered, a `{{field}}` is unfilled, a one-page document is over 400 words, document 4 does not have 3 or 4 symptoms, or the two languages differ in shape; prints a table per document.
- `scripts/style_check.py <folder>`: exit 1 with file, line and rule number when it finds a long dash outside code blocks, a bold label at the start of a list item, curly quotes in a Portuguese file, an emoji or middle dot, a heading in Title Case, a word from the lists in `references/writing-style.md`, a rhetorical pair, or a sentence over 35 words; exit 0 otherwise. It flags; the agent decides and rewrites.

`tests/cases/estante/` holds a full simulated run (the facts known by the developer, the questions asked, the answers given) to repeat a test without a real person.

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
- Documents that read like a machine wrote them, so nobody reads them. Rule 11.
