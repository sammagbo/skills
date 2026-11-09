# Estante : ce que c'est et ce que ça ne fait pas

Préparé le 09/11/2026 par Lucas Ferreira, pour la direction et l'informatique.

## En une phrase

Estante sert à enregistrer les prêts et les retours de livres de la bibliothèque de l'école Jacarandá. Utilisatrice : Joana Lima, bibliothécaire.

## Ce que ça fait

- Enregistre les prêts et les retours, avec le code-barres et la carte.
- Envoie un e-mail de rappel aux responsables quand un livre a plus de 3 jours de retard, à 07:00 en semaine.
- Imprime l'étiquette des livres neufs.

Lucas Ferreira dit que tout marche. Le texte remis ne fait que le décrire : document 6.

## Ce que ça ne fait pas

- Ne bloque pas la sortie du livre. N'a pas de portique antivol, que l'école croit avoir.
- N'envoie ni SMS ni WhatsApp.
- Pas d'amende : désactivée en 2025, par décision de la direction.
- N'est pas relié au secrétariat. La liste des élèves est importée à la main.

## Où ça tourne

- Sur la machine ESTANTE01, en salle de coordination, branchée sur un onduleur.
- Trois parties : estante-app (le programme de l'écran), estante-db (les informations), estante-caddy (le cadenas de l'adresse).
- Accès : navigateur, estante.jacaranda.example.org.
- Les informations sont copiées chaque jour à 02:30, sur la machine. Hors de la machine : Lucas Ferreira croit que Denise Prado copie parfois sur disque externe [À CONFIRMER].

## Qui en est responsable

| Rôle | Nom et fonction | Ce que cette personne décide ou fait |
|---|---|---|
| Propriétaire du système | Marcia Okafor, directrice pédagogique | Décide les changements |
| Référent technique | Denise Prado, technicienne informatique | Première personne à appeler |
| Développeur d'origine | Lucas Ferreira | Part en 11/2026. Questions par e-mail jusqu'au 31/01/2027 |

## Ce qui a une date

| Échéance | Quoi | Qui s'en occupe | Si c'est oublié |
|---|---|---|---|
| 14/03/2027 | Renouvellement du domaine | Roberto, des finances, paie ; qui renouvelle : [À CONFIRMER] | [À CONFIRMER] |
| Chaque mois | Abonnement e-mail MailExemplo | Roberto, des finances, paie | Rappels arrêtés en 06/2026 |

## Les trois choses à ne jamais faire

1. Désactiver l'option qui lance le programme avec la machine : le 11/03/2025, il n'a pas redémarré après une coupure.
2. Importer des élèves sans vérifier les accents : le 19/02/2026, l'import a créé 212 élèves en double.
3. Changer l'adresse de l'imprimante d'étiquettes : en 08/2026, elle a cessé d'imprimer.

---
Ce document fait partie du dossier de passation (6 documents). Une erreur ou un oubli ? Signalez-le à Denise Prado.
