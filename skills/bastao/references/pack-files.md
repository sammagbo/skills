# The files of a pack

What the skill writes besides the six documents, where each file lives, and the contract of the hook. SKILL.md says when to write them; this file says how they look.

## Where they live

One language: everything in one folder at the repository root, named by the user, by default `passation/` (French) or `passagem/` (Portuguese).

Two languages: the folder of the first language holds its six documents, the questions file, `answers.yml`, `inventory.json` and `verification.md`. The second language is a sibling folder with its six documents only (by default `passagem/` beside `passation/`, or the reverse). The line "Second folder" of `verification.md` names it. There is one questions file, in the first language. When an answer to question 10 changes which language comes first, the questions file (translated, with its answers), `answers.yml`, `inventory.json` and `verification.md` move to the folder of the new first language, and "History" notes the move.

A pack exists when a folder holds both `inventory.json` and `verification.md`. A later run looks in the folder the user names; otherwise in `passation/` and `passagem/`; otherwise in every first-level folder of the repository. The pack is never inventoried: `inventory.py` skips the six documents of each language, the questions file and the proposals wherever they are, by their names, and `answers.yml`, `verification.md` and `inventory*.json` in the folder of `--out`.

## The questions file

`00-questions.md` (French) or `00-perguntas.md` (Portuguese). It is written for the developer, who is not a technician of the pack: plain words, no file name or line number inside a question, no "documents 2, 3 and 6". Its sections, in this order:

1. A title, then a short opening in plain words: the answers fill the handover folder; write after "Réponse :" / "Resposta:"; any order, any time; "je ne sais pas" / "não sei" is a good answer; never a password, a key or a PIN, only the place where it is kept; save the file, and the agent uses the answers the next time it works on the folder. The opening also says that the last block is not for the developer: he forwards it, and under each question of that block it names who should answer (the owner or the technical referent, by name when the answers give one).
2. "Urgent" / "Urgente", only when a hook run met one of the two cases of rule 12. Leave the heading out when it is empty.
3. "Questions" / "Perguntas": the open questions for the developer, the one that fills the most cells first. Each question has its number, the question (one thing, two at most; a question of `references/questions.md` that asks more is split in two parts, 1a and 1b, which keep the number 1), "Ce que je sais déjà" / "O que já sei" (what the repository showed, in plain words and with no technical term unless the developer used it himself, the file named at the end in parentheses, no line number), "Cela sert à" / "Serve para" (what it unlocks, in words a school secretary uses: "what to do if it breaks", "who does what"), and the empty answer line.
4. "Si vous avez cinq minutes de plus" / "Se tiver cinco minutos a mais": three follow-up questions at most, C1 to C3.
5. "Pour le propriétaire ou le référent technique" / "Para o dono ou a referência técnica": the questions the developer cannot answer, which he forwards: what he said he does not know, what nobody decided, and any question about a decision (who checks the backup every day, who updates the folder). A question the developer can answer from what he knows, such as where the new code comes from at install time or where the e-mail password is kept, stays in "Questions" for him. Same layout, with an answer line where the person who answers writes their name.
6. "Répondu" / "Respondidas": the answered questions, with their date, moved here by the skill.

Numbers. Questions 1 to 10 keep the numbers of `references/questions.md`; follow-ups are C1 to C3. Any other question (what an answer left open, a question for the owner) takes the next free number from 11, never a number already used, and goes to "Questions" or to the block for the owner, never to the follow-up block, which holds C1 to C3 only, and says "suite de la question N" / "continua a pergunta N" when it is the open part of one. A question stands in one block only. A question that is answered in part moves to "Répondu" / "Respondidas" with the developer's answer word for word (only a secret is replaced), never shortened to what the next question did not take; its open part becomes a new question. The line that document 4 gives for the other symptoms names the number of the open question that holds them.

"I do not know" and "nobody decided" fill no field. The fields stay marked, the answer moves to "Respondidas" as the developer's answer, and the question, reworded, goes to the block for the owner or the referent. A document says "Lucas Ferreira ne sait pas" / "Lucas Ferreira não sabe", never that something does not exist or was never agreed, unless an answer says so in those words.

