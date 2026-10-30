# Estante : ce que c'est et ce que ça ne fait pas

Préparé le 30/10/2026 par Lucas Ferreira, pour Márcia Okafor, Paula Reis, Joana Lima et Denise Prado.

## En une phrase

Estante sert à enregistrer les prêts de la bibliothèque. Qui l'utilise : Joana Lima, bibliothécaire.

## Ce que ça fait

- Enregistre prêts et retours par code-barres. Utilisé par Joana Lima, tous les jours.
- Écrit aux responsables après 3 jours de retard. Tout seul, à 07:00, en semaine.
- Imprime les étiquettes des livres neufs. Utilisé par Joana Lima, chaque semestre.
- Reçoit la liste des élèves. Utilisé par Denise Prado, en février.

## Ce que ça ne fait pas

- N'empêche pas un livre de sortir : pas de portique antivol, même si l'école le croit.
- N'envoie ni SMS ni WhatsApp.
- Ne calcule pas d'amende : elle a été désactivée en 2025.
- Ne se relie pas au logiciel du secrétariat.

## Où ça tourne

- Le programme tourne sur le mini-PC ESTANTE01, en salle de coordination, en trois parties : estante-app (le programme), estante-db (les données) et estante-caddy (le cadenas).
- On y accède par le navigateur, à https://estante.jacaranda.example.org.
- Il dépend d'internet, de MailExemplo (e-mail) et de l'imprimante.
- Les informations restent sur le mini-PC, copiées à 02:30.

## Qui en est responsable

| Rôle | Nom et fonction | Ce que cette personne décide ou fait |
|---|---|---|
| Propriétaire du système | Márcia Okafor, directrice pédagogique | Décide des changements et des renouvellements |
| Référent technique | Denise Prado, technicienne informatique | Première personne à appeler |
| Développeur d'origine | Lucas Ferreira | Questions par e-mail, jusqu'au 31/01/2027 |

## Ce qui a une date

| Échéance | Quoi | Qui s'en occupe | Si c'est oublié |
|---|---|---|---|
| Chaque mois | Paiement de MailExemplo | Roberto, des finances | Les rappels s'arrêtent |
| 14/03/2027 | Domaine jacaranda.example.org | Roberto, des finances | Le site ne s'ouvre plus |
| [À CONFIRMER] | Batterie de l'onduleur (de 2024) | [À CONFIRMER] | Le mini-PC s'éteint en cas de coupure |

## Les trois choses à ne jamais faire

1. Restaurer une sauvegarde sans Lucas Ferreira, parce que ça n'a jamais été testé.
2. Changer le rangement des informations sans Lucas Ferreira, parce que le retour en arrière n'est pas écrit.
3. Charger la liste des élèves hors format UTF-8, parce que ça a doublé 212 élèves.

---
Ce document fait partie du dossier de passation (6 documents). Une erreur ou un oubli ? Signalez-le à Denise Prado.
