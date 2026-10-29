# {{system_name}} : garde des accès

Préparé le {{doc_date}} par {{author}}, pour {{owner}} et {{tech_lead}} seulement. Ne pas diffuser plus loin.

<!-- Ce document ne contient aucun mot de passe, aucune clé, aucun jeton. Il dit ce qui existe, où c'est gardé, qui y a accès, comment le changer, et ce qui arrive si c'est perdu ou divulgué.
     Le scanner de secrets refuse la génération si une valeur ressemble à un mot de passe, une clé ou un jeton.
     Aucune adresse contenant un identifiant (utilisateur:motdepasse@…, jeton dans une URL), aucune commande avec un mot de passe en argument ou en variable d'environnement. Quand une procédure exige un secret, écrire "(le mot de passe est dans {{vault}})".
     Les noms des paramètres viennent du dépôt (fichiers d'exemple, docker-compose, scripts). Si le dépôt contient une valeur en clair, ne jamais la reproduire : l'inscrire comme point à régler dans le document 6 ("secret en clair dans le dépôt : {{param_name}}").
     Ce document est la référence pour les accès et leurs dates ; le document 2 "Comptes et accès par rôle" et le document 1 "Ce qui a une date" en sont des copies, à corriger ensemble.
     Si le développeur d'origine garde un accès après la passation, il apparaît dans l'inventaire avec une date de fin.
     {{vault}}, {{last_restore_date}}, {{backup_offsite}} et {{backup_encrypted}} gardent la marque [À CONFIRMER] tant que le propriétaire ne les a pas confirmés de vive voix, même si le dépôt suggère une valeur.
     À l'export PDF : ce document peut passer en paysage si les tableaux sont serrés. Écrire comme une personne (references/writing-style.md). -->

## Règles de garde

1. Chaque accès a un gardien nommé et un suppléant.
2. Les secrets vivent à un seul endroit de référence : {{vault}} (un gestionnaire de mots de passe, un coffre, une enveloppe scellée).
3. Quand une personne part, les accès qu'elle connaissait sont changés dans les {{access_change_deadline}}. La liste est dans le document 2, « Quand quelqu'un part ».
4. Aucun secret par e-mail, par message ou dans un document partagé. Jamais dans ce dossier.
5. Un compte partagé (« admin », « root », le compte d'un équipement) n'est utilisé que si l'outil n'offre pas de comptes individuels. Il a quand même un gardien et un suppléant, il est gardé dans {{vault}}, et il est changé à chaque départ d'une personne qui le connaissait. Dans l'inventaire, ces comptes portent la mention « (partagé) ».

## Inventaire des accès

<!-- Une ligne par accès, même ceux que l'organisation croit évidents. Les lignes ci-dessous sont les catégories habituelles ; retirer celles qui n'existent pas, ajouter celles que le dépôt révèle. Les mêmes lignes, dans le même ordre, dans les deux tableaux. -->

| Accès | À quoi il sert | Qui le détient | Suppléant | Gardé où |
|---|---|---|---|---|
| Serveur : connexion à la machine ({{server_location}}) | {{access_use}} | {{access_holder}} | {{access_deputy}} | {{access_place}} |
| Hébergeur : console du fournisseur (créer, arrêter, supprimer la machine) | {{access_use}} | {{access_holder}} | {{access_deputy}} | {{access_place}} |
| Compte administrateur de l'application | {{access_use}} | {{access_holder}} | {{access_deputy}} | {{access_place}} |
| Base de données : accès direct aux informations | {{access_use}} | {{access_holder}} | {{access_deputy}} | {{access_place}} |
| Équipements ({{equipment_type}}) | {{access_use}} | {{access_holder}} | {{access_deputy}} | {{access_place}} |
| Nom de domaine et certificat | {{access_use}} | {{access_holder}} | {{access_deputy}} | {{access_place}} |
| Espace où sont déposées les sauvegardes | {{access_use}} | {{access_holder}} | {{access_deputy}} | {{access_place}} |
| Clé de licence ou de signature | {{access_use}} | {{access_holder}} | {{access_deputy}} | {{access_place}} |
| Code source ({{repo_location}}) | {{access_use}} | {{access_holder}} | {{access_deputy}} | {{access_place}} |

### Changer et récupérer

| Accès | Comment le changer | Si c'est perdu ou divulgué |
|---|---|---|
| Serveur | {{access_change_procedure}} | {{access_loss_recovery}} |
| Hébergeur | {{access_change_procedure}} | {{access_loss_recovery}} |
| Compte administrateur de l'application | {{access_change_procedure}} | {{access_loss_recovery}} |
| Base de données | {{access_change_procedure}} | {{access_loss_recovery}} |
| Équipements | {{access_change_procedure}} | {{access_loss_recovery}} |
| Nom de domaine et certificat | {{access_change_procedure}} | {{access_loss_recovery}} |
| Espace des sauvegardes | {{access_change_procedure}} | {{access_loss_recovery}} |
| Clé de licence ou de signature | {{access_change_procedure}} | {{access_loss_recovery}} |
| Code source | {{access_change_procedure}} | {{access_loss_recovery}} |

## Paramètres sensibles du système (noms seulement)

<!-- Liste des paramètres trouvés dans le dépôt, avec leur rôle en langage courant. Jamais la valeur. -->

| Nom du paramètre | À quoi il sert | Où il est défini sur le serveur |
|---|---|---|
| {{param_name}} | {{param_role_plain}} | {{param_location}} |

## Sauvegardes

<!-- Réponse à la question 7. Une sauvegarde est un accès comme un autre : qui peut la lire, qui peut la restaurer, où elle est. -->

- Où : {{backup_location}}.
- À quelle fréquence : {{backup_frequency}}.
- Conservées pendant : {{backup_retention}}.
- Copie hors du serveur : {{backup_offsite}}. Chiffrée : {{backup_encrypted}}.
- Dernière restauration prouvée : le {{last_restore_date}}, par {{last_restore_by}}.
- Qui sait restaurer : {{restore_person}}. La procédure est dans le document 3, « À l'occasion ».
- Qui peut lire une sauvegarde (elle contient des informations personnelles) : {{backup_readers}}.

## Prochaines échéances liées aux accès

| Date | Quoi (certificat, domaine, licence, mot de passe à renouveler) | Qui |
|---|---|---|
| {{due_date}} | {{due_item}} | {{due_owner}} |

---
Ce document fait partie du dossier de passation ({{doc_count}} documents). Une erreur ou un oubli ? Signalez-le à {{corrections_contact}}.
