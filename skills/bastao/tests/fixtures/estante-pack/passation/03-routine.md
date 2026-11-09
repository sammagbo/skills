# Estante : routine

Préparé le 09/11/2026 par Lucas Ferreira, pour Marcia Okafor, Paula Reis, Joana Lima et Denise Prado.

Notez chaque geste et chaque vérification dans le cahier de suivi. Lucas Ferreira ne connaît aucun cahier : l'endroit est [À CONFIRMER].

Écrivez la date, le geste, qui l'a fait et le résultat. C'est le même cahier que pour les incidents (document 4).

L'heure de la machine ESTANTE01 peut différer de l'heure de l'école. Le fuseau horaire de la machine est [À CONFIRMER]. Les heures ci-dessous sont celles de la machine.

## Ce qui se fait tout seul, et comment vérifier que ça s'est fait

| Quand | Ce qui se passe | Comment vérifier | Si ça ne s'est pas fait |
|---|---|---|---|
| 02:30, tous les jours | La machine copie les informations dans le dossier /home/estante/backups et supprime les copies de plus de 30 jours | Voir s'il existe un fichier estante avec la date du jour (commande dans « Les commandes à coller »). Le journal est dans /home/estante/backup.log | Faire la sauvegarde maintenant (voir « Les commandes à coller ») et prévenir Denise Prado, le référent technique |
| 07:00, du lundi au vendredi | Le programme envoie l'e-mail de rappel quand un livre a plus de 3 jours de retard | Le texte du programme ne garde pas de trace de cet envoi : la façon de vérifier est [À CONFIRMER] | Prévenir Denise Prado, le référent technique |

## Tous les jours

1. Vérifier que la sauvegarde du jour existe : commande dans « Les commandes à coller » ([À CONFIRMER], durée [À CONFIRMER]).
2. Ouvrir l'adresse https://estante.jacaranda.example.org et voir que la page s'affiche ([À CONFIRMER], durée [À CONFIRMER]).

Ces deux gestes sont une suggestion de ce dossier. Lucas Ferreira n'a convenu avec personne de qui les fait [À CONFIRMER].

## Toutes les semaines

Aucune tâche hebdomadaire, selon Lucas Ferreira.

## Tous les mois

1. Garder payé l'abonnement e-mail MailExemplo : l'abonnement est mensuel, sur la carte de l'école (Roberto, des finances). En 06/2026, la carte n'a pas payé et les rappels se sont arrêtés une semaine.

## Tous les ans

