# {{system_name}} : ce que c'est et ce que ça ne fait pas

Préparé le {{doc_date}} par {{author}}, pour {{readers}} (direction, gestion, équipe informatique).

<!-- Une page au maximum, environ 350 mots. Aucun terme technique sans sa traduction en langage courant (references/plain-language.md) :
     "backend" devient "le programme qui tourne sur le serveur", "conteneur" devient "la boîte dans laquelle le programme tourne",
     "API" devient "la porte par laquelle d'autres programmes lui parlent", "base de données" devient "l'endroit où les informations sont enregistrées".
     Un champ que ni le dépôt ni les réponses ne remplissent reçoit la marque [À CONFIRMER], jamais une phrase plausible.
     Écrire comme une personne : phrases courtes, verbes simples (est, a, sert à), pas de tiret long, pas de gras dans les listes (references/writing-style.md). -->

## En une phrase

{{system_name}} sert à {{purpose_plain}}. Qui l'utilise : {{users}}.

## Ce que ça fait

<!-- Trois à six lignes, une fonction par ligne, en commençant par ce que l'organisation voit tous les jours. -->

- {{feature}}. Utilisé par {{feature_users}}, {{feature_when}}.
- {{feature}}. Utilisé par {{feature_users}}, {{feature_when}}.
- {{feature}}. Utilisé par {{feature_users}}, {{feature_when}}.

## Ce que ça ne fait pas

<!-- Réponse à la question 4. Chaque ligne dit aussi pourquoi on pourrait croire le contraire : c'est cette croyance qui provoque les incidents. -->

- {{not_feature}}. On pourrait le croire, parce que {{not_feature_reason}}.
- {{not_feature}}. On pourrait le croire, parce que {{not_feature_reason}}.

## Où ça tourne

- Le programme tourne sur {{server_location}}.
- On y accède par {{access_mode}} (une application installée sur les postes, un navigateur, ou les deux).
- Pour fonctionner, il a besoin de {{external_dependencies}}.
- Les informations sont enregistrées dans {{storage_plain}} et sauvegardées {{backup_frequency}}.

## Qui en est responsable

| Rôle | Nom et fonction | Ce que cette personne décide ou fait |
|---|---|---|
| Propriétaire du système | {{owner}} | Décide des changements et des renouvellements |
| Référent technique | {{tech_lead}} | Première personne à appeler quand quelque chose ne va pas |
| Développeur d'origine | {{author}} | Disponible {{developer_availability}} |

## Ce qui a une date

<!-- Réponse à la question 8. S'il n'y a rien, écrire "Aucune échéance connue au {{doc_date}}". Le document 5 est la référence de ces dates. -->

| Échéance | Quoi | Qui s'en occupe | Si c'est oublié |
|---|---|---|---|
| {{due_date}} | {{due_item}} | {{due_owner}} | {{due_consequence}} |

## Les trois choses à ne jamais faire

<!-- Tirées des incidents (question 5) et des dépendances (question 9). Une ligne chacune, au présent, sans adjectif. Trois est une limite de place, pas une figure de style. -->

1. {{forbidden_1}}, parce que {{forbidden_1_reason}}.
2. {{forbidden_2}}, parce que {{forbidden_2_reason}}.
3. {{forbidden_3}}, parce que {{forbidden_3_reason}}.

---
Ce document fait partie du dossier de passation ({{doc_count}} documents). Une erreur ou un oubli ? Signalez-le à {{corrections_contact}}.
