# Estante : garde des accès

Préparé le 30/10/2026 par le développeur d'origine (nom [À CONFIRMER]), pour Marcia Okafor et Denise Prado seulement. Ne pas diffuser plus loin.

## Règles de garde

1. Chaque accès a un gardien nommé et un suppléant.
2. Les secrets vivent à un seul endroit de référence : le Bitwarden de l'école, organisation « Jacaranda TI » [À CONFIRMER]. Le développeur l'a indiqué. Marcia Okafor doit le confirmer de vive voix.
3. Quand une personne part, les accès qu'elle connaissait sont changés dans les [À CONFIRMER]. La liste est dans le document 2, « Quand quelqu'un part ».
4. Aucun secret par e-mail, par message ou dans un document partagé. Jamais dans ce dossier.
5. Un compte partagé (« admin », « root », le compte d'un équipement) n'est utilisé que si l'outil n'offre pas de comptes individuels. Il a quand même un gardien et un suppléant, il est gardé dans le Bitwarden de l'école [À CONFIRMER], et il est changé à chaque départ d'une personne qui le connaissait. Dans l'inventaire, ces comptes portent la mention « (partagé) ».

## Inventaire des accès

| Accès | À quoi il sert | Qui le détient | Suppléant | Gardé où |
|---|---|---|---|---|
| Serveur : connexion à la machine (mini-PC ESTANTE01, adresse 192.168.0.20) | Entrer dans la machine pour vérifier, redémarrer, sauvegarder, installer | Denise Prado (compte « denise »). Compte « estante » (partagé) : [À CONFIRMER] | [À CONFIRMER] | Bitwarden de l'école [À CONFIRMER] |
| Bitwarden de l'école, organisation « Jacaranda TI » | Garder les mots de passe | Marcia Okafor, administratrice. Denise Prado voit la collection « Estante ». Le développeur y a accès jusqu'à son départ, fin novembre 2026. | [À CONFIRMER] | Sans objet |
| Compte administrateur de l'application | Créer des comptes dans Estante | [À CONFIRMER] | [À CONFIRMER] | [À CONFIRMER] |
| Base de données : accès direct aux informations | Lire ou corriger les informations sans passer par l'écran | Denise Prado, par le mini-PC [À CONFIRMER] | [À CONFIRMER] | Fichier deploy/.env sur le mini-PC |
| Équipements (imprimante Zebra GK420t, lecteurs de code-barres et de cartes) | Imprimer les étiquettes, lire les livres et les cartes | [À CONFIRMER] | [À CONFIRMER] | [À CONFIRMER] |
| Routeur de l'école | Garde l'adresse fixe 192.168.0.50 de l'imprimante | [À CONFIRMER] | [À CONFIRMER] | [À CONFIRMER] |
| Nom de domaine et certificat | Adresse jacaranda.example.org au registrador de domínios. Le certificat (le cadenas du navigateur) se renouvelle seul. | Roberto, service financier | [À CONFIRMER] | [À CONFIRMER] |
| Compte MailExemplo (envoi des e-mails) | Envoyer les rappels aux familles | Roberto, service financier, pour le paiement | [À CONFIRMER] | Mot de passe écrit en clair dans le dépôt : point à régler, document 6 |
| Internet (Provedor Exemplo) | La connexion de l'école | Secrétariat, qui a le contrat | [À CONFIRMER] | [À CONFIRMER] |
| Espace où sont déposées les sauvegardes | Garder les copies des informations | Denise Prado, par le mini-PC [À CONFIRMER] | [À CONFIRMER] | /home/estante/backups sur le mini-PC. Disque dur externe : [À CONFIRMER] |
| Code source ([À CONFIRMER] ; une copie est sur le mini-PC, dans /home/estante/estante) | Modifier ou réinstaller le programme | Le développeur d'origine | Denise Prado [À CONFIRMER] | [À CONFIRMER] |

### Changer et récupérer

| Accès | Comment le changer | Si c'est perdu ou divulgué |
|---|---|---|
| Serveur | Sur le mini-PC, changer le mot de passe du compte (commande passwd) ou supprimer le compte. Le nouveau mot de passe va dans le Bitwarden de l'école [À CONFIRMER]. | Changer tout de suite le mot de passe du compte concerné. Prévenir Marcia Okafor. |
| Bitwarden de l'école | Marcia Okafor retire ou ajoute la personne dans l'organisation | [À CONFIRMER] |
| Compte administrateur de l'application | [À CONFIRMER] | [À CONFIRMER] |
| Base de données | [À CONFIRMER] : changer POSTGRES_PASSWORD demande aussi de le changer dans la base. Jusqu'au 31/01/2027, avec le développeur. | [À CONFIRMER] |
| Équipements | [À CONFIRMER] | [À CONFIRMER] |
| Routeur de l'école | [À CONFIRMER] | [À CONFIRMER] |
| Nom de domaine et certificat | [À CONFIRMER] | [À CONFIRMER] |
| Compte MailExemplo | Changer le mot de passe dans MailExemplo, le garder dans le Bitwarden de l'école [À CONFIRMER], et le retirer du fichier docker-compose.yml | Le mot de passe actuel est déjà lisible par toute personne qui a le code : le changer avant la signature du document 6 |
| Internet (Provedor Exemplo) | [À CONFIRMER] | [À CONFIRMER] |
| Espace des sauvegardes | Mêmes accès que le serveur | Une sauvegarde contient les données des élèves : prévenir Marcia Okafor |
| Code source | [À CONFIRMER] | [À CONFIRMER] |

## Paramètres sensibles du système (noms seulement)

Un paramètre est un réglage lu au démarrage du programme. Ici, seulement son nom. La valeur est gardée sur le mini-PC.

| Nom du paramètre | À quoi il sert | Où il est défini sur le serveur |
|---|---|---|
| POSTGRES_USER | Nom du compte de la base de données | deploy/.env |
| POSTGRES_PASSWORD | Mot de passe de la base de données | deploy/.env |
| POSTGRES_DB | Nom de la base de données | deploy/.env |
| DATABASE_URL | Adresse complète de la base pour le programme, construite à partir des trois réglages ci-dessus | deploy/docker-compose.yml |
| SECRET_KEY | Clé qui protège les sessions des personnes connectées | deploy/.env |
| SMTP_HOST | Serveur d'envoi des e-mails (MailExemplo) | deploy/docker-compose.yml, écrit en clair |
| SMTP_USER | Compte d'envoi des e-mails | deploy/docker-compose.yml, écrit en clair |
| SMTP_PASSWORD | Mot de passe du compte d'envoi des e-mails | deploy/docker-compose.yml, écrit en clair : point à régler, document 6 |
| PRINTER_URL | Adresse de l'imprimante d'étiquettes sur le réseau | deploy/.env |
| TZ | Fuseau horaire du programme (pas celui du mini-PC) | deploy/docker-compose.yml |
| ADMIN_EMAIL | [À CONFIRMER] : présent dans deploy/.env.example, mais le programme ne le lit pas | deploy/.env [À CONFIRMER] |

## Sauvegardes

- Où : /home/estante/backups, sur le mini-PC lui-même.
- À quelle fréquence : chaque nuit à 02:30 (heure du mini-PC).
- Conservées pendant : 30 jours.
- Copie hors du serveur : [À CONFIRMER] (le développeur pense que Denise Prado copie parfois sur un disque dur externe, sans certitude). Chiffrée : [À CONFIRMER] (selon le développeur, non).
- Dernière restauration prouvée : le [À CONFIRMER], par [À CONFIRMER]. Selon le développeur, aucune restauration n'a jamais été testée.
- Qui sait restaurer : personne ne l'a prouvé [À CONFIRMER]. La procédure est dans le document 3, « À l'occasion ».
- Qui peut lire une sauvegarde (elle contient des informations personnelles) : [À CONFIRMER].

## Prochaines échéances liées aux accès

| Date | Quoi (certificat, domaine, licence, mot de passe à renouveler) | Qui |
|---|---|---|
| Avant la signature du document 6 | Changer SMTP_PASSWORD (écrit en clair dans le dépôt) | Denise Prado [À CONFIRMER] |
| Fin novembre 2026 (date exacte [À CONFIRMER]) | Retirer l'accès du développeur au Bitwarden et changer les mots de passe qu'il connaît | Marcia Okafor |
| 31/01/2027 | Fin de la disponibilité du développeur par e-mail | Marcia Okafor |
| Chaque mois | Abonnement MailExemplo | Roberto, service financier |
| 14/03/2027 | Adresse jacaranda.example.org au registrador de domínios | Roberto, service financier |
| [À CONFIRMER] | Batterie de l'onduleur APC, changée en 2024 | [À CONFIRMER] |
| [À CONFIRMER] | Contrat internet Provedor Exemplo | Secrétariat |

---
Ce document fait partie du dossier de passation (6 documents). Une erreur ou un oubli ? Signalez-le à Denise Prado.
