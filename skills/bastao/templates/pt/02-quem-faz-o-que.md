# {{system_name}}: quem faz o quê

Preparado em {{doc_date}} por {{author}}, para {{readers}}.

<!-- Duas páginas no máximo. Uma pessoa por linha, nunca "a equipe" nem "o setor": tarefa sem nome não se faz.
     O substituto é obrigatório para toda tarefa cujo esquecimento tem consequência.
     Nenhuma senha aqui nem em lugar nenhum: só o lugar onde ela fica guardada. O documento 5 é a referência dos acessos; o que está aqui é cópia.
     Um campo sem resposta recebe a marca [A CONFIRMAR]. Escrever como uma pessoa (references/writing-style.md). -->

## As pessoas

| Nome | Cargo | Papel no sistema | Contato por |
|---|---|---|---|
| {{person_name}} | {{person_title}} | Dono do sistema | {{person_contact}} |
| {{person_name}} | {{person_title}} | Referência técnica | {{person_contact}} |
| {{person_name}} | {{person_title}} | Operador do dia a dia ({{operator_location}}) | {{person_contact}} |
| {{person_name}} | {{person_title}} | Desenvolvedor de origem, disponível {{developer_availability}} | {{person_contact}} |

## Quem decide o quê

<!-- Resposta à pergunta 1. As cinco decisões abaixo existem em todo sistema; acrescentar outras se o repositório ou as respostas revelarem. -->

| Decisão | Quem decide | Quem deve ser consultado antes | Quem é avisado depois |
|---|---|---|---|
| Mudar uma regra de funcionamento | {{decision_maker}} | {{decision_consulted}} | {{decision_informed}} |
| Dar ou retirar um acesso | {{decision_maker}} | {{decision_consulted}} | {{decision_informed}} |
| Instalar uma nova versão | {{decision_maker}} | {{decision_consulted}} | {{decision_informed}} |
| Renovar licença, domínio ou contrato | {{decision_maker}} | {{decision_consulted}} | {{decision_informed}} |
| Parar o sistema, mesmo que por pouco tempo | {{decision_maker}} | {{decision_consulted}} | {{decision_informed}} |

## Quem faz o quê, e quando

<!-- O detalhe dos gestos está no documento 3 (Rotina). Aqui: só quem, com que frequência, e o que acontece se for esquecido. Ordenar por frequência: diário, semanal, mensal, anual, eventual. -->

| Tarefa | Responsável | Substituto | Frequência | Se ninguém fizer |
|---|---|---|---|---|
| {{task}} | {{task_owner}} | {{task_deputy}} | {{task_frequency}} | {{task_if_missed}} |
| {{task}} | {{task_owner}} | {{task_deputy}} | {{task_frequency}} | {{task_if_missed}} |

## O que cada um pode fazer por conta própria, e o que exige acordo

<!-- Resposta à pergunta 6. É o limite que protege o sucessor: o que ele pode tentar sem risco, o que exige um sim do dono, o que nunca deve fazer sem a referência técnica ou o desenvolvedor. -->

| Pessoa ou papel | Pode fazer por conta própria | Com acordo do dono | Nunca sem a referência técnica ou o desenvolvedor |
|---|---|---|---|
| {{role}} | {{alone_list}} | {{with_owner_list}} | {{never_without_tech_list}} |

## Contas e acessos por papel

<!-- Resposta à pergunta 2. O detalhe (como trocar, quem tem a chave) está no documento 5. Aqui: quem tem o quê, e onde fica guardado. -->

| Papel | Conta ou acesso | Nível | Guardado onde |
|---|---|---|---|
| {{role}} | {{account}} | {{access_level_plain}} | {{custody_place}} |

## Quando alguém sai

<!-- Uma linha por papel: o que transferir, e para quem. É a parte que ninguém escreve e todo mundo procura no dia da saída. -->

- Se {{role}} sair: transferir {{transfer_what}} para {{transfer_to}}, e trocar {{accesses_to_change}}.

---
Este documento faz parte da pasta de passagem ({{doc_count}} documentos). Erro ou esquecimento? Avise {{corrections_contact}}.
