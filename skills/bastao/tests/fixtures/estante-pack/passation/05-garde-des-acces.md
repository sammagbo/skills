# Estante : garde des accès

Préparé le 09/11/2026 par Lucas Ferreira, pour le propriétaire, Marcia Okafor, et le référent technique, Denise Prado, seulement. Ne pas diffuser plus loin.

## Règles de garde

1. Chaque accès a un gardien nommé et un suppléant.
2. Les secrets vivent à un seul endroit de référence : le Bitwarden de l'école, organisation Jacaranda TI [À CONFIRMER]. C'est le programme où les mots de passe sont gardés.
3. Quand une personne part, les accès qu'elle connaissait sont changés dans les [À CONFIRMER]. La liste est dans le document 2, « Quand quelqu'un part ».
4. Aucun secret par e-mail, par message ou dans un document partagé. Jamais dans ce dossier.
5. Un compte partagé (« admin », « root », le compte d'un équipement) n'est utilisé que s'il n'existe pas de comptes individuels. Il a un gardien et un suppléant, et il est changé à chaque départ d'une personne qui le connaissait. Il est gardé dans le Bitwarden de l'école [À CONFIRMER] et porte dans l'inventaire la mention « (partagé) ».

## Inventaire des accès

| Accès | À quoi il sert | Qui le détient | Suppléant | Gardé où |
|---|---|---|---|---|
| Serveur : connexion technique (SSH) à la machine ESTANTE01. Compte denise, créé en septembre. Compte estante (partagé [À CONFIRMER]) | Installer des versions, voir les messages, faire des sauvegardes | Denise Prado (compte denise). Lucas Ferreira a l'accès aujourd'hui et sera retiré quand il partira. Compte estante : [À CONFIRMER] | [À CONFIRMER] | Le Bitwarden de l'école [À CONFIRMER] |
| Bitwarden de l'école, organisation Jacaranda TI, collection Estante [À CONFIRMER] | Garder les mots de passe de ce système | Marcia Okafor (administratrice). Denise Prado (voit la collection Estante). Lucas Ferreira a l'accès aujourd'hui et sera retiré quand il partira [À CONFIRMER] | [À CONFIRMER] | Le Bitwarden de l'école [À CONFIRMER] |
| Compte administrateur du programme : comptes joana et lucas (le compte lucas doit être désactivé) | Administrer le programme | Joana Lima (compte joana). Lucas Ferreira (compte lucas) | [À CONFIRMER] | Le Bitwarden de l'école [À CONFIRMER] |
| Base de données : accès direct aux informations (POSTGRES_USER et POSTGRES_PASSWORD) | Appliquer des changements et restaurer des sauvegardes | [À CONFIRMER] | [À CONFIRMER] | [À CONFIRMER] |
| Équipements (imprimante Zebra d'étiquettes) | Imprimer les étiquettes des livres neufs | [À CONFIRMER] | [À CONFIRMER] | Le panneau de l'imprimante n'avait pas de mot de passe. Lucas Ferreira ne sait pas si quelqu'un l'a changé [À CONFIRMER] |
| Compte e-mail biblioteca@jacaranda.example.org, chez MailExemplo (abonnement mensuel sur la carte de l'école) | Envoyer les rappels aux responsables | [À CONFIRMER]. Roberto, des finances, s'occupe du paiement | [À CONFIRMER] | Écrit sans protection dans le dépôt, l'endroit où le texte du programme est gardé (document 6) |
| Nom de domaine jacaranda.example.org et certificat | Garder l'adresse du système. Caddy renouvelle le certificat tout seul | [À CONFIRMER]. Roberto, des finances, s'occupe du paiement | [À CONFIRMER] | [À CONFIRMER] |
| Espace où sont déposées les sauvegardes : dossier /home/estante/backups, sur la machine | Garder les sauvegardes de 30 jours | [À CONFIRMER] | [À CONFIRMER] | Sur la machine ESTANTE01 |
| Code source (sans adresse distante ; copie sur la machine, dossier /home/estante/estante) | Installer de nouvelles versions | [À CONFIRMER] | [À CONFIRMER] | Sur la machine ESTANTE01 |

### Changer et récupérer

Lucas Ferreira part fin novembre 2026. Désactiver le compte lucas du programme. Retirer son accès à la machine et au Bitwarden de l'école [À CONFIRMER].

À définir avec le propriétaire [À CONFIRMER] : comment changer chaque autre accès, et que faire s'il est perdu ou divulgué. Rien de cela n'est écrit dans le dépôt.

## Paramètres sensibles du système (noms seulement)

| Nom du paramètre | À quoi il sert | Où il est défini sur le serveur |
|---|---|---|
| POSTGRES_USER | Nom du compte de la base de données | Fichier deploy/.env (non ouvert) |
| POSTGRES_PASSWORD | Mot de passe du compte de la base de données | Fichier deploy/.env (non ouvert) |
| POSTGRES_DB | Nom de la base de données | Fichier deploy/.env (non ouvert) |
| DATABASE_URL | Adresse que le programme utilise pour parler à la base, construite avec les trois noms ci-dessus | deploy/docker-compose.yml |
| SECRET_KEY | Clé interne du programme [À CONFIRMER] | Fichier deploy/.env (non ouvert) |
| SMTP_HOST | Machine qui envoie les e-mails | deploy/docker-compose.yml |
| SMTP_USER | Compte e-mail qui envoie les rappels | deploy/docker-compose.yml |
| SMTP_PASSWORD | Mot de passe de ce compte e-mail. La valeur est écrite sans protection dans le fichier ci-contre : document 6 | deploy/docker-compose.yml |
| PRINTER_URL | Adresse de l'imprimante d'étiquettes | Fichier deploy/.env (non ouvert) |
| TZ | Fuseau horaire du programme | deploy/docker-compose.yml |
| ADMIN_EMAIL | E-mail de l'administrateur. Le dépôt ne montre pas où il est utilisé [À CONFIRMER] | Fichier deploy/.env (non ouvert) |

## Sauvegardes

- Où : sur la machine ESTANTE01, dossier /home/estante/backups.
- À quelle fréquence : tous les jours à 02:30.
- Conservées pendant : 30 jours.
- Copie hors du serveur : Lucas Ferreira croit que Denise Prado copie parfois sur un disque externe, mais il ne sait pas [À CONFIRMER]. Chiffrée : non, dit Lucas Ferreira [À CONFIRMER].
- Dernière restauration prouvée : le [À CONFIRMER], par [À CONFIRMER]. Lucas Ferreira croit qu'elle n'a jamais été testée [À CONFIRMER].
- Qui sait restaurer : [À CONFIRMER]. Jusqu'en janvier 2027, seulement après avoir parlé à Lucas Ferreira. La procédure est dans le document 3, « À l'occasion ».
- Qui peut lire une sauvegarde (elle contient des informations personnelles) : [À CONFIRMER].

## Prochaines échéances liées aux accès

| Date | Quoi (certificat, domaine, licence, mot de passe à renouveler) | Qui |
|---|---|---|
| Fin novembre 2026 | Départ de Lucas Ferreira : désactiver le compte lucas et retirer ses accès | [À CONFIRMER] |
| 31/01/2027 | Fin de l'aide de Lucas Ferreira, pour des questions seulement, par e-mail | [À CONFIRMER] |
| 14/03/2027 | Renouvellement du domaine jacaranda.example.org | Roberto, des finances, paie ; qui renouvelle [À CONFIRMER] |
| Chaque mois | Abonnement e-mail MailExemplo, sur la carte de l'école | Roberto, des finances |
| [À CONFIRMER] | Batterie de l'onduleur, changée en 2024 | [À CONFIRMER] |

---
Ce document fait partie du dossier de passation (6 documents). Une erreur ou un oubli ? Signalez-le à Denise Prado.
