---
name: bastao
description: Writes and keeps up to date the handover pack (dossier de passation, pasta de passagem) for a system being handed to a non-technical organization, in French and Portuguese. Six documents, what it is and what it does not do, who does what, routines, what to do if it breaks, access custody without secrets, reception checklist, written first from what the repository proves, gaps marked, questions left in a file the developer answers when they can. Use when the user mentions passagem, passation, handover to a client or school, final delivery, successor, "who stays responsible", leaving a project, documentation for the IT team that will keep the system, or when hook feedback starting with "Bastão hook:" asks to update the pack. Not for agent-to-agent session handoffs.
---

# Bastão

Bastão writes the folder a non-technical organization needs to keep a system running after its developer leaves: six Markdown documents, in French and/or Brazilian Portuguese, written the way a careful person writes, with no secret inside. It writes first, from the repository, and asks last: what the repository does not prove is marked, and the questions wait in a file the developer answers when they have time. Nobody has to ask for anything twice.

Two people, never confused. The user is the developer who runs the skill and hands the system over; the user answers the questions file and passes to the owner what only the owner knows. The owner ("le propriétaire", "o dono") is the person who keeps the system afterwards.

## When to use it, and when not

Use it when the user is delivering a running system to the people who will keep it (a school, an association, a small business), is leaving a project, needs documentation for the IT person who inherits a system, or when hook feedback starting with "Bastão hook:" asks you to bring the pack up to date.

Do not use it for passing a session from one agent to another (that is a handoff, not a handover), for developer onboarding (point to the README or a code tour skill), for an incident in progress (if the pack exists, open its document 4; otherwise help directly), or for a system not yet in production (the pack describes what runs, not plans).

## How it runs

- First run. The user calls the skill, or asks for the handover of the repository in their own words. You inventory the repository, write the six documents in one language from what it proves (the second language comes with question 10), mark every gap, write the questions file, check, and hand back. You ask in the chat only in the two cases of rule 12, and usually never.
- Later run. The user calls the skill again, or says "update the handover". You read the new answers in the questions file, inventory again, update only what changed, and hand back in three lines.
- Hook run. Feedback starting with "Bastão hook:" comes from a hook at the end of a turn (the Claude Code `Stop` event): a file the pack depends on, or the questions file, is newer than the last run. The hook stays silent until a pack exists, so the first run always comes from the user. The plugin ships the hook (`hooks/hooks.json` and `scripts/stop_hook.py`); without the plugin, a user can add it by hand from the contract in `references/pack-files.md`. You behave as in a later run, never ask in the chat, and keep the languages of the pack unless a new answer to question 10 changes them. Nothing changed: one line.

Never open a conversation of questions. The questions file replaces the interview.

## What you produce

A folder named by the user (default `passation/` for French, `passagem/` for Portuguese), containing:

| Nº | File (FR) | File (PT) | Size |
|---|---|---|---|
| 0 | 00-questions.md | 00-perguntas.md | free; the user writes in it |
| 1 | 01-ce-que-cest.md | 01-o-que-e.md | one page |
| 2 | 02-qui-fait-quoi.md | 02-quem-faz-o-que.md | two pages at most |
| 3 | 03-routine.md | 03-rotina.md | free |
| 4 | 04-si-ca-casse.md | 04-se-quebrar.md | one page |
| 5 | 05-garde-des-acces.md | 05-custodia-de-acessos.md | free; restricted distribution |
| 6 | 06-checklist-reception.md | 06-checklist-de-recepcao.md | one page; a part for the owner, a part for the technical referent |

Plus `answers.yml` (the answers, with who gave them and their source, no secrets), `inventory.json` (what the repository revealed, names only, with the commit it was taken from) and `verification.md` (the checks, the fingerprint of each document, the history of runs). `references/pack-files.md` gives the format of each file, where each one lives when the pack has two languages, and what counts as a change. PDF export is optional, through the host's document skill, once the Markdown is approved.

