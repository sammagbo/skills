# Estante : routine

Préparé le 30/10/2026 par Lucas Ferreira, pour Márcia Okafor, Paula Reis, Joana Lima et Denise Prado (celles et ceux qui font tourner le système au quotidien).

Chaque geste fait et chaque vérification sont notés dans [À CONFIRMER] : la date, le geste, qui l'a fait, le résultat. C'est le même cahier que pour les incidents (document 4).

## Ce qui se fait tout seul, et comment vérifier que ça s'est fait

Les heures ci-dessous sont celles de l'horloge du mini-PC ESTANTE01. Si cette horloge est à l'heure de Brasília : [À CONFIRMER]. Le programme utilise America/Sao_Paulo (l'heure de Brasília).

| Quand | Ce qui se passe | Comment vérifier | Si ça ne s'est pas fait |
|---|---|---|---|
| 02:30, tous les jours | Le script backup.sh enregistre une copie des informations (sauvegarde) dans /home/estante/backups, sur le mini-PC lui-même, et efface les copies de plus de 30 jours | Il existe un fichier estante-AAAA-MM-JJ.dump à la date du jour, et le fichier /home/estante/backup.log ne montre pas d'erreur | Denise Prado fait une sauvegarde tout de suite (commandes à la fin) et prévient Lucas Ferreira jusqu'au 31/01/2027 |
| 07:00, du lundi au vendredi | Le programme app.lembretes envoie un e-mail aux responsables de chaque élève qui a un livre en retard de plus de 3 jours | Il n'y a pas de trace propre. Le signe, c'est un responsable qui dit ne pas l'avoir reçu. | Voir le symptôme « Les responsables ne reçoivent pas les e-mails de rappel » dans le document 4 |

## Tous les jours

1. Vérification du matin : ouvrir https://estante.jacaranda.example.org dans le navigateur et voir l'écran d'Estante ([À CONFIRMER] qui le fait, décision de Márcia Okafor ; environ [À CONFIRMER]).

## Toutes les semaines

Aucun geste hebdomadaire défini au 30/10/2026.

## Tous les mois

1. Paiement de l'e-mail MailExemplo : l'abonnement est mensuel, sur la carte de l'école (Roberto, des finances).

## Tous les ans

| Quand | Quoi | Qui | Délai de préparation | Comment |
|---|---|---|---|---|
| Février | Importer la liste des élèves, à partir du fichier CSV du secrétariat | Denise Prado | Demander le fichier au secrétariat avant ; qui le demande : [À CONFIRMER] | Le fichier doit être en UTF-8. Les élèves absents du fichier deviennent inactifs, ils ne sont pas effacés. Commandes à la fin. |
| Début de chaque semestre | Enregistrer les livres neufs et imprimer les étiquettes | Joana Lima | aucun | Dans l'écran d'Estante [À CONFIRMER] |
| Avant le 14/03/2027 | Renouveler le domaine jacaranda.example.org (l'adresse du site, louée chaque année) | Roberto, des finances | [À CONFIRMER] | Chez le bureau d'enregistrement de l'école, nom [À CONFIRMER] |
| Février | Relire les six documents du dossier : noms, contacts, dates, accès, points [À CONFIRMER] restants | Denise Prado avec Márcia Okafor | aucun | Corriger, redater, redistribuer. Le document 5 seulement à ses destinataires. |

## À l'occasion

- Une étiquette est mal sortie ou n'est pas sortie : la réimprimer, d'une façon pas encore écrite [À CONFIRMER] (Denise Prado).
- Un nouveau compte administrateur dans Estante : le créer avec l'accord de Márcia Okafor (Denise Prado).
- Une personne nommée dans le dossier arrive ou part : Denise Prado met à jour les documents 2 et 5 le jour même.
- Un incident nouveau se produit : Denise Prado l'ajoute au document 4 et en retire un symptôme disparu, pour que le document reste sur une page.
- Installer une nouvelle version, avec l'accord prévu au document 2 (« Qui décide quoi »). D'abord une sauvegarde : lancer le script backup.sh (commandes à la fin). Ensuite : suivre les étapes de « Installer une nouvelle version » dans les commandes à la fin. Si la version apporte une migration (mise à jour de la façon dont les informations sont rangées), seulement avec Lucas Ferreira jusqu'au 31/01/2027. Vérifier que ça a marché : ouvrir https://estante.jacaranda.example.org et faire un prêt d'essai avec le livre « TESTE-0001 ». Si ça ne marche pas, revenir en arrière : la procédure n'est pas écrite [À CONFIRMER]. Si la nouvelle version a modifié les informations enregistrées, les remettre aussi depuis la sauvegarde.
- Restaurer une sauvegarde. Attention : cela remplace toutes les informations actuelles par celles de la sauvegarde, et tout ce qui a été saisi depuis est perdu. D'abord sauvegarder l'état actuel (lancer le script backup.sh), puis appeler Lucas Ferreira : la procédure n'est pas écrite, et jusqu'au 31/01/2027 cela se fait seulement avec lui [À CONFIRMER]. Dernière restauration prouvée : jamais testée, selon Lucas Ferreira [À CONFIRMER].

## Les commandes à coller

Cette partie s'adresse au référent technique. Les autres lecteurs peuvent passer.

Toutes les commandes se lancent sur le mini-PC ESTANTE01, après s'y être connecté par la connexion technique (SSH). Si le compte « denise » a le droit d'utiliser Docker et d'écrire dans /home/estante/backups : [À CONFIRMER].

```bash
# Se connecter au mini-PC depuis le réseau de l'école. (le mot de passe est dans le Bitwarden de l'école [À CONFIRMER])
ssh denise@192.168.0.20

# Vérifier que le programme tourne. Ne modifie rien. On doit voir : estante-db, estante-app et estante-caddy, chacun avec « Up »
docker ps --filter name=estante

# Vérifier que Docker redémarre seul après une coupure de courant. Ne modifie rien. On doit voir : enabled
systemctl is-enabled docker

# Voir les derniers messages du programme. Ne modifie rien. On ne doit pas voir : Traceback
docker logs --tail 50 estante-app

# Redémarrer le programme. Seulement si la vérification ci-dessus ne montre pas « Up ». Ensuite, refaire la vérification.
docker restart estante-db estante-app estante-caddy
```

```bash
# Faire une sauvegarde tout de suite. Ensuite, le fichier du jour doit apparaître dans la liste.
/home/estante/estante/scripts/backup.sh
ls -l /home/estante/backups | tail -3
```

```bash
# Import annuel. D'abord vérifier le format du fichier. Ne modifie rien. On doit voir le mot utf-8
file -i alunos.csv

# Seulement si utf-8 est apparu : importer. On doit voir le nombre d'élèves lus.
docker exec -i estante-app python scripts/importar_alunos.py < alunos.csv
```

Installer une nouvelle version (docs/deploy.md), avec l'accord de Márcia Okafor et après une sauvegarde :

1. Aller dans le dossier du code et télécharger la nouvelle version. L'origine de ce téléchargement n'est pas confirmée [À CONFIRMER].
2. Appliquer les nouvelles migrations, une par une, dans l'ordre des numéros (seulement avec Lucas Ferreira jusqu'au 31/01/2027).
3. Reconstruire et relancer le programme.
4. Refaire la vérification ci-dessus.
5. Faire un prêt d'essai avec le livre « TESTE-0001 ».

```bash
# Étape 1
cd /home/estante/estante && git pull

# Étape 2, une fois par nouvelle migration, en remplaçant 00X_nome.sql par le nom du fichier
docker exec -i estante-db sh -c 'psql -U "$POSTGRES_USER" -d "$POSTGRES_DB"' < migrations/00X_nome.sql

# Étape 3
docker compose -f deploy/docker-compose.yml up -d --build
```

---
Ce document fait partie du dossier de passation (6 documents). Une erreur ou un oubli ? Signalez-le à Denise Prado.
