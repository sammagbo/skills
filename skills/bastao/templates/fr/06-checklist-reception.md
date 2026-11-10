# {{system_name}} : checklist de réception

Préparé le {{doc_date}} par {{author}} pour le propriétaire, {{owner}}, et le référent technique, {{tech_lead}}.

<!-- Une page. Deux personnes reçoivent, chacune avec sa partie : le propriétaire confirme ce qu'il décide et ce qu'il sait ; le référent technique vérifie ce qui touche au système. Chaque personne coche seulement ce qu'elle a vu ou fait elle-même, pas ce qu'on lui a dit. Le développeur ne remplit rien, il signe.
     Une case non cochée n'est pas un échec : c'est un point à régler avant la signature, à lister en bas avec qui décide et pour quand.
     Rien n'est provoqué sur le système en production pour cocher une case.
     Chaque ligne vaut pour la personne de sa partie : sans propriétaire, sans référent technique ou sans réponse pour un champ, la marque, jamais une phrase sur une autre personne. Une case dit ce que la personne a fait, jamais un fait sur qui d'autre a quoi. La disponibilité du développeur garde la limite que les réponses donnent (seulement des questions, sans toucher à la machine). repo_location est le lieu du code : dossier et machine. La version installée n'est cochée que si le document 3 donne un moyen de la lire sans rien provoquer ; sinon la case reste vide et le tableau le dit. Entrent dans le tableau, avec qui décide quand une réponse le donne : qui fait la vérification quotidienne, qui retire les accès du développeur et quand, et chaque point ouvert dont une case dépend.
     À l'export PDF : deux lignes de hauteur pour chaque ligne de signature. Écrire comme une personne, à la première personne de celui qui coche, sans forme genrée (references/writing-style.md). -->

## Le propriétaire confirme

- [ ] J'ai lu les documents 1, 2 et 4 et je sais ce que le système ne fait pas.
- [ ] Je sais les trois choses à ne jamais faire, qui décide quoi, qui appeler et les échéances de l'année.
- [ ] J'ai reçu le document 5 et je ne l'ai pas transmis.
- [ ] Je suis d'accord que {{update_owner}} met ce dossier à jour.
- [ ] Je connais la disponibilité de {{author}} ({{developer_availability}}) et la sortie de ses accès ({{access_change_deadline}}).

## Le référent technique vérifie

- [ ] J'ai lu les documents 1 à 5 et reçu le programme : {{repo_location}}, version {{repo_version}}.
- [ ] Le programme installé est en version {{installed_version}}.
- [ ] Je me connecte à {{main_access}} avec mon compte et j'ai les mots de passe de mon rôle.
- [ ] J'ai fait la vérification quotidienne du document 3. Attendu : {{expected_result}}. Vu : ________.
- [ ] J'ai vu une copie récente des informations, du {{backup_seen_date}}.
- [ ] J'ai parcouru avec {{author}} un incident du document 4 ({{drill_incident}}), sans rien provoquer.

## Ce qui reste à régler avant la signature

<!-- Chaque phrase qui parle du coffre des mots de passe, de la dernière restauration, de la copie hors de la machine ou du chiffrement porte sa marque [À CONFIRMER] dans la phrase, et la réserve de celui qui a répondu (« je crois ») reste. La marque dans les colonnes Qui décide et Pour quand ne compte pas. Les secrets écrits sans protection : le nom de la variable, suivi de ce que c'est en mots simples. Qui décide et Pour quand : le nom et la date qu'une réponse donne ; sinon, une ligne vide, ________, à remplir le jour même. -->

Chaque point reçoit un nom et une date avant la signature.

| Point | Qui décide | Pour quand |
|---|---|---|
| {{open_point}} | {{open_point_owner}} | {{open_point_due}} |

## Signatures

| | Nom | Date | Signature |
|---|---|---|---|
| Remis par | {{author}} | | |
| Propriétaire du système | {{owner}} | | |
| Référent technique | {{tech_lead}} | | |

{{author}} signe qu'il a remis ; les deux autres signent leur partie.

---
Ce document fait partie du dossier de passation ({{doc_count}} documents). Une erreur ou un oubli ? Signalez-le à {{corrections_contact}}.
