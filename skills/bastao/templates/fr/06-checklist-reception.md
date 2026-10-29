# {{system_name}} : checklist de réception

Remis le {{doc_date}} par {{author}} à {{successor}} ({{successor_title}}, {{successor_role}}).

<!-- Une page. À remplir par le successeur, pas par le développeur. Chaque case cochée est une chose qu'il a vue ou faite lui-même, pas une chose qu'on lui a dite.
     Une case non cochée n'est pas un échec : c'est un point à régler avant la signature, à lister en bas avec un nom et une date.
     Rien n'est provoqué sur le système en production pour cocher une case.
     À l'export PDF : deux lignes de hauteur pour chaque ligne de signature. Écrire comme une personne, à la première personne, sans forme genrée (references/writing-style.md). -->

## J'ai reçu et lu

- [ ] Les documents 1 à 4 : ce que c'est, qui fait quoi, routine, si ça casse.
- [ ] Le document 5, garde des accès, reçu par le référent technique, {{tech_lead}}, qui signe ci-dessous.
- [ ] Le code source : {{repo_location}}, version {{repo_version}}.

## J'ai vérifié par moi-même

- [ ] Le programme affiche la version {{installed_version}}, installée le {{installed_date}}, et c'est bien celle du code source reçu.
- [ ] Je peux me connecter à {{main_access}} avec mon compte, pas celui du développeur.
- [ ] Je sais où sont gardés les secrets, et j'ai accès à ceux de mon rôle (document 2, « Comptes et accès par rôle ») sans les avoir reçus par message.
- [ ] Les accès personnels du développeur d'origine (serveur, application, équipements, hébergement, code) ont été retirés ou changés. Ce qu'il garde, et jusqu'à quand, est écrit dans le document 5.
- [ ] J'ai fait la vérification quotidienne du document 3 et obtenu : {{expected_result}}.
- [ ] J'ai vu une sauvegarde récente, du {{backup_seen_date}}, et je sais qui sait la restaurer.
- [ ] J'ai parcouru à blanc, avec {{author}}, un incident du document 4 ({{drill_incident}}) jusqu'au bout, sans rien provoquer sur le système, et les contacts du tableau « Qui appeler » ont répondu.
- [ ] Je connais les trois choses à ne jamais faire.
- [ ] Je sais quelles échéances tombent dans les douze prochains mois et qui s'en occupe.
- [ ] Je sais qui appeler, dans quel ordre, et jusqu'où je peux aller sans aide.
- [ ] Je sais où le dossier est gardé ({{dossier_location}}) et qui le met à jour quand une personne, une date ou un accès change.

## Ce qui reste à régler avant la signature

| Point | Qui | Pour quand |
|---|---|---|
| {{open_point}} | {{open_point_owner}} | {{open_point_due}} |

## Signatures

| | Nom | Date | Signature |
|---|---|---|---|
| Remis par | {{author}} | | |
| Reçu par | {{successor}} | | |
| Référent technique | {{tech_lead}} | | |
| Propriétaire du système | {{owner}} | | |

---
Ce document fait partie du dossier de passation ({{doc_count}} documents). Une erreur ou un oubli ? Signalez-le à {{corrections_contact}}.