The language of the pack: the one the user writes in, when it is French or Portuguese; otherwise the language of the README, when it is one of the two; otherwise French. The questions file is in that language. Question 10 asks for the readers and their languages; its answer can add the second language or change which one comes first, on the run that reads it, a hook run included (`references/pack-files.md` says what moves). With two languages, the readers' main language is written first and the other one is translated from the checked first version, with identical structure.

## Rules that never bend

1. Never read, store or print a secret value. Read variable names from `.env.example`, `docker-compose*.yml`, systemd units and scripts; never open `.env`; never reproduce a value found inline in a compose file or a script when its variable name suggests a secret. A value that is not secret (a host name, a port, a schedule) may be written where a document needs it; when unsure, treat it as a secret. A value found in clear in the repository becomes an open point in document 6 ("password written without protection in the code: NAME", followed by what it is in plain words, since document 6 holds no technical term).
2. No address with credentials (`user:password@host`, token in a URL), no command with a password as argument or environment variable. When a procedure needs a secret, write "(the password is in {{vault}})" in the document's language.
3. Never invent. Anything the repository does not prove and nobody answered is marked `[À CONFIRMER]` (FR) or `[A CONFIRMAR]` (PT). A marked gap beats a plausible sentence. Four fields keep the marker until the owner confirms them in person, whatever the repository suggests: `vault`, `last_restore_date`, `backup_offsite`, `backup_encrypted`. When a place or a name is known, write it followed by the marker ("le Bitwarden de l'école [À CONFIRMER]"), never the marker alone. A repository fact that describes a state and is more than 30 days old ("since 25/08 the gate recognises 46 students") is written with its date and goes to the questions file ("is this still true?"); unconfirmed, it carries the marker. The git author with the most commits is only a candidate for the developer who hands over: write the name followed by the marker until question 10 confirms it. With several human authors, or a bot or company account, write the marker alone and list the candidates under question 10. An answer says what it says. Do not widen it (a person who "decides the changes" decides what the answers list, not renewals or stopping the system), do not drop its hedge ("acho que", "je crois" keeps its marker), do not turn "I do not know" into "does not exist" or "was never agreed", do not take what a question supposed for an answer (a question that assumed the address belongs to the printer is not the developer saying so), and do not give anyone a decision, a role or an answer that no source gives. A sentence that carries one of the four fields above carries the marker, in every document where it appears.
4. Plain language for non-technical readers: every technical term is translated the first time it appears in each document (`references/plain-language.md`), and documents 1, 4 and 6 hold no technical term at all (rule 31 of `references/writing-style.md`; the checker flags them). A product name stays with what it does ("Bitwarden, le programme où les mots de passe sont gardés"). Names, dates, numbers; no adjectives.
5. One page for documents 1, 4 and 6: aim for 380 words, never more than 400 (document 6, which holds two parts and the signatures: 450), as counted by `scripts/coverage_check.py` (the text a reader reads, without Markdown syntax). Document 4 holds only symptoms that happened or almost happened, each with a check without risk and a "fixed when" that come from the incident's recorded cause and fix (an incident file, a runbook, an answer). If the cause was "the card was not paid", the check is whether it is paid now and the "fixed when" is the symptom gone after the recorded fix; nothing else is added, and a check that only restates the symptom ("does the printer print?") is not a check. Never say what usually happens: an incident recorded once gives "last time the cause was X", not "most of the time". A commit message or an issue gives a symptom and its date, not its cause or fix: that symptom stays a line under the open question about incidents. A symptom that stops everybody (the system down) is never the one dropped to fit the page: drop the one that stops the fewest people. A recorded symptom left out, for length or for lack of a check, is named in the line "Autres symptômes" below, or, when the page is full, in the open question that the line points to; that line is then required even when the pack has three symptoms. A finished pack has three symptoms, four at most. While fewer are known, write the ones you have and, under the last one, the line "Autres symptômes : question N de 00-questions.md." / "Outros sintomas: pergunta N de 00-perguntas.md.", N being the number of the open question that holds them (5 on the first run), with the name of the pack's own questions file; in the second language, add its folder and its language ("pergunta 5 de passation/00-questions.md, em francês"). The pack is then a draft, and `coverage_check.py` says so with a warning. An open investigation with no safe gesture is an open point in document 6.
6. `templates/<lang>/` is the only source of structure; field keys are identical in both languages (`references/fields.md`). Between two languages, headings, markers, checkboxes and table rows match one to one.
7. Everything stays local; nothing is sent to any service. The user reviews before delivering. Document 5 goes only to its two recipients. When an answer places a document where this rule forbids it (document 5 in a folder four people read), keep what was said, add an open point in document 6 and an entry under "Contradictions found", and name it in the hand-back.
8. Template comments (`<!-- -->`) are instructions to you: follow them, then strip them from the delivered documents.
9. A secret typed in the chat or written in the questions file is never copied anywhere. In the questions file, replace the value and write under it the line given in `references/pack-files.md`; in the hand-back, say where the secret belongs. A scanner finding in the questions file that is not a secret stays as written and is noted in `verification.md`.
10. Never write an example PIN, password or key, not even as a recommendation, a factory default or "for instance". Commands read user and database names from the container's own variables (`"$POSTGRES_USER"`), not from literal values.
11. Write like a person, for a reader in a hurry. Every sentence you put in a document follows `references/writing-style.md`: its checklist against machine writing, and its rules adapted from the ASD-STE100 standard (Simplified Technical English) to French and Portuguese: twenty words per sentence in procedures, twenty-five elsewhere, three sentences per paragraph, one instruction per sentence, the same word for the same thing. The skill claims no conformance to that standard and no approval by ASD. A document that fails the style pass is not finished.
12. Ask in the chat only when a whole document is blocked, never for a cell, and only in two cases: two sources contradict each other on something that goes into document 4 or 5 and the pack cannot say which is true; or no symptom of document 4 can be written. Write the whole pack first, then ask in the hand-back, one question per blocked document. On a hook run, never ask: the question goes to the top of the questions file, under "Urgent" / "Urgente", and the hand-back names it.

