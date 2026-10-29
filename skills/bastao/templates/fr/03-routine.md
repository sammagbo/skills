# {{system_name}} : routine

Préparé le {{doc_date}} par {{author}}, pour {{readers}} (celles et ceux qui font tourner le système au quotidien).

Chaque geste fait et chaque vérification sont notés dans {{logbook}} : la date, le geste, qui l'a fait, le résultat. C'est le même cahier que pour les incidents (document 4).

<!-- Réponse à la question 3, complétée par le dépôt (scripts, tâches planifiées, sauvegardes, imports).
     Chaque geste est écrit pour être exécuté, pas compris : la commande exacte à coller, ou l'écran et le bouton exacts.
     Aucune commande qui modifie quelque chose sans dire d'abord comment vérifier qu'elle a réussi.
     Jamais de mot de passe ni de jeton dans une commande ou une capture d'écran ; aucune adresse contenant un identifiant (utilisateur:motdepasse@…, jeton dans une URL) ; aucune commande avec un mot de passe en argument ou en variable d'environnement. Quand une procédure exige un secret, écrire "(le mot de passe est dans {{vault}})".
     Si le dépôt contient une valeur en clair (docker-compose, script), ne jamais la reproduire : l'inscrire comme point à régler dans le document 6 ("secret en clair dans le dépôt : {{param_name}}").
     Préciser l'heure du serveur ou l'heure locale quand elles diffèrent.
     Ce que le dépôt ne prouve pas et que le propriétaire n'a pas confirmé reste [À CONFIRMER]. Écrire comme une personne (references/writing-style.md). -->

## Ce qui se fait tout seul, et comment vérifier que ça s'est fait

<!-- Tâches planifiées trouvées dans le dépôt (cron, tâches du système, scripts). Une ligne par tâche : quand (heure du serveur ou heure locale, dire laquelle), quoi, et comment voir que ça a tourné.
     La colonne "Si ça ne s'est pas fait" donne le geste, ou renvoie à un symptôme qui existe réellement dans le document 4. -->

| Quand | Ce qui se passe | Comment vérifier | Si ça ne s'est pas fait |
|---|---|---|---|
| {{auto_time}} | {{auto_task}} | {{auto_check}} | {{auto_if_missed}} |

## Tous les jours

<!-- Trois à cinq gestes au maximum. Si la liste est plus longue, quelque chose devrait être automatisé : le noter dans le document 6, "Ce qui reste à régler". -->

1. {{step}} : {{step_how}} ({{step_owner}}, environ {{step_duration}}).
2. {{step}} : {{step_how}} ({{step_owner}}, environ {{step_duration}}).

## Toutes les semaines

1. {{step}} : {{step_how}} ({{step_owner}}).

## Tous les mois

1. {{step}} : {{step_how}} ({{step_owner}}).

## Tous les ans

<!-- La partie qui se perd : rentrée, import des listes, renouvellements, archivage, changement d'année. Mettre la période habituelle et le délai de préparation. La dernière ligne (relecture du dossier) est fixe. -->

| Quand | Quoi | Qui | Délai de préparation | Comment |
|---|---|---|---|---|
| {{period}} | {{yearly_task}} | {{yearly_owner}} | {{lead_time}} | {{yearly_procedure}} |
| {{review_period}} | Relire les six documents du dossier : noms, contacts, dates, accès, points [À CONFIRMER] restants | {{review_owner}} | aucun | Corriger, redater, redistribuer. Le document 5 seulement à ses destinataires. |

## À l'occasion

<!-- Nouvelle personne à enregistrer, départ d'une personne, changement ou panne d'équipement, nouvelle version du programme, restauration d'une sauvegarde. Les quatre dernières lignes sont fixes. -->

- {{event}} : {{event_procedure}} ({{event_owner}}).
- Une personne nommée dans le dossier arrive ou part : {{update_owner}} met à jour les documents 2 et 5 le jour même.
- Un incident nouveau se produit : {{update_owner}} l'ajoute au document 4 et en retire un symptôme disparu, pour que le document reste sur une page.
- Installer une nouvelle version, avec l'accord prévu au document 2 (« Qui décide quoi »). D'abord une sauvegarde : {{backup_procedure}}. Ensuite : {{upgrade_procedure}}. Vérifier que ça a marché : {{upgrade_check}}. Si ça ne marche pas, revenir en arrière : {{rollback_procedure}}. Si la nouvelle version a modifié les informations enregistrées, les remettre aussi depuis la sauvegarde.
- Restaurer une sauvegarde. Attention : cela remplace toutes les informations actuelles par celles de la sauvegarde, et tout ce qui a été saisi depuis est perdu. D'abord sauvegarder l'état actuel ({{backup_procedure}}), puis {{restore_procedure}}. Dernière restauration prouvée le {{last_restore_date}}. <!-- même date que le document 5, "Sauvegardes" -->

## Les commandes à coller

Cette partie s'adresse au référent technique. Les autres lecteurs peuvent passer.

<!-- Chaque commande est précédée de ce qu'elle fait et suivie de ce qu'on doit voir. Les commandes de vérification d'abord (elles ne modifient rien), la commande qui modifie ensuite, jamais enchaînées sur une seule ligne. -->

```bash
# Vérifier que le programme tourne. Ne modifie rien. On doit voir : {{expected_state}}
{{check_command}}

# Voir les derniers messages du programme. Ne modifie rien. On ne doit pas voir : {{error_word}}
{{log_command}}

# Redémarrer le programme. Seulement si la vérification ci-dessus ne montre pas {{expected_state}}. Ensuite, refaire la vérification.
{{restart_command}}
```

---
Ce document fait partie du dossier de passation ({{doc_count}} documents). Une erreur ou un oubli ? Signalez-le à {{corrections_contact}}.
