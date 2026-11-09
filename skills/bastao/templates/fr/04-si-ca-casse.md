# {{system_name}} : si ça casse

Préparé le {{doc_date}} par {{author}}, pour {{readers}} : la personne qui est là quand ça arrive.

<!-- Une page, environ 380 mots. Ce document est lu sous stress : phrases courtes, un symptôme par bloc, l'ordre exact des gestes, le vouvoiement à l'impératif (Vérifiez, Appelez).
     Construit à partir de la question 5 (incidents réels, pas imaginés) et de la question 6 (qui appeler, jusqu'où aller sans aide).
     Ordre : d'abord ce qui est sans risque, ensuite qui appeler, et clairement ce qu'il ne faut jamais faire.
     Trois symptômes, quatre au maximum si chaque bloc tient en cinq lignes (symptom_4_*). Le titre de chaque bloc est le symptôme en langage courant, tel que la personne le dirait au téléphone.
     La cause, la vérification et le « c'est réparé quand » viennent seulement de l'incident enregistré (sa cause et sa réparation) ; jamais d'une supposition ni d'un « le plus souvent ». {{notify_who}} est la personne qu'une réponse dit de prévenir ; sans réponse, la marque. Ne jamais donner au propriétaire la décision d'arrêter le système, ni le devoir d'être prévenu, si aucune réponse ne le dit. Deux contacts pour des problèmes différents (imprimante, internet) portent le même numéro d'ordre avec une lettre (2a, 2b). Si la réponse limite le développeur à répondre à des questions, la ligne 3 le dit. S'il n'y a pas de référent technique, la ligne 1 du tableau "Qui appeler" est le développeur d'origine selon ses conditions, et l'absence de référent est un point à régler dans le document 6.
     À l'export PDF : titres compacts (12 pt) et petites marges. Écrire comme une personne (references/writing-style.md). -->

## Avant tout

- À ne jamais faire, quoi qu'il arrive : {{forbidden_1}} ; {{forbidden_2}} ; {{forbidden_3}}. Les raisons sont dans le document 1.
- Si des personnes sont bloquées ({{blocked_example}}), commencez par la solution de secours : {{fallback_procedure}}.
- Ensuite seulement, notez l'heure et prenez en photo ce qui s'affiche à l'écran.

## {{symptom_1}}

- Vérifiez d'abord, sans risque : {{symptom_1_check}}
- La dernière fois, la cause était : {{symptom_1_cause}}
- Ce que vous pouvez faire vous-même : {{symptom_1_action}}
- C'est réparé quand : {{symptom_1_fixed_when}}
- Si ça ne suffit pas, appelez {{symptom_1_who}} ({{symptom_1_how}}).

## {{symptom_2}}

- Vérifiez d'abord, sans risque : {{symptom_2_check}}
- La dernière fois, la cause était : {{symptom_2_cause}}
- Ce que vous pouvez faire vous-même : {{symptom_2_action}}
- C'est réparé quand : {{symptom_2_fixed_when}}
- Si ça ne suffit pas, appelez {{symptom_2_who}} ({{symptom_2_how}}).

## {{symptom_3}}

- Vérifiez d'abord, sans risque : {{symptom_3_check}}
- La dernière fois, la cause était : {{symptom_3_cause}}
- Ce que vous pouvez faire vous-même : {{symptom_3_action}}
- C'est réparé quand : {{symptom_3_fixed_when}}
- Si ça ne suffit pas, appelez {{symptom_3_who}} ({{symptom_3_how}}).

## Qui appeler, dans l'ordre

| Ordre | Qui | Pour quoi | Joignable (comment, quand) |
|---|---|---|---|
| 1 | {{tech_lead}} | Tout ce qui est dans ce document | {{tech_lead_contact}}, {{tech_lead_hours}} |
| 2 | {{vendor}} | {{vendor_scope}} | {{vendor_contact}}, {{vendor_hours}} |
| 3 | {{author}} | Questions sur la façon dont le système a été fait. Disponible {{developer_availability}} | {{author_contact}}, {{author_hours}} |

Prévenez {{notify_who}} dès que des personnes sont bloquées ou que des informations sont en jeu.

## Après l'incident

- Notez dans {{logbook}} : la date, le symptôme, ce qui a été fait, qui a réparé, la durée.

---
Ce document fait partie du dossier de passation ({{doc_count}} documents). Une erreur ou un oubli ? Signalez-le à {{corrections_contact}}.