## Workflow

### Step 1: inventory the repository

Run `python3 <skill>/scripts/inventory.py <repo_path> --out <folder>/inventory.json`. It writes `inventory.json`: project name (README title, compose project name), services and images, ports, volumes, scheduled jobs (cron files, systemd timers, `@Scheduled` methods), scripts named like backup, import or sync, deploy documentation, variable names per service, git remote, current tag or commit and the git authors, secret names found with a value in clear, the README's first paragraph. It never reads `.env` and never records a value: for an inline secret it keeps only a length and a hash, for the scanner. It skips the pack's own files, by their names, wherever they are; repeat `--skip <folder>` for any other folder to leave out, such as an old handover kept in the repository.

Do not show the inventory and do not ask what is wrong. Read the repository's own documents as well: a README, a runbook, an operations or incident file, an existing handover. Each fact you take from them keeps its source (file and line) and its date. Incidents come from incident files, runbooks, commit messages and issues that name a failure that happened; from nothing else. Rule 5 says what each source can prove.

### Step 2: fill the templates from the repository

Map the inventory and the documents you read to fields with `references/fields.md`. Fill the templates of the first language (`templates/fr/` or `templates/pt/`). Repeated rows (features, tasks, symptoms) come from repeating the template line. Unknown field: the language's marker, never an empty cell, never a guess. A table row where every cell would be a marker becomes one sentence under the table instead ("À définir avec Marcia Okafor : ce que la bibliothécaire peut faire seule."), so the reader sees what is known. Where an open point leaves no procedure (restoring a backup, say), the document gives the first safe gesture instead of a pointer to a procedure that does not exist: do nothing irreversible, make a fresh copy, write to the named person. In document 3, a procedure of more than five steps goes to the commands section at the end, and the routine tables keep one line pointing to it. A rule that depends on a person available until a date ("never without the developer") carries that date. Rows marked fixed in the templates stay as they are; their wording may be shortened to fit the page, never their meaning, and a fixed row that an answer limits takes the limit (the developer only answers questions: the row says so; only the developer may restore a backup: the install row says so). A field filled on reception day (origin "recepção" in `references/fields.md`) becomes a blank line, `________`, for the person who signs. Before you keep a step or a command, check it against the open points of documents 2, 5 and 6: a step that needs what they say is missing (a git remote for `git pull`, an account, a restore procedure) is written with the gap named, never as a command that works; every command block starts with the folder it runs in and names the account. Write each sentence as you would say it to the reader across a table. Strip the comments. Keep the footer.

