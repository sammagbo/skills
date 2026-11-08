# The files of a pack

What the skill writes besides the six documents, where each file lives, and the contract of the hook. SKILL.md says when to write them; this file says how they look.

## Where they live

One language: everything in one folder at the repository root, named by the user, by default `passation/` (French) or `passagem/` (Portuguese).

Two languages: the folder of the first language holds its six documents, the questions file, `answers.yml`, `inventory.json` and `verification.md`. The second language is a sibling folder with its six documents only (by default `passagem/` beside `passation/`, or the reverse). The line "Second folder" of `verification.md` names it. There is one questions file, in the first language. When an answer to question 10 changes which language comes first, the questions file (translated, with its answers), `answers.yml`, `inventory.json` and `verification.md` move to the folder of the new first language, and "History" notes the move.

A pack exists when a folder holds both `inventory.json` and `verification.md`. A later run looks in the folder the user names; otherwise in `passation/` and `passagem/`; otherwise in every first-level folder of the repository. The pack is never inventoried: `inventory.py` skips the six documents of each language, the questions file and the proposals wherever they are, by their names, and `answers.yml`, `verification.md` and `inventory*.json` in the folder of `--out`.

## The questions file

`00-questions.md` (French) or `00-perguntas.md` (Portuguese). Its sections, in this order:

1. A title, then four lines on how to answer: write after "Réponse :" / "Resposta:", in any order, at any time; never a password, a key or a PIN, only the place where it is kept; pass to the owner what only the owner knows; save the file, and the next run does the rest.
2. "Urgent" / "Urgente", only when a hook run met one of the two cases of rule 12. Leave the heading out when it is empty.
3. "Questions" / "Perguntas": the open questions, the one that fills the most cells first. Each keeps the number it has in `references/questions.md`, so "Question 7" can come first.
4. "Si vous avez cinq minutes de plus" / "Se tiver cinco minutos a mais": three follow-up questions at most, numbered C1 to C3.
5. "Répondu" / "Respondidas": the answered questions, with their date, moved here by the skill. Questions 2 and 7, which hold the four fields of rule 3, keep under their answer an empty line "Confirmé par le propriétaire :" / "Confirmado pelo dono:" until the user writes there the owner's name and the date. The user can also write "Correction :" / "Correção:" under any answered question, with the new answer.

One question, in Portuguese:

```markdown
### Pergunta 7

Existe backup? Onde, com que frequência, e quando foi a última restauração provada?

O repositório mostra: `deploy/backup.sh`, agendado às 02:30 em `deploy/crontab` (linha 3). Nada sobre restauração.
Libera: documentos 3, 5 e 6.

Resposta:
```

A question the repository fully answered stays, in one line, as a confirmation: "Le dépôt dit : sauvegarde à 02:30 par `deploy/backup.sh`. C'est bien celle-là ?" / "O repositório diz: backup às 02:30 por `deploy/backup.sh`. É esse mesmo?".

An answer that holds a secret: replace the value with "(retiré)" / "(removido)" and write under it "Réponse retirée le DD/MM/YYYY : elle contenait un mot de passe. Écrivez seulement l'endroit où il est gardé." / "Resposta removida em DD/MM/YYYY: continha uma senha. Escreva só o lugar onde ela fica guardada.".

## answers.yml

One entry per answered question, under its number. A later run adds entries. It changes an existing entry only for a line the user wrote under that question in "Répondu" / "Respondidas": "Confirmé par le propriétaire" / "Confirmado pelo dono" sets `confirmed_by`; "Correction" / "Correção" moves the old answer to `previous` and writes the new one. "History" notes each change. A value never holds a secret.

```yaml
q7:
  answer: "Backup toda noite no NAS da secretaria. Restauração testada em 12/09/2026 por Denise Prado."
  answered_by: user
  confirmed_by: ""
  source: "00-perguntas.md, pergunta 7"
  date: "08/11/2026"
  fields:
    backup_location: "NAS da secretaria"
    backup_frequency: "toda noite"
    last_restore_by: "Denise Prado"
```

`answered_by` is `user`, or `owner` when the user writes that the owner gave the answer. `confirmed_by` holds the owner's name and the date only when the user writes that the owner confirmed in person; the four fields of rule 3 (`vault`, `last_restore_date`, `backup_offsite`, `backup_encrypted`) keep their marker until it does. In the example, `last_restore_date` stays marked.

## verification.md

Fixed sections, in this order. Each run that changes the pack rewrites them all except "History", which it extends. A run that changes nothing rewrites only the first lines and adds nothing to "History".