One question, in Portuguese:

```markdown
### Pergunta 7

Existe backup? Onde fica, com que frequência é feito, e quando foi a última vez que alguém conseguiu recuperar as informações a partir dele?

O que já sei: um programa copia as informações todo dia às 02:30 (arquivo de tarefas agendadas). Não sei se alguém já testou recuperar uma cópia.
Serve para: o que fazer se quebrar, quem guarda o quê e a lista de recepção.

Resposta:
```

A question the repository fully answered stays, in one line, as a confirmation: "Le dépôt dit : sauvegarde à 02:30. C'est bien celle-là ?" / "O repositório diz: backup às 02:30. É esse mesmo?".

An answer that holds a secret: replace the value with "(retiré)" / "(removido)" and write under it "Réponse retirée le DD/MM/YYYY : elle contenait un mot de passe. Écrivez seulement l'endroit où il est gardé." / "Resposta removida em DD/MM/YYYY: continha uma senha. Escreva só o lugar onde ela fica guardada.".

## answers.yml

One entry per answered question, under its number. The file exists from the first run as an empty mapping, `{}`. A later run adds entries. It changes an existing entry only for a line the user wrote under that question in "Répondu" / "Respondidas": "Confirmé par le propriétaire" / "Confirmado pelo dono" sets `confirmed_by`; "Correction" / "Correção" moves the old answer to `previous` and writes the new one. "History" notes each change. A value never holds a secret.

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

`answer` is the developer's text as he wrote it. A hedged answer ("acho que", "je crois") and "I do not know" fill no field of rule 3: `fields` leaves `vault`, `last_restore_date`, `backup_offsite` and `backup_encrypted` out until `confirmed_by` is set, and the documents write the hedge with the marker. `answered_by` is `user`, or `owner` when the user writes that the owner gave the answer. `confirmed_by` holds the owner's name and the date only when the user writes that the owner confirmed in person; the four fields of rule 3 (`vault`, `last_restore_date`, `backup_offsite`, `backup_encrypted`) keep their marker until it does. In the example, `last_restore_date` stays marked.

## verification.md

Fixed sections, in this order, and no other: an extra finding goes under "Contradictions found" or "Still marked". Each run that changes the pack rewrites them all except "History", which it extends. A run that changes nothing rewrites only the first lines and adds nothing to "History".

1. The first lines: "Run: DD/MM/YYYY, commit <short>"; "Status: draft" or "Status: ready for review"; "Second folder: <path>" when there are two languages. These lines change on every run, even one that changes nothing else: the hook compares file times with this file.
2. "Checks": one line per script and its result; the word and marker counts copied from the output of `coverage_check.py` after your last edit, never from memory. A run that changes the pack replaces the whole section; it keeps no line from an earlier run.
3. "Fixed": what this run corrected.
4. "Still marked": the markers left, per document.
5. "Still to rewrite": style or coverage flags that this run did not fix: in sections it did not change, in a pack written before the current rules, in a document edited by hand (marked "hand edit"), or because of a proposal that is pending (marked "proposal pending"). A hand edit made in one language only is listed here as a translation to do, and offered in the hand-back; the agent translates it only when the user asks. The hand-back counts every entry.
6. "Words kept on purpose": flagged words that are the right word in context.
7. "Words chosen": words picked for things that no list covers (rule 26 of `references/writing-style.md`).
8. "Contradictions found": both sides, each with its source (file and line, or question and date).
9. "Fingerprints": a table `| File | SHA-256 |`, one row per document 1 to 6 in each language, the `sha256sum` of the file as you leave it.
10. "History": a heading per run, `### DD/MM/YYYY, commit <short>`, with no tag after the commit, then three lines: what changed in the repository, what was answered, which documents moved.

## Fingerprints and hand edits

Before touching a document, compute its SHA-256 and compare it with "Fingerprints".