The owner comes only from the answer to question 1; until then the owner is a marker. When the repository contradicts what an answer says (the developer says the reminders work, the code does nothing), both sides appear where the claim is written, in document 1 for example, and again in document 6. The developer who hands over follows rule 3.

### Step 3: write the questions file

Write `00-questions.md` (FR) or `00-perguntas.md` (PT) in the language and the folder of the first language. It replaces the interview; `references/pack-files.md` gives its sections and an example. In short: an opening in plain words; the ten questions of `references/questions.md`, the one that fills the most cells first, each keeping its number, each with what the repository already showed and what it is for, in plain words; three follow-up questions at most; a block for the questions that only the owner or the technical referent can answer; the answered questions, with their date. A question the repository fully answered stays, in one line, as a confirmation. A new question takes a new number, from 11, and goes to "Perguntas", never to the follow-up block; a question stands in one block only. A question asks one thing, two at most.

On a later run, read the answer lines first. Each answer goes to `answers.yml` (format in `references/pack-files.md`), fills its fields, and its question moves to "Répondu" / "Respondidas"; what an answer leaves open becomes a new question, and "I do not know" or "nobody decided" fills nothing and sends the question, reworded, to the block for the owner or the referent. An answer that holds a secret: rule 9. An answer that contradicts the repository is written with both sides in `verification.md` and becomes an open point in document 6; if it concerns document 4 or 5, that is the first case of rule 12.

### Step 4: check, in silence

Run the scripts; never replace them with a check improvised in the session, and never report a number you estimated. Report only what fails. A check that passes is one line in `verification.md`, not a paragraph in the chat.

- `python3 <skill>/scripts/secret_scanner.py <folder> --inventory <folder>/inventory.json --repo <repo_path>`: fails on any token that looks like a password, key, credential URL, inline value or `.env` value (`references/secret-patterns.md`), in every file of the folder: the six documents, the questions file, `answers.yml`, `verification.md` and any proposal. Run it on each language folder; the second one is named on the "Second folder" line of `verification.md`. A WARNING (a value equal to a service name) is checked by hand and noted in `verification.md`.
- `python3 <skill>/scripts/coverage_check.py <folder>/inventory.json <first_language_folder> --pair <second_language_folder>`: every variable name explained in document 5, every scheduled job in document 3, every service in document 1 ("where it runs"), every secret in clear as an open point in document 6, no `{{field}}` or comment left, documents 1 and 4 within 400 words and document 6 within 450, 3 or 4 symptoms in document 4 (fewer, with the line of rule 5, is a warning: the pack is a draft), and parity of headings, markers, checkboxes and table rows between the two languages. Above the limit, cut: in document 4 drop the symptom that stops the fewest people (rule 5); in document 6 never drop a checkbox, shorten the wording. While a proposal is pending (see "Updating an existing pack"), add `--merged`: the check is made on the pack as it will be once the user has merged, and that is the result to record.
- `python3 <skill>/scripts/style_check.py <folder>`, on each language folder, for the mechanical part of the style, including the sentence and paragraph limits of rules 21 and 22 of `references/writing-style.md`. It reads proposals as well as documents. Then, for each of the four fields of rule 3, find every sentence of every document that carries it (the vault, the last restore, the copy outside the machine, the encryption), including the table of open points of document 6, and check that the marker is in the sentence itself, not only in a neighbouring column. Then read every document as its reader, with the checklist in `references/writing-style.md`: "what here sounds like a machine wrote it?" Fix those lines. Then: "would this person know what to do at 8 a.m. with people waiting?" A flag in a section this run did not change, in a pack written before the current rules, or in a document edited by hand goes under "Still to rewrite" in `verification.md`. You rewrite it the next time that section changes, or when the user asks for a full re-read; in a document edited by hand, only when the user agrees.

