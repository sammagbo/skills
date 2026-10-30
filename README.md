# sammagbo/skills

Skills for AI coding agents (Claude Code, Codex, Antigravity, Cursor, GitHub Copilot), written by Sammy K. Magbo. The first one, Bastão, writes the handover pack a non-technical organization needs when a developer hands over a system. Instructions below are in French, then in Portuguese. Status: experimental, version 0.1.0 (see CHANGELOG.md).

## Bastão

### Français

Bastão écrit le dossier de passation d'un système qu'un développeur remet à une organisation qui n'a pas d'équipe technique : une école, une association, une petite entreprise. Il part du dépôt et de dix questions, et produit six documents en français et en portugais, vérifiés contre le dépôt, sans aucun secret à l'intérieur.

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
- Les marketplaces de plugins (Claude Code, Codex, Antigravity) arrivent avec la version 0.2.
- Les vérifications passent par quatre scripts Python (bibliothèque standard, sans réseau). Pour éviter une demande d'autorisation à chaque vérification, autorisez une fois `python3 */bastao/scripts/*.py` dans votre agent.

Exemple complet, sur un dépôt fictif : `examples/estante/`. Extrait du document 4 :

> **Les étiquettes ne sortent pas de l'imprimante**
>
> - Vérifiez d'abord, sans risque : l'imprimante Zebra est-elle allumée ? Le PC de la bibliothèque a-t-il reçu une mise à jour de Windows ?
> - Le plus souvent, ça veut dire : l'adresse réseau de l'imprimante a changé (08/2026).
> - Ce que vous pouvez faire vous-même : rien. Denise Prado réimprime.
> - C'est réparé quand : une étiquette sort entière.
> - Si ça ne suffit pas, appelez Denise Prado, puis Etiquetas Exemplo.

Essayer : « Prépare le dossier de passation de ce dépôt pour l'équipe informatique du client, en français et en portugais. » L'agent lit le dépôt, pose dix questions une par une, puis écrit le dossier dans `passation/`.

### Português

Bastão escreve a pasta de passagem de um sistema que um desenvolvedor entrega a uma organização sem equipe técnica: uma escola, uma associação, uma pequena empresa. Ele parte do repositório e de dez perguntas, e produz seis documentos em francês e em português, verificados contra o repositório, sem nenhum segredo dentro.

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
- Os marketplaces de plugins (Claude Code, Codex, Antigravity) chegam com a versão 0.2.
- As verificações passam por quatro scripts Python (biblioteca padrão, sem rede). Para evitar um pedido de permissão a cada verificação, autorize uma vez `python3 */bastao/scripts/*.py` no seu agente.

Exemplo completo, num repositório fictício: `examples/estante/`. Trecho do documento 4:

> **As etiquetas não saem na impressora**
>
> - Verifique primeiro, sem risco: a impressora Zebra está ligada? O PC da biblioteca recebeu uma atualização do Windows?
> - Na maioria das vezes, isso quer dizer: o endereço da impressora na rede mudou (08/2026).
> - O que você pode fazer por conta própria: nada. Denise Prado reimprime.
> - Está consertado quando: uma etiqueta sai inteira.
> - Se não resolver, chame Denise Prado, depois a Etiquetas Exemplo.

Experimente: "Prepare a pasta de passagem deste repositório para a equipe de TI do cliente, em francês e em português." O agente lê o repositório, faz dez perguntas uma por vez e escreve a pasta em `passagem/`.

## Repository layout

```
examples/
└── estante/        a complete pack produced on a fictional repository
skills/
└── bastao/
    ├── SKILL.md
    ├── templates/fr/   six documents in French
    ├── templates/pt/   six documents in Brazilian Portuguese
    ├── references/     questions, field dictionary, plain language, writing style, secret patterns
    ├── scripts/        inventory, secret scanner, coverage check, style check
    └── tests/          a fictional repository, a simulated run, unit tests
```

## Contributing

Open an issue with the "handover report" template when a generated pack missed something the successor needed. Pull requests are welcome for new languages (same section structure, same field keys) and for new hosts. Commit messages in English.

## License

Apache-2.0. See LICENSE.