1. The first lines: "Run: DD/MM/YYYY, commit <short>"; "Status: draft" or "Status: ready for review"; "Second folder: <path>" when there are two languages. These lines change on every run, even one that changes nothing else: the hook compares file times with this file.
2. "Checks": one line per script and its result; the word and marker counts copied from `coverage_check.py`.
3. "Fixed": what this run corrected.
4. "Still marked": the markers left, per document.
5. "Still to rewrite": style or coverage flags that this run did not fix: in sections it did not change, in a pack written before the current rules, or in a document edited by hand (marked "hand edit"). The hand-back counts them.
6. "Words kept on purpose": flagged words that are the right word in context.
7. "Words chosen": words picked for things that no list covers (rule 26 of `references/writing-style.md`).
8. "Contradictions found": both sides, each with its source (file and line, or question and date).
9. "Fingerprints": a table `| File | SHA-256 |`, one row per document 1 to 6 in each language, the `sha256sum` of the file as you leave it.
10. "History": a heading per run, `### DD/MM/YYYY, commit <short>`, then three lines: what changed in the repository, what was answered, which documents moved.

## Fingerprints and hand edits

Before touching a document, compute its SHA-256 and compare it with "Fingerprints".

- Same hash: the document is yours to update.
- Different hash, and nothing that feeds this document changed: someone edited it by hand. Their version is the new baseline. Record its hash and leave it, even when a check flags it: the flags go under "Still to rewrite", marked "hand edit", and wait for the user.
- Different hash, and something that feeds it changed: do not overwrite it. Write your version beside it as `proposition-<name>.md` (French) or `proposta-<name>.md` (Portuguese), record both hashes, and name it in the hand-back. The user merges. `style_check.py` and `coverage_check.py` skip these files; `secret_scanner.py` reads them. When a later run finds the proposal gone, the document as it stands is the baseline.

A document you change takes the date of the run in its header (`{{doc_date}}`).

## What counts as a change

- A new answer in the questions file.
- In the inventory, without its `git` block: a service, a scheduled job, a variable name, a secret in clear or a deploy document that appeared or disappeared.
- A file of the successor list changed since the recorded commit, in a commit or in the working tree.

The successor list: compose and container files (`docker-compose*.yml`, `compose*.yml`, `Dockerfile*`), cron and systemd files, `.env.example` and its variants, deploy, operations, incident and runbook documents, scripts named like backup, import, sync, restore or migrate, Java or Kotlin files with `@Scheduled`, `application*.properties`, and the README.

A new commit is not a change by itself: it only serves to list the changed files (`git diff --name-only <recorded commit>`). The version in document 6 moves only when the user says a version was installed.

## Hook contract

For the plugin that will ship the hook (version 0.2), and for a user who adds it by hand until then. The host is Claude Code.

- Event: `Stop`, which runs each time Claude finishes a turn. A `SessionEnd` hook cannot ask Claude for anything: Claude Code discards its output.
- Handler: a command hook, never a prompt hook, which cannot look at the repository. In the plugin, `hooks/hooks.json` declares it with the plugin's own path: `{"hooks": {"Stop": [{"hooks": [{"type": "command", "command": "\"${CLAUDE_PLUGIN_ROOT}\"/scripts/stop_hook.py", "timeout": 30}]}]}}`. `Stop` takes no matcher. Without the plugin, the same object goes in `.claude/settings.json` (the project) or `~/.claude/settings.json` (every project), with an absolute path or `${CLAUDE_PROJECT_DIR}`, because `${CLAUDE_PLUGIN_ROOT}` exists only for a plugin.
- The script reads the hook input, a JSON object, on stdin, and always exits 0; never 2. It prints nothing when `stop_hook_active` is true, when no pack is found from `cwd` (see "Where they live"), or when no file of the successor list and not the questions file is newer than `verification.md`. It stays fast: file times only, no model, no network.
- Otherwise it prints one JSON object: `{"hookSpecificOutput": {"hookEventName": "Stop", "additionalContext": "Bastão hook: repository <repo>, pack <folder>. Update the pack if something it describes changed."}}`. Claude then goes on with that text as hook feedback. Claude Code also accepts `{"decision": "block", "reason": "..."}`, but shows it to the user as a hook error.
- Do not count on the cap of eight continuations in a row that Claude Code puts on `Stop` hooks: it starts again each time Claude uses a tool. What keeps the hook quiet is `stop_hook_active` and the time of `verification.md`.
- The skill recognises a hook run by the prefix "Bastão hook:". On a hook run it never asks in the chat, keeps the languages of the pack unless a new answer to question 10 changes them, says one line when nothing changed, and always rewrites the first lines of `verification.md`, so the hook stays quiet until a file changes again.