Write `verification.md` with the sections listed in `references/pack-files.md`, from the run line to the history.

### Step 5: hand back

First run, five lines: the full path of the folder; how many markers remain and in which documents; that the questions wait in `00-questions.md` or `00-perguntas.md`, to be answered when the developer has time, and that the pack is a draft until then; the open points that went into document 6; and the three things only a human can do: deliver document 5 to its two recipients only, walk through one incident of document 4 with the successor without touching the system, collect the signatures of document 6. When rule 12 applies, its question comes after these five lines.

Later run, a few short lines: what changed; the proposals to merge, by file name; how many markers and "Still to rewrite" flags remain; what still waits in the questions file; one line for each new risk you found that is not a case of rule 12. Nothing changed: one line.

## Updating an existing pack

A pack exists when a folder holds `inventory.json` and `verification.md`; `references/pack-files.md` says where to look. Then:

1. Read the new answers in the questions file (step 3).
2. Run the inventory again into `<folder>/inventory.new.json` and compare it with `inventory.json`, without their `git` blocks. Equal: delete the new file and keep `inventory.json`. Different: replace `inventory.json` with the new one. List the files of the successor list changed since the commit recorded in the old file: `git diff --name-only <recorded commit>`, which covers tracked files in the working tree, and `git status --short` for new files. `references/pack-files.md` defines the successor list and what counts as a change; a new commit alone is not one.
3. If nothing brings a change, rewrite the first lines of `verification.md` (date and commit of this run) and stop.
4. Otherwise update only the sections that depend on what changed, in place, then run step 4 on the whole pack. A new service, job or variable appears in its document with the date; a removed one is removed, and the removal is noted in `verification.md`. A document you change takes the date of this run in its header.
5. Before touching a document, compare its SHA-256 with "Fingerprints" in `verification.md`. `references/pack-files.md` says when a document edited by hand becomes the new baseline, and when your version goes beside it as `proposition-<name>.md` (FR) or `proposta-<name>.md` (PT); when one language gets a proposal, the other language gets one too, so the pair stays coherent until the user merges. Run the checks with `--merged` while a proposal is pending.

The yearly re-read in document 3 stays: the hook keeps the pack current, it does not replace a person reading it once a year.

## Writing

The short version; `references/writing-style.md` has the rules, the approved words, the word lists and the examples.

- You write for the organization's people, not for developers: "the program on the machine", not "the backend".
- Twenty words per sentence in documents 3 and 4; twenty-five elsewhere; a procedure in another document keeps to twenty. A short sentence after a long one.
- Paragraphs of three sentences at most; in documents 3 and 4, a list item that holds a short procedure, six. One idea per line in lists.
- One instruction per sentence in procedures. Two actions, two sentences. A warning comes before the step it protects and starts with the command.
- Simple verbs: is, has, does, serves to. Never "constitutes", "represents", "ensures" when "is" or "does" says it.
- The same word for the same thing every time, from the approved words in `references/writing-style.md`. The owner is "le propriétaire" / "o dono" in every document; the technical referent is "le référent technique" / "a referência técnica". Synonyms confuse a successor.
- Specifics: names, dates, numbers, screens, buttons. Not "the relevant equipment" but "the entrance camera, the one with the green light".
- Punctuation: commas, periods, colons, parentheses. No long dash. French quotes « » in French, straight quotes in Portuguese. No emoji, no bold inside lists, headings in sentence case.
- Register: French "vous", Portuguese "você". Document 3 procedures in the infinitive; document 4 in the imperative (Vérifiez, Verifique); document 6 in the first person of whoever ticks the box, without gendered forms. Dates as DD/MM/YYYY; times with the zone when server time and local time differ.
- Nothing a chatbot would say: no "hope this helps", no "feel free", no upbeat closing line, no "let's look at".

## Scripts

