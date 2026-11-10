# {{system_name}}: checklist de recepção

Preparado em {{doc_date}} por {{author}} para o dono, {{owner}}, e a referência técnica, {{tech_lead}}.

<!-- Uma página. Duas pessoas recebem, cada uma com a sua parte: o dono confirma o que decide e o que sabe; a referência técnica verifica o que mexe no sistema. Cada pessoa marca só o que viu ou fez ela mesma, não o que lhe disseram. O desenvolvedor não preenche nada, só assina.
     Uma caixa não marcada não é falha: é um ponto a resolver antes da assinatura, listado embaixo com quem decide e para quando.
     Nada é provocado no sistema em produção para marcar uma caixa.
     Cada linha vale para a pessoa da sua parte: sem dono, sem referência técnica ou sem resposta para um campo, a marca, nunca uma frase sobre outra pessoa. Uma caixa diz o que a pessoa fez, nunca um fato sobre quem mais tem o quê. A disponibilidade do desenvolvedor guarda o limite que as respostas dão (só dúvidas, sem mexer na máquina). repo_location é o lugar do código: pasta e máquina. A versão instalada só é marcada se o documento 3 dá um jeito de lê-la sem provocar nada; senão a caixa fica em branco e a tabela diz isso. Entram na tabela, com quem decide quando uma resposta o dá: quem faz a verificação diária, quem retira os acessos do desenvolvedor e quando, e cada ponto em aberto de que uma caixa depende.
     Na exportação em PDF: duas linhas de altura para cada linha de assinatura. Escrever como uma pessoa, na primeira pessoa de quem marca, sem forma de gênero (references/writing-style.md). -->

## O dono confirma

- [ ] Li os documentos 1, 2 e 4 e sei o que o sistema não faz.
- [ ] Sei as três coisas que nunca se deve fazer, quem decide o quê, quem chamar e os prazos do próximo ano.
- [ ] Recebi o documento 5 e não o repassei.
- [ ] Concordo que {{update_owner}} atualiza esta pasta.
- [ ] Conheço a disponibilidade de {{author}} ({{developer_availability}}) e a saída dos acessos dele ({{access_change_deadline}}).

## A referência técnica verifica

- [ ] Li os documentos 1 a 5 e recebi o programa: {{repo_location}}, versão {{repo_version}}.
- [ ] O programa instalado é da versão {{installed_version}}.
- [ ] Entro em {{main_access}} com a minha conta e tenho as senhas do meu papel.
- [ ] Fiz a verificação diária do documento 3. Esperado: {{expected_result}}. Vi: ________.
- [ ] Vi uma cópia recente das informações, de {{backup_seen_date}}.
- [ ] Percorri com {{author}} um incidente do documento 4 ({{drill_incident}}), sem provocar nada.

## O que falta resolver antes da assinatura

<!-- Cada frase que fala do cofre de senhas, da última restauração, da cópia fora da máquina ou da criptografia leva a sua marca [A CONFIRMAR] dentro da frase, e a ressalva de quem respondeu ("acho que") fica. A marca nas colunas Quem decide e Para quando não vale. Segredos escritos sem proteção: o nome da variável, seguido do que ela é em palavras simples. Quem decide e Para quando: o nome e a data que uma resposta dá; senão, uma linha em branco, ________, para preencher no dia. -->

Cada ponto leva um nome e uma data antes da assinatura.

| Ponto | Quem decide | Para quando |
|---|---|---|
| {{open_point}} | {{open_point_owner}} | {{open_point_due}} |

## Assinaturas

| | Nome | Data | Assinatura |
|---|---|---|---|
| Entregue por | {{author}} | | |
| Dono do sistema | {{owner}} | | |
| Referência técnica | {{tech_lead}} | | |

{{author}} assina que entregou; os outros dois assinam a sua parte.

---
Este documento faz parte da pasta de passagem ({{doc_count}} documentos). Erro ou esquecimento? Avise {{corrections_contact}}.
