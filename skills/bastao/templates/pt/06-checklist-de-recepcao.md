# {{system_name}}: checklist de recepção

Entregue em {{doc_date}} por {{author}} a {{successor}} ({{successor_title}}, {{successor_role}}).

<!-- Uma página. Para ser preenchido pelo sucessor, não pelo desenvolvedor. Cada caixa marcada é algo que ele viu ou fez ele mesmo, não algo que lhe disseram.
     Uma caixa não marcada não é falha: é um ponto a resolver antes da assinatura, listado embaixo com nome e data.
     Nada é provocado no sistema em produção para marcar uma caixa.
     Na exportação em PDF: duas linhas de altura para cada linha de assinatura. Escrever como uma pessoa, na primeira pessoa, sem forma de gênero (references/writing-style.md). -->

## Recebi e li

- [ ] Os documentos 1 a 4: o que é, quem faz o quê, rotina, se quebrar.
- [ ] O documento 5, custódia de acessos, recebido pela referência técnica, {{tech_lead}}, que assina abaixo.
- [ ] O código-fonte: {{repo_location}}, versão {{repo_version}}.

## Verifiquei pessoalmente

- [ ] O programa mostra a versão {{installed_version}}, instalada em {{installed_date}}, e é a mesma do código-fonte recebido.
- [ ] Consigo entrar em {{main_access}} com a minha conta, não a do desenvolvedor.
- [ ] Sei onde os segredos ficam guardados, e tenho acesso aos do meu papel (documento 2, "Contas e acessos por papel") sem tê-los recebido por mensagem.
- [ ] Os acessos pessoais do desenvolvedor de origem (servidor, aplicativo, equipamentos, hospedagem, código) foram retirados ou trocados. O que ele mantém, e até quando, está escrito no documento 5.
- [ ] Fiz a verificação diária do documento 3 e obtive: {{expected_result}}.
- [ ] Vi um backup recente, de {{backup_seen_date}}, e sei quem sabe restaurá-lo.
- [ ] Percorri em simulação, com {{author}}, um incidente do documento 4 ({{drill_incident}}) até o fim, sem provocar nada no sistema, e os contatos da tabela "Quem chamar" atenderam.
- [ ] Conheço as três coisas que nunca se deve fazer.
- [ ] Sei quais prazos vencem nos próximos doze meses e quem cuida deles.
- [ ] Sei quem chamar, em que ordem, e até onde posso ir por conta própria.
- [ ] Sei onde a pasta fica guardada ({{dossier_location}}) e quem a atualiza quando uma pessoa, uma data ou um acesso muda.

## O que falta resolver antes da assinatura

| Ponto | Quem | Para quando |
|---|---|---|
| {{open_point}} | {{open_point_owner}} | {{open_point_due}} |

## Assinaturas

| | Nome | Data | Assinatura |
|---|---|---|---|
| Entregue por | {{author}} | | |
| Recebido por | {{successor}} | | |
| Referência técnica | {{tech_lead}} | | |
| Dono do sistema | {{owner}} | | |

---
Este documento faz parte da pasta de passagem ({{doc_count}} documentos). Erro ou esquecimento? Avise {{corrections_contact}}.