Run them with Python 3.10+, standard library only (PyYAML is used when present). No network. Give every folder and file as an absolute path. Tests: `python3 -m unittest discover -s <skill>/tests`, on the fictional repository in `tests/fixtures/estante`.

- `scripts/inventory.py <repo_path> [--out inventory.json] [--skip <folder>]...`: exit 0; prints a ten-line summary; reads names only; never opens `.env`; skips the pack's own files by their names and every `--skip` folder (repeat the option for each).
- `scripts/secret_scanner.py <folder> [--inventory inventory.json] [--repo <repo_path>]`: exit 1 with file and line when a secret-like token, a credential URL or a compose inline value is found in any `.md`, `.yml`, `.yaml` or `.json` of the folder except `inventory.json`; exit 0 otherwise.
- `scripts/coverage_check.py <inventory.json> <folder> [--pair <folder>] [--merged]`: exit 1 when a name, job, service or secret in clear is not covered, a `{{field}}` is unfilled, a one-page document is over its limit (400 words; 450 for document 6), document 4 has more than 4 symptoms, fewer than 3 without the line of rule 5, or a line that names a questions file not in the pack, or the two languages differ in shape; prints a table per document and the warnings. With `--merged` a proposal stands in for the document it sits beside.
- `scripts/style_check.py <folder> [--lang fr|pt] [--max-words N] [--max-sentences N]`: exit 1 with file, line and rule number when it finds a long dash outside code blocks, a bold label at the start of a list item, curly quotes in a Portuguese file, an emoji or middle dot, a heading in Title Case, a word from the lists in `references/writing-style.md`, a technical term of the jargon lists in documents 1, 4 and 6 (rule 31), a rhetorical pair, a sentence over the limit (20 words in documents 3 and 4, 25 in the others), a paragraph, list item or table cell of more than three sentences (six for a list item or table cell in documents 3 and 4); exit 0 otherwise. It reads a sentence across the lines of its paragraph or list item and counts a URL, an e-mail address or a `{{field}}` as one word. It checks documents 01 to 06 and the proposals, never the questions file. It flags; the agent decides and rewrites.

- `scripts/stop_hook.py`: the end-of-turn hook (Claude Code `Stop` event). Reads the hook input on stdin, prints a "Bastão hook:" line when a file of the successor list or the questions file is newer than `verification.md`, nothing otherwise; always exit 0; file times only. You do not run it; the plugin does.

`tests/cases/estante/` holds the facts a developer knows and the round 3 interview, kept as history; `tests/README.md` says how to repeat a test in passive mode.

## References

- `references/questions.md`: the ten questions, FR and PT, with reason and fields.
- `references/pack-files.md`: where the files of a pack live; the questions file, `answers.yml` and `verification.md`; fingerprints and hand edits; what counts as a change; the hook contract.
- `references/fields.md`: field dictionary: key, meaning, source, documents.
- `references/plain-language.md`: jargon to plain language, FR and PT.
- `references/writing-style.md`: how to write like a person, the rules adapted from ASD-STE100, the approved words, the word lists the checker uses.
- `references/successor-needs.md`: what a successor needs on day one, from real handovers.
- `references/secret-patterns.md`: what the scanner refuses.
- `templates/fr/`, `templates/pt/`: the six documents per language.

## Failure modes seen in real handovers

- A deploy README without the word "migrations": the successor cannot redeploy. Document 3 names every step, including the ones that run once a year.
- A licence or certificate that expires and nobody knew; the organization discovers it through a banner. Documents 1 and 5 carry every date with an owner.
- A handover written the day before leaving, obsolete a week later. The hook and the yearly re-read in document 3 exist for that.
- Passwords in an envelope nobody can find. Document 5 names the place, the keeper and the deputy; never the password.
- A document 4 made of imagined incidents. Only incidents that happened or almost happened.
- Documents that read like a machine wrote them, so nobody reads them. Rule 11.
- A skill that asks ten questions before writing a line, so the developer never runs it. Write first, ask in a file, interrupt only when a document is blocked. Rule 12.
