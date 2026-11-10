# Exemple : Estante (fictif) / Exemplo: Estante (fictício)

## Français

Ce dossier montre ce que Bastão produit en mode passif, sur le dépôt fictif `skills/bastao/tests/fixtures/estante` (le système de prêt de livres d'une école imaginaire). Aucune personne, école ou entreprise réelle.

Comment il a été fait, en trois temps. D'abord, la skill a lu le dépôt et écrit le dossier en portugais, sans poser aucune question, avec `00-perguntas.md` pour les questions. Ensuite, un second agent a joué le développeur qui part : il a répondu à ce fichier à partir d'une liste de faits écrite à l'avance (`skills/bastao/tests/cases/estante/verdade.md`), et à elle seule. Enfin, la skill a relu les réponses, complété le dossier et ajouté la version française, que la réponse à la question 10 demandait.

Ensuite, quatre relecteurs indépendants ont comparé le dossier aux faits, aux règles, à la langue et aux besoins de ses lecteurs. Seul ce qui était faux ou une erreur de langue a été corrigé à la main : 26 lignes, listées dans l'historique de `passagem/verification.md`. Le reste de ce que les relecteurs ont trouvé est dit plus bas.

Les marques [À CONFIRMER] sont normales : ce sont les points que le développeur ne savait pas, ou que seul le propriétaire peut confirmer. Le dossier les montre au lieu de les inventer. Le document 5 serait, dans la réalité, réservé à ses deux destinataires.

Où sont les fichiers : `passagem/` est le dossier de la première langue et garde aussi `00-perguntas.md` (avec les réponses), `answers.yml` et `verification.md`. `passation/` est la version française. `inventory.json` n'est pas gardé : il contient le chemin de la machine et le commit du test, et `inventory.py` le refait.

Limites connues de cet exemple :

- Dans les documents 2, 3 et 5 en portugais, la skill a écrit « cópia » là où la table des mots approuvés demande « backup ».
- Trois questions du fichier de questions en posent plus de deux à la fois.
- Les documents 4 et 6 sont à 400 mots en français : la limite et les lignes fixes des modèles se gênent.
- Le document 6 a été réécrit à la main d'après le nouveau modèle (une partie pour la propriétaire, une pour la référente technique), à partir des seules réponses et des autres documents ; il n'est pas issu d'un passage de la skill.

## Português

Esta pasta mostra o que o Bastão produz no modo passivo, sobre o repositório fictício `skills/bastao/tests/fixtures/estante` (o sistema de empréstimo de livros de uma escola imaginária). Nenhuma pessoa, escola ou empresa real.

Como foi feita, em três tempos. Primeiro, a skill leu o repositório e escreveu a pasta em português, sem fazer nenhuma pergunta, deixando as perguntas em `00-perguntas.md`. Depois, um segundo agente fez o papel do desenvolvedor que sai: respondeu a esse arquivo a partir de uma lista de fatos escrita antes (`skills/bastao/tests/cases/estante/verdade.md`), e só dela. Por fim, a skill leu as respostas, completou a pasta e acrescentou a versão em francês, que a resposta à pergunta 10 pedia.

Em seguida, quatro revisores independentes compararam a pasta com os fatos, com as regras, com a língua e com as necessidades de quem a lê. Só o que era falso ou erro de língua foi corrigido à mão: 26 linhas, listadas no histórico de `passagem/verification.md`. O resto do que os revisores acharam está abaixo.

As marcas [A CONFIRMAR] são normais: são os pontos que o desenvolvedor não sabia, ou que só o dono pode confirmar. A pasta mostra esses pontos em vez de inventar. Na vida real, o documento 5 ficaria só com os seus dois destinatários.

Onde ficam os arquivos: `passagem/` é a pasta da primeira língua e guarda também `00-perguntas.md` (com as respostas), `answers.yml` e `verification.md`. `passation/` é a versão em francês. O `inventory.json` não é guardado: ele leva o caminho da máquina e o commit do teste, e o `inventory.py` o refaz.

Limites conhecidos deste exemplo:

- Nos documentos 2, 3 e 5 em português, a skill escreveu "cópia" onde a tabela de palavras aprovadas pede "backup".
- Três perguntas do arquivo de perguntas fazem mais de duas coisas de uma vez.
- Os documentos 4 e 6 estão em 400 palavras no francês: o limite e as linhas fixas dos modelos se atrapalham.
- O documento 6 foi reescrito à mão a partir do modelo novo (uma parte para a dona, uma para a referência técnica), só com as respostas e os outros documentos; ele não saiu de uma rodada da skill.
