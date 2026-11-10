# sammagbo/skills

Skills for AI coding agents (Claude Code, Codex, Antigravity, Cursor, GitHub Copilot), written by Sammy K. Magbo. The first one, Bastão, writes the handover pack a non-technical organization needs when a developer hands over a system. Instructions below are in French, then in Portuguese. Status: experimental, version 0.1.0 (see CHANGELOG.md).

## Bastão

### Français

Bastão écrit le dossier de passation d'un système qu'un développeur remet à une organisation qui n'a pas d'équipe technique : une école, une association, une petite entreprise. Il part du dépôt, écrit d'abord ce que le dépôt prouve, marque le reste, et laisse ses questions dans un fichier que vous remplissez quand vous avez le temps. Six documents en français et en portugais, vérifiés contre le dépôt, sans aucun secret à l'intérieur.

Les règles d'écriture s'inspirent de la norme ASD-STE100 (Simplified Technical English, Issue 9), adaptées au français et au portugais : vingt mots par phrase dans les procédures, une instruction par phrase, un mot pour une chose. La skill ne revendique aucune conformité à cette norme, dont le dictionnaire n'existe qu'en anglais, et elle n'est ni approuvée par l'ASD ni liée à elle.

Pour qui : le développeur qui livre ou qui part, et la personne qui garde le système après lui.

Les six documents :

1. Ce que c'est et ce que ça ne fait pas (une page).
2. Qui fait quoi.
3. Routine : ce qui se fait tout seul, tous les jours, toutes les semaines, tous les ans.
4. Si ça casse (une page, lue sous stress).
5. Garde des accès : où sont les secrets, qui a la clé, jamais les secrets eux-mêmes.
6. Checklist de réception, signée par la personne qui reçoit.

Ce que la skill ne fait jamais : lire ou recopier un mot de passe, une clé ou un jeton ; inventer ce que le dépôt ne prouve pas (elle écrit [À CONFIRMER]) ; envoyer quoi que ce soit à un service ; écrire dans vos systèmes.

Installation :

- Avec la CLI skills, pour la plupart des agents : `npx skills@latest add sammagbo/skills`
- Claude Code, à la main : copier `skills/bastao/` dans `.claude/skills/bastao/` (le projet) ou `~/.claude/skills/bastao/` (tous les projets).
- Codex : `$skill-installer install https://github.com/sammagbo/skills/tree/main/skills/bastao`
- Claude Code, avec le plugin (il apporte aussi le hook de mise à jour) : `/plugin marketplace add sammagbo/skills`, puis `/plugin install bastao@sammagbo-skills`. Les fichiers du plugin pour Codex sont dans le dépôt (`plugin.json`, `.agents/plugins/marketplace.json`) ; ils n'ont pas encore été essayés dans Codex. Antigravity : par la CLI skills ci-dessus.
- Les vérifications passent par quatre scripts Python (bibliothèque standard, sans réseau). Pour éviter une demande d'autorisation à chaque vérification, autorisez une fois `python3 */bastao/scripts/*.py` dans votre agent.

Exemple complet, sur un dépôt fictif : `examples/estante/`. Extrait du document 4 :

> **Les rappels par e-mail ne partent pas (06/2026)**
>
> - Vérifiez d'abord, sans risque : l'abonnement MailExemplo est-il payé sur la carte de l'école ?
> - La dernière fois, la cause était : la carte n'a pas payé, MailExemplo a bloqué le compte.
> - Ce que vous pouvez faire vous-même : seulement la vérification. Demandez le paiement à Roberto, des finances.
> - C'est réparé quand : les rappels repartent.
> - Si ça ne suffit pas, appelez Denise Prado.

Essayer : « Prépare le dossier de passation de ce dépôt pour l'équipe informatique du client. » L'agent lit le dépôt, écrit le dossier dans `passation/` et laisse ses questions dans `passation/00-questions.md`. Répondez quand vous voulez ; au passage suivant, il complète le dossier. Avec le plugin, un hook regarde à la fin de chaque réponse de l'agent si un fichier dont le dossier dépend a changé. Si oui, il demande à l'agent de mettre le dossier à jour. Tant que le dossier n'existe pas, il ne fait rien.

### Português