| Quand | Quoi | Qui | Délai de préparation | Comment |
|---|---|---|---|---|
| Février | Importer la liste des élèves, venue du secrétariat en CSV (tableau en texte). Le fichier doit être en UTF-8 (l'enregistrement des lettres accentuées) | Denise Prado [À CONFIRMER] | [À CONFIRMER] | Voir « Les commandes à coller ». Selon le commentaire du programme, les élèves absents de la liste deviennent inactifs [À CONFIRMER] |
| Au début de chaque semestre | Enregistrer les livres neufs et imprimer les étiquettes | Joana Lima | [À CONFIRMER] | [À CONFIRMER] |
| 14/03/2027 | Renouveler le domaine jacaranda.example.org, enregistré par l'école | Roberto, des finances, paie ; qui renouvelle [À CONFIRMER] | [À CONFIRMER] | Sur le site du registraire de domaines [À CONFIRMER] |
| Février, avec l'import | Relire les six documents du dossier : noms, contacts, dates, accès, points [À CONFIRMER] restants | Denise Prado, avec Marcia Okafor | aucun | Corriger, redater, redistribuer. Le document 5 seulement à ses destinataires. |

## À l'occasion

- Quelqu'un cité arrive ou part : Denise Prado met à jour les documents 2 et 5 le jour même.
- Un incident nouveau se produit : Denise Prado l'ajoute au document 4 et en retire un symptôme disparu. Le document reste sur une page.
- Installer une nouvelle version, avec l'accord de Marcia Okafor (document 2). Jusqu'en janvier 2027, l'étape 2 seulement après avoir parlé à Lucas Ferreira. Les étapes sont dans « Les commandes à coller ». D'abord, faire une sauvegarde.
- Vérifier la nouvelle version : ouvrir l'adresse du système et faire un prêt d'essai avec le livre « TESTE-0001 ».
- Revenir en arrière sur une nouvelle version : la procédure n'est pas écrite dans le texte du programme [À CONFIRMER]. N'effacez rien. Gardez la sauvegarde faite avant. Appelez Denise Prado, le référent technique.
- Si la nouvelle version a modifié les informations enregistrées, ne continuez pas seul. Voyez la restauration d'une sauvegarde, juste en dessous.
- D'où vient le nouveau code : Lucas Ferreira ne s'en souvient pas [À CONFIRMER]. Le programme n'a pas d'adresse distante, donc `git pull` (télécharger la nouvelle version) ne marche pas.
- Avant de restaurer une sauvegarde, sauvegarder l'état actuel : voir « Faire la sauvegarde maintenant ». La restauration remplace toutes les informations actuelles. Ce qui a été saisi depuis la sauvegarde restaurée est perdu.
- Restaurer une sauvegarde : jusqu'en janvier 2027, seulement après avoir parlé à Lucas Ferreira. Après cette date : [À CONFIRMER]. La procédure n'est pas écrite dans le texte du programme [À CONFIRMER]. Premier geste sûr : ne rien faire d'irréversible. Faites une nouvelle sauvegarde et écrivez à Denise Prado, le référent technique. Dernière restauration prouvée le [À CONFIRMER] : Lucas Ferreira croit qu'elle n'a jamais été testée.

## Les commandes à coller

Cette partie s'adresse au référent technique. Les autres lecteurs peuvent passer.

Les commandes tournent sur la machine ESTANTE01, dans le dossier /home/estante/estante. Denise Prado se connecte avec le compte denise : `ssh denise@192.168.0.20`.

Le mot de passe est dans le Bitwarden de l'école [À CONFIRMER]. Bitwarden est le programme où les mots de passe sont gardés.

Si le compte denise peut lancer les commandes ci-dessous : [À CONFIRMER]. Le texte du programme utilise le compte estante.

### Vérifier

```bash
# Vérifier que le programme tourne. Ne modifie rien.
# On doit voir : les trois parties estante-db, estante-app et estante-caddy, à l'état "Up" ou "running".
cd /home/estante/estante
docker compose -f deploy/docker-compose.yml ps

# Voir les derniers messages du programme. Ne modifie rien. On ne doit pas voir : Error ni Traceback.
cd /home/estante/estante
docker compose -f deploy/docker-compose.yml logs --tail 50 app

# Vérifier que Docker (le programme qui crée la boîte du système) démarre tout seul avec la machine. Ne modifie rien. On doit voir : enabled
systemctl is-enabled docker

# Vérifier que la sauvegarde du jour existe. Ne modifie rien.
# On doit voir : un fichier estante-AAAA-MM-JJ.dump avec la date du jour.
ls -l /home/estante/backups | tail -n 3

# Voir le journal de la dernière sauvegarde. Ne modifie rien.
tail -n 5 /home/estante/backup.log
```

### Redémarrer

Ne redémarrez que si la vérification ci-dessus ne montre pas « Up ». Ensuite, refaites la vérification.

```bash
# Redémarrer le programme.
cd /home/estante/estante
docker compose -f deploy/docker-compose.yml restart app
```

### Faire la sauvegarde maintenant

Vérifiez d'abord avec la dernière commande de « Vérifier ». Ensuite, lancez le bloc ci-dessous. Un nouveau fichier doit apparaître, avec la date du jour.

```bash
# Faire la sauvegarde maintenant. Crée un nouveau fichier.
cd /home/estante/estante
sh scripts/backup.sh
```

### Installer une nouvelle version

Faites la sauvegarde avant. Chaque bloc est une étape.

Étape 1 : le nouveau code doit être dans le dossier /home/estante/estante. La façon dont il arrive est [À CONFIRMER] : Lucas Ferreira ne s'en souvient pas.

Étape 2 : jusqu'en janvier 2027, seulement après avoir parlé à Lucas Ferreira. Appliquez chaque nouveau changement, dans l'ordre des numéros. Remplacez 00X_nome.sql par le nouveau fichier.

Lesquels sont déjà appliqués est [À CONFIRMER]. Denise Prado ou Lucas Ferreira le vérifient dans l'endroit des informations enregistrées, avant son départ.

```bash
# Appliquer un changement de la façon de ranger les informations (migration). On doit voir : aucune ligne avec ERROR.
cd /home/estante/estante
docker exec -i estante-db sh -c 'psql -U "$POSTGRES_USER" -d "$POSTGRES_DB"' < migrations/00X_nome.sql
```

Étape 3 : reconstruisez et relancez le programme. Ensuite, faites la vérification.

```bash
# Reconstruire et relancer le programme.
cd /home/estante/estante
docker compose -f deploy/docker-compose.yml up -d --build
```

### Importer la liste des élèves

En février. Vérifiez d'abord l'enregistrement du fichier. Le 19/02/2026, un fichier avec un autre enregistrement a créé 212 élèves en double.

```bash
# Vérifier le fichier. Ne modifie rien. On doit voir : utf-8 en fin de ligne.
file -i alunos.csv
```

Importez seulement si la vérification a montré utf-8. On doit voir : « N alunos lidos ».

Le texte du programme reçu compte seulement les lignes du fichier. Où est le programme qui importe vraiment : [À CONFIRMER] (question 18).

```bash
# Importer la liste des élèves.
cd /home/estante/estante
docker exec -i estante-app python scripts/importar_alunos.py < alunos.csv
```

---
Ce document fait partie du dossier de passation (6 documents). Une erreur ou un oubli ? Signalez-le à Denise Prado.
