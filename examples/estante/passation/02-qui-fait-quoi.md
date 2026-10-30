# Estante : qui fait quoi

Préparé le 30/10/2026 par Lucas Ferreira, pour Márcia Okafor, Paula Reis, Joana Lima et Denise Prado.

## Les personnes

| Nom | Fonction | Rôle dans le système | Joignable par |
|---|---|---|---|
| Márcia Okafor | Directrice pédagogique | Propriétaire du système | [À CONFIRMER] |
| Denise Prado | Technicienne informatique de l'école | Référent technique | denise.prado@jacaranda.example.org, du lundi au mercredi, de 8 h à 12 h |
| Joana Lima | Bibliothécaire | Opérateur quotidien (bibliothèque) | [À CONFIRMER] |
| Paula Reis | Coordination | Consultée sur les règles de la bibliothèque | [À CONFIRMER] |
| Roberto (nom de famille [À CONFIRMER]) | Service financier | Paie le domaine et l'e-mail MailExemplo | [À CONFIRMER] |
| Lucas Ferreira | Développeur | Développeur d'origine, disponible jusqu'au 31/01/2027, gratuitement, seulement pour des questions, sans toucher au serveur | lucas.ferreira.dev@example.com |

## Qui décide quoi

| Décision | Qui décide | Qui doit être consulté avant | Qui est prévenu après |
|---|---|---|---|
| Changer une règle de fonctionnement | Márcia Okafor | Paula Reis, si c'est une règle de la bibliothèque | [À CONFIRMER] |
| Donner ou retirer un accès | Márcia Okafor | [À CONFIRMER] | [À CONFIRMER] |
| Installer une nouvelle version | Márcia Okafor | [À CONFIRMER] | [À CONFIRMER] |
| Renouveler une licence, un domaine, un contrat | Márcia Okafor | [À CONFIRMER] | [À CONFIRMER] |
| Arrêter le système, même temporairement | Márcia Okafor | [À CONFIRMER] | [À CONFIRMER] |

## Qui fait quoi, et quand

| Tâche | Responsable | Suppléant | Fréquence | Si personne ne le fait |
|---|---|---|---|---|
| Vérifier le matin qu'Estante s'ouvre | [À CONFIRMER] (décision de Márcia Okafor) | [À CONFIRMER] | Tous les jours | Un problème n'apparaît que quand quelqu'un se plaint. En 06/2026, les rappels se sont arrêtés une semaine. |
| Payer l'e-mail MailExemplo | Roberto, des finances | [À CONFIRMER] | Chaque mois | Les rappels s'arrêtent |
| Enregistrer les livres neufs et imprimer les étiquettes | Joana Lima | [À CONFIRMER] | Début de chaque semestre | Les livres neufs n'ont pas de code-barres pour le prêt |
| Demander au secrétariat le fichier des élèves | [À CONFIRMER] | [À CONFIRMER] | Chaque année, avant février | L'import de février ne peut pas se faire |
| Importer la liste annuelle des élèves | Denise Prado | [À CONFIRMER] | Chaque année, en février | Les nouveaux élèves n'existent pas dans Estante, et ceux qui sont partis restent actifs |
| Renouveler le domaine jacaranda.example.org | Roberto, des finances | [À CONFIRMER] | Chaque année, avant le 14/03 | Le site ne s'ouvre plus |
| Relire le dossier | Denise Prado avec Márcia Okafor | [À CONFIRMER] | Chaque année, en février | Le dossier garde des noms et des dates faux |

## Ce que chacun peut faire sans aide, et ce qui demande un accord

| Personne ou rôle | Peut faire sans aide | Avec l'accord du propriétaire | Jamais sans le référent technique ou le développeur |
|---|---|---|---|
| Référent technique (Denise Prado) | Redémarrer le programme, lire les messages du programme, faire une sauvegarde tout de suite, réimprimer une étiquette | Installer une nouvelle version, créer un compte administrateur | Jusqu'au 31/01/2027, jamais sans Lucas Ferreira : toucher aux migrations (la façon dont les informations sont rangées) et restaurer une sauvegarde |

À définir avec Márcia Okafor : ce que Joana Lima peut faire seule, par exemple allumer l'onduleur ou redémarrer le mini-PC [À CONFIRMER].

## Comptes et accès par rôle

| Rôle | Compte ou accès | Niveau | Gardé où |
|---|---|---|---|
| Propriétaire du système | Bitwarden de l'école, organisation « Jacarandá TI » | Administre le gestionnaire de mots de passe | Bitwarden de l'école [À CONFIRMER] |
| Référent technique | Compte « denise » sur le mini-PC, créé en 09/2026 | Connexion technique à la machine (SSH) | Collection « Estante » du Bitwarden de l'école [À CONFIRMER] |
| Opérateur quotidien | Compte « joana » dans Estante | Administrateur de l'application | Bitwarden de l'école [À CONFIRMER] |
| Développeur d'origine | Compte « estante » sur le mini-PC, compte « lucas » dans Estante, accès au Bitwarden | Tout | À retirer au départ, fin 11/2026 |

## Quand quelqu'un part

- Si Lucas Ferreira part (fin 11/2026) : transférer la sauvegarde et les rappels, qui tournent sur son compte « estante », vers un compte de l'école [À CONFIRMER]. Changer le compte « lucas » dans Estante, le compte « estante » sur le mini-PC, son accès au Bitwarden et les mots de passe qu'il connaissait (document 5).
- Si Denise Prado part : transférer le compte « denise » et la collection « Estante » du Bitwarden à [À CONFIRMER], et changer les mots de passe du mini-PC et de la base de données.
- Si Joana Lima part : transférer les tâches de la bibliothèque à [À CONFIRMER], et changer le compte « joana » dans Estante.

---
Ce document fait partie du dossier de passation (6 documents). Une erreur ou un oubli ? Signalez-le à Denise Prado.