- Same hash: the document is yours to update.
- Different hash, and nothing that feeds this document changed: someone edited it by hand. Their version is the new baseline. Record its hash and leave it, even when a check flags it: the flags go under "Still to rewrite", marked "hand edit", and wait for the user.
- Different hash, and something that feeds it changed: do not overwrite it. Write your version beside it as `proposition-<name>.md` (French) or `proposta-<name>.md` (Portuguese), record both hashes, and name it in the hand-back. The same document of the other language gets a proposal too, translated from yours, so the two languages stay coherent until the user merges. While proposals are pending, `coverage_check.py --merged` checks the pack as it will be after the merge, and that is the result "Checks" records, with the word counts of the proposals. The user merges. `style_check.py` and `secret_scanner.py` read the proposals; `coverage_check.py` ignores them unless you give it `--merged`, which checks them in place of the documents they sit beside. When a later run finds the proposal gone, the document as it stands is the baseline.

A document you change takes the date of the run in its header (`{{doc_date}}`).

## What counts as a change

- A new answer in the questions file.
- In the inventory, without its `git` block: a service, a scheduled job, a variable name, a secret in clear or a deploy document that appeared or disappeared.
- A file of the successor list changed since the recorded commit, in a commit or in the working tree (`git diff --name-only <commit>` for tracked files, `git status --short` for new ones).

The successor list: compose and container files (`docker-compose*.yml`, `compose*.yml`, `Dockerfile*`), cron and systemd files, `.env.example` and its variants, deploy, operations, incident and runbook documents, scripts named like backup, import, sync, restore or migrate, Java or Kotlin files with `@Scheduled`, `application*.properties`, and the README.

A `.env` file is never a change, even when `git status --short` lists it as new: it is never opened. A new commit is not a change by itself: it only serves to list the changed files (`git diff --name-only <recorded commit>`). The version in document 6 moves only when the user says a version was installed.

## Hook contract

Implemented by `scripts/stop_hook.py`, which the plugin declares in `hooks/hooks.json`; the same contract serves a user who adds the hook by hand. The host is Claude Code. Codex has no equivalent that this skill relies on: its plugin hooks are documented only for a manual install in the desktop app.

- Event: `Stop`, which runs each time Claude finishes a turn. A `SessionEnd` hook cannot ask Claude for anything: Claude Code discards its output.
- Handler: a command hook, never a prompt hook, which cannot look at the repository. In the plugin, `hooks/hooks.json` declares it in exec form with the plugin's own path: `{"hooks": {"Stop": [{"hooks": [{"type": "command", "command": "python3", "args": ["${CLAUDE_PLUGIN_ROOT}/skills/bastao/scripts/stop_hook.py"], "timeout": 30}]}]}}`. `Stop` takes no matcher. Without the plugin, the same object goes in `.claude/settings.json` (the project) or `~/.claude/settings.json` (every project), with an absolute path or `${CLAUDE_PROJECT_DIR}`, because `${CLAUDE_PLUGIN_ROOT}` exists only for a plugin.
- The script reads the hook input, a JSON object, on stdin, and always exits 0; never 2. It prints nothing when `stop_hook_active` is true, when no pack is found from `cwd` (see "Where they live"), or when no file of the successor list and not the questions file is newer than `verification.md`. It stays fast: file times only, no model, no network.
- Otherwise it prints one JSON object: `{"hookSpecificOutput": {"hookEventName": "Stop", "additionalContext": "Bastão hook: repository <repo>, pack <folder>. Use the bastao skill to update the pack: files it describes changed, whatever this session did."}}`. Claude then goes on with that text as hook feedback. Claude Code also accepts `{"decision": "block", "reason": "..."}`, but shows it to the user as a hook error.
- Do not count on the cap of eight continuations in a row that Claude Code puts on `Stop` hooks: it starts again each time Claude uses a tool. What keeps the hook quiet is `stop_hook_active` and the time of `verification.md`.
- The skill recognises a hook run by the prefix "Bastão hook:". On a hook run it never asks in the chat, keeps the languages of the pack unless a new answer to question 10 changes them, says one line when nothing changed, and always rewrites the first lines of `verification.md`, so the hook stays quiet until a file changes again.
