# Estante : qui fait quoi

Préparé le 30/10/2026 par le développeur d'origine (nom [À CONFIRMER]), pour Marcia Okafor, Paula Reis, Joana Lima et Denise Prado.

## Les personnes

| Nom | Fonction | Rôle dans le système | Joignable par |
|---|---|---|---|
| Marcia Okafor | Directrice pédagogique | Propriétaire du système, à partir de décembre 2026 | [À CONFIRMER] |
| Denise Prado | Technicienne informatique de l'école | Référent technique | [À CONFIRMER] |
| Joana Lima | Bibliothécaire | Opérateur quotidien (bibliothèque, matin et après-midi) | [À CONFIRMER] |
| Paula Reis | Coordinatrice | Consultée sur les règles de la bibliothèque | [À CONFIRMER] |
| Roberto (nom de famille [À CONFIRMER]) | Service financier | Paie l'adresse du site et MailExemplo | [À CONFIRMER] |
| Nom [À CONFIRMER] | Développeur d'origine | Développeur d'origine, disponible jusqu'au 31/01/2027, par e-mail, gratuitement, pour des questions seulement, sans toucher au serveur | lucas.ferreira.dev@example.com |

## Qui décide quoi

| Décision | Qui décide | Qui doit être consulté avant | Qui est prévenu après |
|---|---|---|---|
| Changer une règle de fonctionnement | Marcia Okafor | Paula Reis | [À CONFIRMER] |
| Donner ou retirer un accès | Marcia Okafor | [À CONFIRMER] | [À CONFIRMER] |
| Installer une nouvelle version | Marcia Okafor | [À CONFIRMER] | [À CONFIRMER] |
| Renouveler une licence, un domaine, un contrat | Marcia Okafor | [À CONFIRMER] | [À CONFIRMER] |
| Arrêter le système, même temporairement | Marcia Okafor | [À CONFIRMER] | [À CONFIRMER] |

## Qui fait quoi, et quand

| Tâche | Responsable | Suppléant | Fréquence | Si personne ne le fait |
|---|---|---|---|---|
| Payer l'abonnement MailExemplo avec la carte de l'école | Roberto, service financier | [À CONFIRMER] | Chaque mois | MailExemplo bloque le compte et les e-mails de rappel s'arrêtent (une semaine en juin 2026) |
| Enregistrer les livres nouveaux et imprimer leurs étiquettes | Joana Lima | [À CONFIRMER] | Début de chaque semestre | Les livres nouveaux n'ont pas de code-barres à lire |
| Importer la liste des élèves du secrétariat | [À CONFIRMER] | [À CONFIRMER] | Chaque année, en février | Les nouveaux élèves ne sont pas dans le système |
| Relire le dossier de passation | Denise Prado, avec Marcia Okafor | [À CONFIRMER] | Chaque année, en février | Le dossier devient faux |
| Renouveler l'adresse jacaranda.example.org (registrador de domínios) | Roberto, service financier | [À CONFIRMER] | Chaque année, avant le 14/03/2027 | Le site ne s'ouvre plus à son adresse |

## Ce que chacun peut faire sans aide, et ce qui demande un accord

| Personne ou rôle | Peut faire sans aide | Avec l'accord du propriétaire | Jamais sans le référent technique ou le développeur |
|---|---|---|---|
| Denise Prado, référent technique | Redémarrer le programme, lire ses messages, lancer une sauvegarde à la main, réimprimer une étiquette | Installer une nouvelle version, créer un compte administrateur dans Estante | Jusqu'au 31/01/2027, jamais sans le développeur : modifier la façon dont les informations sont rangées (migrations), restaurer une sauvegarde. Après cette date : [À CONFIRMER] |
| Joana Lima, bibliothécaire | [À CONFIRMER] | [À CONFIRMER] | [À CONFIRMER] |
| Paula Reis, coordination | [À CONFIRMER] | [À CONFIRMER] | [À CONFIRMER] |

## Comptes et accès par rôle

| Rôle | Compte ou accès | Niveau | Gardé où |
|---|---|---|---|
| Référent technique (Denise Prado) | Compte personnel « denise » sur le mini-PC, créé en septembre 2026 | Connexion technique à la machine (niveau exact [À CONFIRMER]) | Bitwarden de l'école [À CONFIRMER] |
| Référent technique (Denise Prado) | Collection « Estante » du Bitwarden de l'école | Voit les mots de passe de la collection | Sans objet |
| Propriétaire du système (Marcia Okafor) | Organisation « Jacaranda TI » du Bitwarden | Administratrice | Sans objet |
| Opérateur quotidien (Joana Lima) | Compte dans Estante [À CONFIRMER] | [À CONFIRMER] | [À CONFIRMER] |
| Compte « estante » sur le mini-PC (partagé) | Compte qui fait tourner le programme et les tâches de nuit | [À CONFIRMER] | [À CONFIRMER] |
| Développeur d'origine | Accès au Bitwarden de l'école, autres accès [À CONFIRMER] | [À CONFIRMER] | Retiré à son départ, fin novembre 2026 |

## Quand quelqu'un part

- Si le développeur d'origine part (fin novembre 2026) : transférer l'emplacement du code source ([À CONFIRMER]) à Denise Prado. Changer son accès au Bitwarden et les mots de passe qu'il connaît : compte « estante », POSTGRES_PASSWORD, SECRET_KEY, SMTP_PASSWORD. Liste complète : [À CONFIRMER].
- Si Denise Prado part : transférer ce dossier et l'accès technique à [À CONFIRMER]. Changer son compte « denise », son accès à la collection « Estante » et le mot de passe du compte « estante ».
- Si Joana Lima part : transférer son compte dans Estante à [À CONFIRMER], et changer [À CONFIRMER].
- Si Marcia Okafor part : transférer l'administration du Bitwarden et le rôle de propriétaire à [À CONFIRMER], et changer [À CONFIRMER].

---
Ce document fait partie du dossier de passation (6 documents). Une erreur ou un oubli ? Signalez-le à Denise Prado.
