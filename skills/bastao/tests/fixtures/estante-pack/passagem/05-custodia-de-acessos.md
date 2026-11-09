# Estante: custódia de acessos

Preparado em 09/11/2026 por Lucas Ferreira, só para o dono, Marcia Okafor, e a referência técnica, Denise Prado. Não repassar.

## Regras de custódia

1. Cada acesso tem um guardião nomeado e um substituto.
2. Os segredos vivem num único lugar de referência: o Bitwarden da escola (o programa onde as senhas ficam guardadas), organização Jacaranda TI [A CONFIRMAR].
3. Quando alguém sai, os acessos que essa pessoa conhecia são trocados em até [A CONFIRMAR]. A lista está no documento 2, "Quando alguém sai".
4. Nenhum segredo por e-mail, por mensagem ou em documento compartilhado. Nunca nesta pasta.
5. Uma conta compartilhada só é usada se não houver contas individuais (a conta "admin", "root" ou a de um equipamento). Ela tem um guardião e um substituto, e é trocada a cada saída de alguém que a conhecia. Ela fica guardada no Bitwarden da escola [A CONFIRMAR] e leva no inventário a marca "(compartilhada)".

## Inventário de acessos

| Acesso | Para que serve | Quem detém | Substituto | Guardado onde |
|---|---|---|---|---|
| Servidor: conexão técnica (SSH) à máquina ESTANTE01. Conta denise, criada em setembro. Conta estante (compartilhada [A CONFIRMAR]) | Instalar versões, ver mensagens, fazer cópias | Denise Prado (conta denise). Lucas Ferreira tem acesso hoje e será removido quando sair. Conta estante: [A CONFIRMAR] | [A CONFIRMAR] | O Bitwarden da escola [A CONFIRMAR] |
| Bitwarden da escola, organização Jacaranda TI, coleção Estante [A CONFIRMAR] | Guardar as senhas deste sistema | Marcia Okafor (administradora). Denise Prado (vê a coleção Estante). Lucas Ferreira tem acesso hoje e será removido quando sair [A CONFIRMAR] | [A CONFIRMAR] | O Bitwarden da escola [A CONFIRMAR] |
| Conta de administrador do programa: contas joana e lucas (a conta lucas deve ser desativada) | Administrar o programa | Joana Lima (conta joana). Lucas Ferreira (conta lucas) | [A CONFIRMAR] | O Bitwarden da escola [A CONFIRMAR] |
| Banco de dados: acesso direto às informações (POSTGRES_USER e POSTGRES_PASSWORD) | Aplicar mudanças e restaurar cópias | [A CONFIRMAR] | [A CONFIRMAR] | [A CONFIRMAR] |
| Equipamentos (impressora Zebra de etiquetas) | Imprimir as etiquetas dos livros novos | [A CONFIRMAR] | [A CONFIRMAR] | O painel da impressora não tinha senha. Lucas Ferreira não sabe se alguém mudou isso [A CONFIRMAR] |
| Conta de e-mail biblioteca@jacaranda.example.org, no serviço MailExemplo (plano mensal no cartão da escola) | Enviar os lembretes aos responsáveis | [A CONFIRMAR]. Roberto, do financeiro, cuida do pagamento | [A CONFIRMAR] | Escrita sem proteção no repositório, o lugar onde o texto do programa fica guardado (documento 6) |
| Domínio jacaranda.example.org e certificado | Manter o endereço do sistema. O Caddy renova o certificado sozinho | [A CONFIRMAR]. Roberto, do financeiro, cuida do pagamento | [A CONFIRMAR] | [A CONFIRMAR] |
| Espaço onde as cópias são depositadas: pasta /home/estante/backups, na própria máquina | Guardar as cópias de 30 dias | [A CONFIRMAR] | [A CONFIRMAR] | Na máquina ESTANTE01 |
| Código-fonte (sem endereço remoto; cópia na máquina, pasta /home/estante/estante) | Instalar novas versões | [A CONFIRMAR] | [A CONFIRMAR] | Na máquina ESTANTE01 |

### Trocar e recuperar

Lucas Ferreira sai no fim de novembro de 2026. Desativar a conta lucas do programa. Retirar o acesso dele à máquina e ao Bitwarden da escola [A CONFIRMAR].

A definir com o dono [A CONFIRMAR]: como trocar cada outro acesso, e o que fazer se ele for perdido ou vazar. Nada disso está escrito no repositório.

## Parâmetros sensíveis do sistema (só os nomes)

| Nome do parâmetro | Para que serve | Onde é definido no servidor |
|---|---|---|
| POSTGRES_USER | Nome da conta do banco de dados | Arquivo deploy/.env (não aberto) |
| POSTGRES_PASSWORD | Senha da conta do banco de dados | Arquivo deploy/.env (não aberto) |
| POSTGRES_DB | Nome do banco de dados | Arquivo deploy/.env (não aberto) |
| DATABASE_URL | Endereço que o programa usa para falar com o banco, montado com os três nomes acima | deploy/docker-compose.yml |
| SECRET_KEY | Chave interna do programa [A CONFIRMAR] | Arquivo deploy/.env (não aberto) |
| SMTP_HOST | Máquina que envia os e-mails | deploy/docker-compose.yml |
| SMTP_USER | Conta de e-mail que envia os lembretes | deploy/docker-compose.yml |
| SMTP_PASSWORD | Senha dessa conta de e-mail. O valor está escrito sem proteção no arquivo ao lado: documento 6 | deploy/docker-compose.yml |
| PRINTER_URL | Endereço da impressora de etiquetas | Arquivo deploy/.env (não aberto) |
| TZ | Fuso horário do programa | deploy/docker-compose.yml |
| ADMIN_EMAIL | E-mail do administrador. O repositório não mostra onde é usado [A CONFIRMAR] | Arquivo deploy/.env (não aberto) |

## Backups

- Onde: na própria máquina ESTANTE01, pasta /home/estante/backups.
- Com que frequência: todo dia às 02:30.
- Guardados durante: 30 dias.
- Cópia fora do servidor: Lucas Ferreira acha que Denise Prado copia às vezes para um disco externo, mas não sabe [A CONFIRMAR]. Criptografada: não, diz Lucas Ferreira [A CONFIRMAR].
- Última restauração provada: em [A CONFIRMAR], por [A CONFIRMAR]. Lucas Ferreira acha que nunca testou [A CONFIRMAR].
- Quem sabe restaurar: [A CONFIRMAR]. Até janeiro de 2027, só depois de falar com Lucas Ferreira. O procedimento está no documento 3, "Quando for preciso".
- Quem pode ler um backup (ele contém informações pessoais): [A CONFIRMAR].

## Próximos prazos ligados a acessos

| Data | O quê (certificado, domínio, licença, senha a renovar) | Quem |
|---|---|---|
| Fim de novembro de 2026 | Saída de Lucas Ferreira: desativar a conta lucas e retirar os acessos dele | [A CONFIRMAR] |
| 31/01/2027 | Fim da ajuda de Lucas Ferreira, só para dúvidas, por e-mail | [A CONFIRMAR] |
| 14/03/2027 | Renovação do domínio jacaranda.example.org | Roberto, do financeiro, paga; quem renova [A CONFIRMAR] |
| Todo mês | Plano do e-mail MailExemplo, no cartão da escola | Roberto, do financeiro |
| [A CONFIRMAR] | Bateria do nobreak, trocada em 2024 | [A CONFIRMAR] |

---
Este documento faz parte da pasta de passagem (6 documentos). Erro ou esquecimento? Avise Denise Prado.
