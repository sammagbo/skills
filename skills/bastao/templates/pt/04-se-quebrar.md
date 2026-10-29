# {{system_name}}: se quebrar

Preparado em {{doc_date}} por {{author}}, para {{readers}}: a pessoa que está lá quando acontece.

<!-- Uma página, cerca de 380 palavras. Este documento é lido sob estresse: frases curtas, um sintoma por bloco, a ordem exata dos gestos, você no imperativo (Verifique, Chame).
     Construído a partir da pergunta 5 (incidentes reais, não imaginados) e da pergunta 6 (quem chamar, até onde ir por conta própria).
     Ordem: primeiro o que é sem risco, depois quem chamar, e com clareza o que nunca se deve fazer.
     Três sintomas, quatro no máximo se cada bloco couber em cinco linhas (symptom_4_*). O título de cada bloco é o sintoma em linguagem corrente, do jeito que a pessoa diria ao telefone.
     Se não houver referência técnica, a linha 1 da tabela "Quem chamar" é o desenvolvedor de origem, nas condições dele, e a falta de referência é um ponto a resolver no documento 6.
     Na exportação em PDF: títulos compactos (12 pt) e margens pequenas. Escrever como uma pessoa (references/writing-style.md). -->

## Antes de tudo

- Nunca faça isto, aconteça o que acontecer: {{forbidden_1}}; {{forbidden_2}}; {{forbidden_3}}. As razões estão no documento 1.
- Se houver pessoas bloqueadas ({{blocked_example}}), comece pela solução de emergência: {{fallback_procedure}}.
- Só depois, anote a hora e tire uma foto do que aparece na tela.

## {{symptom_1}}

- Verifique primeiro, sem risco: {{symptom_1_check}}
- Na maioria das vezes, isso quer dizer: {{symptom_1_cause}}
- O que você pode fazer por conta própria: {{symptom_1_action}}
- Está consertado quando: {{symptom_1_fixed_when}}
- Se não resolver, chame {{symptom_1_who}} ({{symptom_1_how}}).

## {{symptom_2}}

- Verifique primeiro, sem risco: {{symptom_2_check}}
- Na maioria das vezes, isso quer dizer: {{symptom_2_cause}}
- O que você pode fazer por conta própria: {{symptom_2_action}}
- Está consertado quando: {{symptom_2_fixed_when}}
- Se não resolver, chame {{symptom_2_who}} ({{symptom_2_how}}).

## {{symptom_3}}

- Verifique primeiro, sem risco: {{symptom_3_check}}
- Na maioria das vezes, isso quer dizer: {{symptom_3_cause}}
- O que você pode fazer por conta própria: {{symptom_3_action}}
- Está consertado quando: {{symptom_3_fixed_when}}
- Se não resolver, chame {{symptom_3_who}} ({{symptom_3_how}}).

## Quem chamar, nesta ordem

| Ordem | Quem | Para quê | Contato (como, quando) |
|---|---|---|---|
| 1 | {{tech_lead}} | Tudo o que está neste documento | {{tech_lead_contact}}, {{tech_lead_hours}} |
| 2 | {{vendor}} | {{vendor_scope}} | {{vendor_contact}}, {{vendor_hours}} |
| 3 | {{author}} | O que mais ninguém sabe consertar. Disponível {{developer_availability}} | {{author_contact}}, {{author_hours}} |

Avise {{owner}} assim que houver pessoas bloqueadas ou informações em jogo. Parar ou não o sistema é decisão dessa pessoa.

## Depois do incidente

- Anote em {{logbook}}: a data, o sintoma, o que foi feito, quem consertou, quanto tempo levou.

---
Este documento faz parte da pasta de passagem ({{doc_count}} documentos). Erro ou esquecimento? Avise {{corrections_contact}}.
