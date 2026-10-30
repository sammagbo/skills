# Estante : routine

Préparé le 30/10/2026 par le développeur d'origine (nom [À CONFIRMER]), pour Denise Prado et Joana Lima (celles et ceux qui font tourner le système au quotidien).

Chaque geste fait et chaque vérification sont notés dans le cahier de bord [À CONFIRMER] : la date, le geste, qui l'a fait, le résultat. C'est le même cahier que pour les incidents (document 4).

## Ce qui se fait tout seul, et comment vérifier que ça s'est fait

Les heures sont celles de l'horloge du mini-PC. Son fuseau horaire n'a jamais été vérifié [À CONFIRMER]. Le programme lui-même a son propre réglage d'heure (paramètre TZ, document 5).

| Quand | Ce qui se passe | Comment vérifier | Si ça ne s'est pas fait |
|---|---|---|---|
| Chaque nuit à 02:30 (heure du mini-PC) | Sauvegarde des informations dans /home/estante/backups. Les copies de plus de 30 jours sont effacées. | Un fichier estante-AAAA-MM-JJ.dump à la date du jour est dans /home/estante/backups. Les erreurs sont dans /home/estante/backup.log. | Denise Prado lance une sauvegarde à la main (voir « À l'occasion »). |
| Du lundi au vendredi à 07:00 (heure du mini-PC) | Envoi d'un e-mail aux familles de chaque élève qui a un livre en retard de plus de 3 jours | [À CONFIRMER] : cette tâche n'écrit dans aucun fichier de suivi | Document 4, « Les familles ne reçoivent plus les e-mails de rappel » |

## Tous les jours

Aucun geste à la main connu au 30/10/2026. La vérification que le programme tourne est dans « Les commandes à coller ».

## Toutes les semaines

Aucun geste connu au 30/10/2026.

## Tous les mois

Aucun geste connu au 30/10/2026. L'abonnement MailExemplo est payé chaque mois avec la carte de l'école (Roberto, service financier). En juin 2026, un paiement manqué a arrêté les e-mails pendant une semaine.

## Tous les ans

| Quand | Quoi | Qui | Délai de préparation | Comment |
|---|---|---|---|---|
| Février | Importer la liste des élèves | [À CONFIRMER] | [À CONFIRMER] | Demander au secrétariat le fichier CSV (un tableau en texte) des élèves. Vérifier qu'il est enregistré en UTF-8. Faire une sauvegarde (voir « À l'occasion »). Lancer `docker exec -i estante-app python scripts/importar_alunos.py < alunos.csv`. Vérifier que le nombre affiché (« N alunos lidos ») est le nombre de lignes du fichier. Les élèves absents du fichier passent en inactif, ils ne sont pas effacés. |
| Début de chaque semestre | Enregistrer les livres nouveaux et imprimer leurs étiquettes | Joana Lima | [À CONFIRMER] | Écrans et boutons : [À CONFIRMER]. L'imprimante est la Zebra GK420t de la bibliothèque, à l'adresse 192.168.0.50. |
| Avant le 14/03/2027 | Renouveler l'adresse jacaranda.example.org au registrador de domínios | Roberto, service financier | [À CONFIRMER] | Dans l'espace client du registrador de domínios. Qui y a accès : [À CONFIRMER]. |
| Février | Relire les six documents du dossier : noms, contacts, dates, accès, points [À CONFIRMER] restants | Denise Prado, avec Marcia Okafor | aucun | Corriger, redater, redistribuer. Le document 5 seulement à ses destinataires. |

## À l'occasion

- Créer un compte administrateur dans Estante : avec l'accord de Marcia Okafor, comment exactement [À CONFIRMER] (Denise Prado).
- Après une longue coupure de courant : quand le courant revient, vérifier que le programme tourne (« Les commandes à coller »). Docker (le logiciel qui fait tourner les boîtes du programme) démarre seul avec la machine depuis le 11/03/2025 (Denise Prado).
- Une personne nommée dans le dossier arrive ou part : Denise Prado met à jour les documents 2 et 5 le jour même.
- Un incident nouveau se produit : Denise Prado l'ajoute au document 4 et en retire un symptôme disparu, pour que le document reste sur une page.
- Installer une nouvelle version, avec l'accord prévu au document 2 (« Qui décide quoi »). D'abord une sauvegarde : lancer `/home/estante/estante/scripts/backup.sh` sur le mini-PC (quel compte en a le droit : [À CONFIRMER]). Vérifier qu'un fichier à la date du jour est apparu dans /home/estante/backups. Ensuite : se connecter au mini-PC (192.168.0.20) avec son compte et aller dans /home/estante/estante. Récupérer la nouvelle version (d'où : [À CONFIRMER], le dépôt n'a pas d'adresse distante). Appliquer dans l'ordre les migrations nouvelles (mises à jour de la façon dont les informations sont rangées) : `docker exec -i estante-db psql -U estante -d estante < migrations/00X_nom.sql`. Puis lancer `docker compose -f deploy/docker-compose.yml up -d --build`. Jusqu'au 31/01/2027, les migrations seulement avec le développeur. Vérifier que ça a marché : ouvrir estante.jacaranda.example.org et faire un prêt de test avec le livre « TESTE-0001 ». Si ça ne marche pas, revenir en arrière : [À CONFIRMER]. Si la nouvelle version a modifié les informations enregistrées, les remettre aussi depuis la sauvegarde.
- Restaurer une sauvegarde. Attention : cela remplace toutes les informations actuelles par celles de la sauvegarde, et tout ce qui a été saisi depuis est perdu. D'abord sauvegarder l'état actuel (lancer `/home/estante/estante/scripts/backup.sh` et vérifier le nouveau fichier), puis [À CONFIRMER] : le dépôt ne contient aucune procédure de restauration. Jusqu'au 31/01/2027, jamais sans le développeur. Dernière restauration prouvée le [À CONFIRMER].

## Les commandes à coller

Cette partie s'adresse au référent technique. Les autres lecteurs peuvent passer.

```bash
# Vérifier que le programme tourne. Ne modifie rien. On doit voir : trois lignes, estante-app, estante-db et estante-caddy, chacune avec « Up »
docker ps --filter name=estante

# Voir les derniers messages du programme. Ne modifie rien. On ne doit pas voir : Traceback ou Error
docker logs --tail 50 estante-app

# Redémarrer le programme. Seulement si la vérification ci-dessus ne montre pas les trois lignes avec « Up ». Ensuite, refaire la vérification.
docker compose -f /home/estante/estante/deploy/docker-compose.yml restart
```

---
Ce document fait partie du dossier de passation (6 documents). Une erreur ou un oubli ? Signalez-le à Denise Prado.
