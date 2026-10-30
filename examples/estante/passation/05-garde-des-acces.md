# Estante : garde des accès

Préparé le 30/10/2026 par Lucas Ferreira, pour Márcia Okafor et Denise Prado seulement. Ne pas diffuser plus loin.

## Règles de garde

1. Chaque accès a un gardien nommé et un suppléant.
2. Les secrets vivent à un seul endroit de référence : le Bitwarden de l'école, organisation « Jacarandá TI » [À CONFIRMER] (un gestionnaire de mots de passe). Márcia Okafor administre l'organisation. Denise Prado a la collection « Estante ».
3. Quand une personne part, les accès qu'elle connaissait sont changés dans les [À CONFIRMER]. La liste est dans le document 2, « Quand quelqu'un part ».
4. Aucun secret par e-mail, par message ou dans un document partagé. Jamais dans ce dossier.
5. Un compte partagé (« admin », « root », le compte d'un équipement) n'est utilisé que si l'outil n'offre pas de comptes individuels. Il a quand même un gardien et un suppléant, il est gardé dans le Bitwarden de l'école [À CONFIRMER], et il est changé à chaque départ d'une personne qui le connaissait. Dans l'inventaire, ces comptes portent la mention « (partagé) ».

## Inventaire des accès

| Accès | À quoi il sert | Qui le détient | Suppléant | Gardé où |
|---|---|---|---|---|
| Serveur : connexion à la machine (mini-PC ESTANTE01, 192.168.0.20, salle de la coordination) | Connexion technique (SSH) pour vérifier, redémarrer et installer | Denise Prado (compte « denise », créé en 09/2026) ; Lucas Ferreira (compte « estante », à retirer au départ ; la sauvegarde et les rappels tournent dessus) | [À CONFIRMER] | Collection « Estante » du Bitwarden de l'école [À CONFIRMER] |
| Compte administrateur de l'application | Administrer Estante | Joana Lima (compte « joana ») ; Lucas Ferreira (compte « lucas », à retirer au départ) | [À CONFIRMER] | Bitwarden de l'école [À CONFIRMER] |
| Base de données : accès direct aux informations | Lire et modifier les informations enregistrées, sans passer par Estante | Qui se connecte au mini-PC : Denise Prado | [À CONFIRMER] | Fichier deploy/.env sur le mini-PC ; copie dans le Bitwarden : [À CONFIRMER] |
| Équipements (imprimante d'étiquettes Zebra GK420t) | Imprimer les étiquettes | Pas de mot de passe sur le panneau, selon Lucas Ferreira ; si quelqu'un l'a changé : [À CONFIRMER] (partagé) | [À CONFIRMER] | [À CONFIRMER] |
| Nom de domaine et certificat | Garder l'adresse jacaranda.example.org ; le cadenas du navigateur se renouvelle tout seul | Roberto, des finances, paie ; qui a le compte chez le bureau d'enregistrement : [À CONFIRMER] | [À CONFIRMER] | [À CONFIRMER] |
| E-mail biblioteca@jacaranda.example.org (MailExemplo) | Envoyer les e-mails de rappel | [À CONFIRMER] | [À CONFIRMER] | Mot de passe écrit en clair dans le code (voir SMTP_PASSWORD plus bas) |
| Espace où sont déposées les sauvegardes | Garder les copies de sauvegarde | Qui se connecte au mini-PC : Denise Prado | [À CONFIRMER] | /home/estante/backups, sur le mini-PC |
| Code source (origine du git pull sur le mini-PC [À CONFIRMER] ; copie dans /home/estante/estante) | Installer une nouvelle version | Lucas Ferreira | [À CONFIRMER] | [À CONFIRMER] |

Le routeur de l'école sert à fixer l'adresse de l'imprimante sur le réseau (192.168.0.50). Qui a l'accès, le suppléant et où il est gardé : [À CONFIRMER].

### Changer et récupérer

| Accès | Comment le changer | Si c'est perdu ou divulgué |
|---|---|---|
| Serveur | Chaque personne change le mot de passe de son propre compte sur le mini-PC ; le compte « estante » est désactivé une fois la sauvegarde et les rappels passés sur un autre compte [À CONFIRMER] | Se connecter au mini-PC avec un clavier et un écran, dans la salle de la coordination [À CONFIRMER] |
| Compte administrateur de l'application | Par un autre compte administrateur, avec l'accord de Márcia Okafor [À CONFIRMER] | Denise Prado crée un autre compte, avec l'accord de Márcia Okafor |
| Base de données | Avec Lucas Ferreira jusqu'au 31/01/2027 : le mot de passe est dans deploy/.env et dans DATABASE_URL [À CONFIRMER] | Changer le mot de passe et prévenir Márcia Okafor : la base contient des données personnelles des élèves |
| Équipements | [À CONFIRMER] | Etiquetas Exemplo [À CONFIRMER] |
| Nom de domaine et certificat | Sur le site du bureau d'enregistrement [À CONFIRMER] | Roberto, des finances, contacte le bureau d'enregistrement [À CONFIRMER] |
| E-mail biblioteca@ | Dans le panneau de MailExemplo, puis changer SMTP_PASSWORD sur le mini-PC [À CONFIRMER] | Changer le mot de passe tout de suite : quelqu'un peut envoyer des e-mails au nom de la bibliothèque |
| Espace des sauvegardes | Avec le serveur | Les sauvegardes contiennent des données personnelles des élèves : prévenir Márcia Okafor |

Pour le routeur de l'école et pour le code source, la façon de changer l'accès et ce qu'il faut faire s'il est perdu ne sont pas connues [À CONFIRMER].

## Paramètres sensibles du système (noms seulement)

Ce sont des réglages lus quand le programme démarre. Ici, seulement le nom. La valeur reste sur le mini-PC.

| Nom du paramètre | À quoi il sert | Où il est défini sur le serveur |
|---|---|---|
| POSTGRES_USER | Nom de l'utilisateur de la base de données | deploy/.env |
| POSTGRES_PASSWORD | Mot de passe de la base de données | deploy/.env |
| POSTGRES_DB | Nom de la base de données | deploy/.env |
| DATABASE_URL | Adresse que le programme utilise pour parler à la base, faite avec les trois précédents | deploy/docker-compose.yml |
| SECRET_KEY | Clé qui protège les sessions des personnes connectées à Estante | deploy/.env |
| SMTP_HOST | Serveur de l'e-mail MailExemplo | deploy/docker-compose.yml |
| SMTP_USER | Compte e-mail qui envoie les rappels | deploy/docker-compose.yml |
| SMTP_PASSWORD | Mot de passe de ce compte e-mail. Il est écrit en clair dans le fichier : point ouvert du document 6 | deploy/docker-compose.yml |
| PRINTER_URL | Adresse de l'imprimante d'étiquettes sur le réseau | deploy/.env |
| TZ | Fuseau horaire du programme (heure de Brasília) | deploy/docker-compose.yml |
| ADMIN_EMAIL | Figure dans le fichier d'exemple, mais aucune partie du programme ne l'utilise [À CONFIRMER] | deploy/.env.example |

## Sauvegardes

- Où : /home/estante/backups, sur le mini-PC ESTANTE01 lui-même.
- À quelle fréquence : tous les jours à 02:30, à l'heure du mini-PC.
- Conservées pendant : 30 jours.
- Copie hors du serveur : peut-être un disque dur externe, copié de temps en temps par Denise Prado [À CONFIRMER]. Chiffrée : non, selon Lucas Ferreira [À CONFIRMER].
- Dernière restauration prouvée : jamais testée, selon Lucas Ferreira [À CONFIRMER].
- Qui sait restaurer : Lucas Ferreira, jusqu'au 31/01/2027 [À CONFIRMER]. La procédure est dans le document 3, « À l'occasion ».
- Qui peut lire une sauvegarde (elle contient des informations personnelles) : qui se connecte au mini-PC, aujourd'hui Denise Prado et Lucas Ferreira. Qui lit le fichier /home/estante/backup.log : [À CONFIRMER].

## Prochaines échéances liées aux accès

| Date | Quoi (certificat, domaine, licence, mot de passe à renouveler) | Qui |
|---|---|---|
| Fin 11/2026 | Retirer les comptes de Lucas Ferreira et changer les mots de passe qu'il connaissait | Denise Prado |
| Chaque mois | Paiement de MailExemplo, sur la carte de l'école | Roberto, des finances |
| 31/01/2027 | Fin de la disponibilité de Lucas Ferreira | Márcia Okafor |
| 14/03/2027 | Renouvellement du domaine jacaranda.example.org | Roberto, des finances |
| Automatique | Certificat du cadenas, renouvelé tout seul | Personne |

---
Ce document fait partie du dossier de passation (6 documents). Une erreur ou un oubli ? Signalez-le à Denise Prado.
