# {{system_name}}: custódia de acessos

Preparado em {{doc_date}} por {{author}}, só para {{owner}} e {{tech_lead}}. Não repassar.

<!-- Este documento não contém nenhuma senha, chave ou token. Ele diz o que existe, onde fica guardado, quem tem acesso, como trocar, e o que acontece se for perdido ou vazar.
     O scanner de segredos recusa a geração se algum valor parecer senha, chave ou token.
     Nenhum endereço com credencial (usuario:senha@…, token numa URL), nenhum comando com senha como argumento ou variável de ambiente. Quando um procedimento exigir um segredo, escrever "(a senha está em {{vault}})".
     Os nomes dos parâmetros vêm do repositório (arquivos de exemplo, docker-compose, scripts). Se o repositório contiver um valor em claro, nunca reproduzi-lo: registrar como ponto a resolver no documento 6 ("segredo em claro no repositório: {{param_name}}").
     Este documento é a referência para os acessos e suas datas; o documento 2 "Contas e acessos por papel" e o documento 1 "O que tem data" são cópias dele, a corrigir juntos.
     Se o desenvolvedor de origem mantiver algum acesso depois da passagem, ele aparece no inventário com data de fim.
     {{vault}}, {{last_restore_date}}, {{backup_offsite}} e {{backup_encrypted}} ficam com a marca [A CONFIRMAR] até o dono confirmar de viva voz, mesmo que o repositório sugira um valor.
     Na exportação em PDF: este documento pode sair em paisagem se as tabelas ficarem apertadas. Escrever como uma pessoa (references/writing-style.md). -->

## Regras de custódia

1. Cada acesso tem um guardião nomeado e um substituto.
2. Os segredos vivem num único lugar de referência: {{vault}} (um gerenciador de senhas, um cofre, um envelope lacrado).
3. Quando alguém sai, os acessos que essa pessoa conhecia são trocados em até {{access_change_deadline}}. A lista está no documento 2, "Quando alguém sai".
4. Nenhum segredo por e-mail, por mensagem ou em documento compartilhado. Nunca nesta pasta.
5. Uma conta compartilhada ("admin", "root", a conta de um equipamento) só é usada se a ferramenta não oferecer contas individuais. Mesmo assim ela tem um guardião e um substituto, fica guardada em {{vault}} e é trocada a cada saída de alguém que a conhecia. No inventário, essas contas levam a marca "(compartilhada)".

## Inventário de acessos

<!-- Uma linha por acesso, inclusive os que a organização acha óbvios. As linhas abaixo são as categorias habituais; retirar as que não existem, acrescentar as que o repositório revelar. As mesmas linhas, na mesma ordem, nas duas tabelas. -->

| Acesso | Para que serve | Quem detém | Substituto | Guardado onde |
|---|---|---|---|---|
| Servidor: conexão à máquina ({{server_location}}) | {{access_use}} | {{access_holder}} | {{access_deputy}} | {{access_place}} |
| Provedor de hospedagem: console do fornecedor (criar, parar, apagar a máquina) | {{access_use}} | {{access_holder}} | {{access_deputy}} | {{access_place}} |
| Conta de administrador do aplicativo | {{access_use}} | {{access_holder}} | {{access_deputy}} | {{access_place}} |
| Banco de dados: acesso direto às informações | {{access_use}} | {{access_holder}} | {{access_deputy}} | {{access_place}} |
| Equipamentos ({{equipment_type}}) | {{access_use}} | {{access_holder}} | {{access_deputy}} | {{access_place}} |
| Domínio e certificado | {{access_use}} | {{access_holder}} | {{access_deputy}} | {{access_place}} |
| Espaço onde os backups são depositados | {{access_use}} | {{access_holder}} | {{access_deputy}} | {{access_place}} |
| Chave de licença ou de assinatura digital | {{access_use}} | {{access_holder}} | {{access_deputy}} | {{access_place}} |
| Código-fonte ({{repo_location}}) | {{access_use}} | {{access_holder}} | {{access_deputy}} | {{access_place}} |

### Trocar e recuperar

| Acesso | Como trocar | Se for perdido ou vazar |
|---|---|---|
| Servidor | {{access_change_procedure}} | {{access_loss_recovery}} |
| Provedor de hospedagem | {{access_change_procedure}} | {{access_loss_recovery}} |
| Conta de administrador do aplicativo | {{access_change_procedure}} | {{access_loss_recovery}} |
| Banco de dados | {{access_change_procedure}} | {{access_loss_recovery}} |
| Equipamentos | {{access_change_procedure}} | {{access_loss_recovery}} |
| Domínio e certificado | {{access_change_procedure}} | {{access_loss_recovery}} |
| Espaço dos backups | {{access_change_procedure}} | {{access_loss_recovery}} |
| Chave de licença ou de assinatura digital | {{access_change_procedure}} | {{access_loss_recovery}} |
| Código-fonte | {{access_change_procedure}} | {{access_loss_recovery}} |

## Parâmetros sensíveis do sistema (só os nomes)

<!-- Lista dos parâmetros encontrados no repositório, com o papel de cada um em linguagem corrente. Nunca o valor. -->

| Nome do parâmetro | Para que serve | Onde é definido no servidor |
|---|---|---|
| {{param_name}} | {{param_role_plain}} | {{param_location}} |

## Backups

<!-- Resposta à pergunta 7. Backup é um acesso como qualquer outro: quem pode ler, quem pode restaurar, onde está. -->

- Onde: {{backup_location}}.
- Com que frequência: {{backup_frequency}}.
- Guardados durante: {{backup_retention}}.
- Cópia fora do servidor: {{backup_offsite}}. Criptografada: {{backup_encrypted}}.
- Última restauração provada: em {{last_restore_date}}, por {{last_restore_by}}.
- Quem sabe restaurar: {{restore_person}}. O procedimento está no documento 3, "Quando for preciso".
- Quem pode ler um backup (ele contém informações pessoais): {{backup_readers}}.

## Próximos prazos ligados a acessos

| Data | O quê (certificado, domínio, licença, senha a renovar) | Quem |
|---|---|---|
| {{due_date}} | {{due_item}} | {{due_owner}} |

---
Este documento faz parte da pasta de passagem ({{doc_count}} documentos). Erro ou esquecimento? Avise {{corrections_contact}}.
