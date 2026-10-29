# {{system_name}} : qui fait quoi

Préparé le {{doc_date}} par {{author}}, pour {{readers}}.

<!-- Deux pages au maximum. Une personne par ligne, jamais "l'équipe" ni "le service" : une tâche sans nom ne se fait pas.
     Le suppléant est obligatoire pour toute tâche dont l'oubli a une conséquence.
     Aucun mot de passe ici ni ailleurs : seulement le lieu où il est gardé. Le document 5 est la référence des accès ; ce qui est écrit ici en est une copie.
     Un champ sans réponse reçoit la marque [À CONFIRMER]. Écrire comme une personne (references/writing-style.md). -->

## Les personnes

| Nom | Fonction | Rôle dans le système | Joignable par |
|---|---|---|---|
| {{person_name}} | {{person_title}} | Propriétaire du système | {{person_contact}} |
| {{person_name}} | {{person_title}} | Référent technique | {{person_contact}} |
| {{person_name}} | {{person_title}} | Opérateur quotidien ({{operator_location}}) | {{person_contact}} |
| {{person_name}} | {{person_title}} | Développeur d'origine, disponible {{developer_availability}} | {{person_contact}} |

## Qui décide quoi

<!-- Réponse à la question 1. Les cinq décisions ci-dessous existent dans tout système ; en ajouter si le dépôt ou les réponses en révèlent d'autres. -->

| Décision | Qui décide | Qui doit être consulté avant | Qui est prévenu après |
|---|---|---|---|
| Changer une règle de fonctionnement | {{decision_maker}} | {{decision_consulted}} | {{decision_informed}} |
| Donner ou retirer un accès | {{decision_maker}} | {{decision_consulted}} | {{decision_informed}} |
| Installer une nouvelle version | {{decision_maker}} | {{decision_consulted}} | {{decision_informed}} |
| Renouveler une licence, un domaine, un contrat | {{decision_maker}} | {{decision_consulted}} | {{decision_informed}} |
| Arrêter le système, même temporairement | {{decision_maker}} | {{decision_consulted}} | {{decision_informed}} |

## Qui fait quoi, et quand

<!-- Le détail des gestes est dans le document 3 (Routine). Ici : seulement qui, à quelle fréquence, et ce qui arrive si c'est oublié. Trier par fréquence : quotidien, hebdomadaire, mensuel, annuel, à l'occasion. -->

| Tâche | Responsable | Suppléant | Fréquence | Si personne ne le fait |
|---|---|---|---|---|
| {{task}} | {{task_owner}} | {{task_deputy}} | {{task_frequency}} | {{task_if_missed}} |
| {{task}} | {{task_owner}} | {{task_deputy}} | {{task_frequency}} | {{task_if_missed}} |

## Ce que chacun peut faire sans aide, et ce qui demande un accord

<!-- Réponse à la question 6. C'est la limite qui protège le successeur : ce qu'il peut tenter sans risque, ce qui demande un oui du propriétaire, ce qu'il ne doit jamais faire sans le référent technique ou le développeur. -->

| Personne ou rôle | Peut faire sans aide | Avec l'accord du propriétaire | Jamais sans le référent technique ou le développeur |
|---|---|---|---|
| {{role}} | {{alone_list}} | {{with_owner_list}} | {{never_without_tech_list}} |

## Comptes et accès par rôle

<!-- Réponse à la question 2. Le détail (comment changer, qui a la clé) est dans le document 5. Ici : qui a quoi, et où c'est gardé. -->

| Rôle | Compte ou accès | Niveau | Gardé où |
|---|---|---|---|
| {{role}} | {{account}} | {{access_level_plain}} | {{custody_place}} |

## Quand quelqu'un part

<!-- Une ligne par rôle : ce qu'il faut transférer, et à qui. C'est la partie que personne n'écrit et que tout le monde cherche le jour du départ. -->

- Si {{role}} part : transférer {{transfer_what}} à {{transfer_to}}, et changer {{accesses_to_change}}.

---
Ce document fait partie du dossier de passation ({{doc_count}} documents). Une erreur ou un oubli ? Signalez-le à {{corrections_contact}}.
