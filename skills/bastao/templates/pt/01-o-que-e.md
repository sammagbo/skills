# {{system_name}}: o que é e o que não faz

Preparado em {{doc_date}} por {{author}}, para {{readers}} (direção, administração, equipe de TI).

<!-- Uma página no máximo, cerca de 380 palavras. Nenhum termo técnico sem a tradução para linguagem corrente (references/plain-language.md):
     "backend" vira "o programa que roda na máquina", "contêiner" vira "a caixa dentro da qual o programa roda",
     "API" vira "a porta pela qual outros programas falam com ele", "banco de dados" vira "o lugar onde as informações ficam gravadas".
     Um campo que nem o repositório nem as respostas preenchem recebe a marca [A CONFIRMAR], nunca uma frase plausível.
     Escrever como uma pessoa: frases curtas, verbos simples (é, tem, serve para), sem travessão, sem negrito nas listas (references/writing-style.md). -->

## Em uma frase

{{system_name}} serve para {{purpose_plain}}. Quem usa: {{users}}.

## O que ele faz

<!-- Três a seis linhas, uma função por linha, começando pelo que a organização vê todos os dias. -->

- {{feature}}. Usado por {{feature_users}}, {{feature_when}}.
- {{feature}}. Usado por {{feature_users}}, {{feature_when}}.
- {{feature}}. Usado por {{feature_users}}, {{feature_when}}.

## O que ele não faz

<!-- Resposta à pergunta 4. Quando o motivo é conhecido, a linha diz por que alguém poderia achar o contrário: é essa crença que provoca os incidentes. Motivo desconhecido: manter só a primeira frase, sem marca. -->

- {{not_feature}}. Dá para achar que faz, porque {{not_feature_reason}}.
- {{not_feature}}. Dá para achar que faz, porque {{not_feature_reason}}.

## Onde ele roda

<!-- access_mode: um programa instalado nos computadores, um navegador, ou os dois. Escrever só o que o repositório ou uma resposta mostra. -->

- O programa roda em {{server_location}}.
- O acesso é por {{access_mode}}.
- Para funcionar, ele precisa de {{external_dependencies}}.
- As informações ficam gravadas em {{storage_plain}} e são copiadas {{backup_frequency}}.

## Quem é responsável

| Papel | Nome e cargo | O que essa pessoa decide ou faz |
|---|---|---|
| Dono do sistema | {{owner}} | Decide {{owner_decides}} |
| Referência técnica | {{tech_lead}} | Primeira pessoa a chamar quando algo não vai bem |
| Desenvolvedor de origem | {{author}} | Disponível {{developer_availability}} |

## O que tem data

<!-- Resposta à pergunta 8. Se não houver nada, escrever "Nenhum prazo conhecido em {{doc_date}}". O documento 5 é a referência dessas datas. Entram aqui todas as datas que têm uma pessoa e uma consequência, também as dos documentos 2, 3 e 5: a saída do desenvolvedor, o fim da ajuda dele, a revisão anual, os pagamentos mensais, o domínio. Quem paga não é quem cuida: escrever só o que a resposta diz. -->

| Prazo | O quê | Quem cuida | Se for esquecido |
|---|---|---|---|
| {{due_date}} | {{due_item}} | {{due_owner}} | {{due_consequence}} |

## As três coisas que nunca se deve fazer

<!-- Quando uma proibição depende de uma pessoa disponível até uma data ("sem o desenvolvedor"), escrever a data: "sem Lucas Ferreira, até 31/01/2027". Depois dessa data, a regra diz quem assume, ou leva a marca. -->

<!-- Tiradas dos incidentes (pergunta 5) e das dependências (pergunta 9). Uma linha cada, no presente, sem adjetivo. Três é um limite de espaço, não figura de estilo. -->

1. {{forbidden_1}}, porque {{forbidden_1_reason}}.
2. {{forbidden_2}}, porque {{forbidden_2_reason}}.
3. {{forbidden_3}}, porque {{forbidden_3_reason}}.

---
Este documento faz parte da pasta de passagem ({{doc_count}} documentos). Erro ou esquecimento? Avise {{corrections_contact}}.