Bastão escreve a pasta de passagem de um sistema que um desenvolvedor entrega a uma organização sem equipe técnica: uma escola, uma associação, uma pequena empresa. Ele parte do repositório, escreve primeiro o que o repositório prova, marca o resto, e deixa as perguntas num arquivo que você preenche quando tiver tempo. Seis documentos em francês e em português, verificados contra o repositório, sem nenhum segredo dentro.

As regras de escrita se inspiram na norma ASD-STE100 (Simplified Technical English, Issue 9), adaptadas ao francês e ao português: vinte palavras por frase nos procedimentos, uma instrução por frase, uma palavra para cada coisa. A skill não afirma conformidade com essa norma, cujo dicionário só existe em inglês, e não é aprovada pela ASD nem ligada a ela.

Para quem: o desenvolvedor que entrega ou que sai, e a pessoa que fica com o sistema depois dele.

Os seis documentos:

1. O que é e o que não faz (uma página).
2. Quem faz o quê.
3. Rotina: o que acontece sozinho, todo dia, toda semana, todo ano.
4. Se quebrar (uma página, lida sob estresse).
5. Custódia de acessos: onde estão os segredos, quem tem a chave, nunca os segredos em si.
6. Checklist de recepção, assinada por quem recebe.

O que a skill nunca faz: ler ou copiar uma senha, uma chave ou um token; inventar o que o repositório não prova (ela escreve [A CONFIRMAR]); mandar qualquer coisa para um serviço; escrever nos seus sistemas.

Instalação:

- Com a CLI skills, para a maioria dos agentes: `npx skills@latest add sammagbo/skills`
- Claude Code, à mão: copiar `skills/bastao/` para `.claude/skills/bastao/` (o projeto) ou `~/.claude/skills/bastao/` (todos os projetos).
- Codex: `$skill-installer install https://github.com/sammagbo/skills/tree/main/skills/bastao`
- Claude Code, com o plugin (ele traz também o hook de atualização): `/plugin marketplace add sammagbo/skills` e depois `/plugin install bastao@sammagbo-skills`. Os arquivos do plugin para o Codex estão no repositório (`plugin.json`, `.agents/plugins/marketplace.json`); ainda não foram experimentados no Codex. Antigravity: pela CLI skills acima.
- As verificações passam por quatro scripts Python (biblioteca padrão, sem rede). Para evitar um pedido de permissão a cada verificação, autorize uma vez `python3 */bastao/scripts/*.py` no seu agente.

Exemplo completo, num repositório fictício: `examples/estante/`. Trecho do documento 4:

> **Os lembretes por e-mail não saem (06/2026)**
>
> - Verifique primeiro, sem risco: o plano do e-mail MailExemplo está pago no cartão da escola?
> - Da última vez, a causa foi: o cartão não pagou, e o MailExemplo bloqueou a conta.
> - O que você pode fazer por conta própria: só a verificação. Peça o pagamento a Roberto, do financeiro.
> - Está consertado quando: os lembretes voltam a sair.
> - Se não resolver, chame Denise Prado.

Experimente: "Prepare a pasta de passagem deste repositório para a equipe de TI do cliente." O agente lê o repositório, escreve a pasta em `passagem/` e deixa as perguntas em `passagem/00-perguntas.md`. Responda quando quiser; na rodada seguinte, ele completa a pasta. Com o plugin, um hook olha no fim de cada resposta do agente se um arquivo de que a pasta depende mudou. Se mudou, pede ao agente que atualize a pasta. Enquanto a pasta não existe, ele não faz nada.

## Repository layout

```
.claude-plugin/     plugin.json and marketplace.json for Claude Code
.agents/plugins/    marketplace.json for Codex
plugin.json         plugin manifest for Codex
hooks/hooks.json    the end-of-turn hook (Claude Code)
examples/
└── estante/        a complete pack produced on a fictional repository
skills/
└── bastao/
    ├── SKILL.md
    ├── templates/fr/   six documents in French
    ├── templates/pt/   six documents in Brazilian Portuguese
    ├── references/     questions, pack files, field dictionary, plain language, writing style, successor needs, secret patterns
    ├── scripts/        inventory, secret scanner, coverage check, style check, stop hook
    └── tests/          a fictional repository, a pack, unit tests
```

## Contributing

Open an issue with the "handover report" template when a generated pack missed something the successor needed. Pull requests are welcome for new languages (same section structure, same field keys) and for new hosts. Commit messages in English.

## License

Apache-2.0. See LICENSE.
