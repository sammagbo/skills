# Estante: custódia de acessos

Preparado em 30/10/2026 pelo desenvolvedor de origem (nome [A CONFIRMAR]), só para Marcia Okafor e Denise Prado. Não repassar.

## Regras de custódia

1. Cada acesso tem um guardião nomeado e um substituto.
2. Os segredos vivem num único lugar de referência: o Bitwarden da escola, organização "Jacaranda TI" [A CONFIRMAR]. Foi o desenvolvedor que informou. Marcia Okafor precisa confirmar de viva voz.
3. Quando alguém sai, os acessos que essa pessoa conhecia são trocados em até [A CONFIRMAR]. A lista está no documento 2, "Quando alguém sai".
4. Nenhum segredo por e-mail, por mensagem ou em documento compartilhado. Nunca nesta pasta.
5. Uma conta compartilhada ("admin", "root", a conta de um equipamento) só é usada se a ferramenta não oferecer contas individuais. Mesmo assim ela tem um guardião e um substituto, fica guardada no Bitwarden da escola [A CONFIRMAR] e é trocada a cada saída de alguém que a conhecia. No inventário, essas contas levam a marca "(compartilhada)".

## Inventário de acessos

| Acesso | Para que serve | Quem detém | Substituto | Guardado onde |
|---|---|---|---|---|
| Servidor: conexão à máquina (mini-PC ESTANTE01, endereço 192.168.0.20) | Entrar na máquina para verificar, reiniciar, fazer backup, instalar | Denise Prado (conta "denise"). Conta "estante" (compartilhada): [A CONFIRMAR] | [A CONFIRMAR] | Bitwarden da escola [A CONFIRMAR] |
| Bitwarden da escola, organização "Jacaranda TI" | Guardar as senhas | Marcia Okafor, administradora. Denise Prado vê a coleção "Estante". O desenvolvedor tem acesso até a saída, no fim de novembro de 2026. | [A CONFIRMAR] | Não se aplica |
| Conta de administrador do aplicativo | Criar contas no Estante | [A CONFIRMAR] | [A CONFIRMAR] | [A CONFIRMAR] |
| Banco de dados: acesso direto às informações | Ler ou corrigir as informações sem passar pela tela | Denise Prado, pelo mini-PC [A CONFIRMAR] | [A CONFIRMAR] | Arquivo deploy/.env no mini-PC |
| Equipamentos (impressora Zebra GK420t, leitores de código de barras e de carteirinha) | Imprimir as etiquetas, ler os livros e as carteirinhas | [A CONFIRMAR] | [A CONFIRMAR] | [A CONFIRMAR] |
| Roteador da escola | Guarda o endereço fixo 192.168.0.50 da impressora | [A CONFIRMAR] | [A CONFIRMAR] | [A CONFIRMAR] |
| Domínio e certificado | Endereço jacaranda.example.org no registrador de domínios. O certificado (o cadeado do navegador) se renova sozinho. | Roberto, financeiro | [A CONFIRMAR] | [A CONFIRMAR] |
| Conta do MailExemplo (envio dos e-mails) | Enviar os lembretes às famílias | Roberto, financeiro, para o pagamento | [A CONFIRMAR] | Senha escrita em claro no repositório: ponto a resolver, documento 6 |
| Internet (Provedor Exemplo) | A conexão da escola | Secretaria, que tem o contrato | [A CONFIRMAR] | [A CONFIRMAR] |
| Espaço onde os backups são depositados | Guardar as cópias das informações | Denise Prado, pelo mini-PC [A CONFIRMAR] | [A CONFIRMAR] | /home/estante/backups no mini-PC. HD externo: [A CONFIRMAR] |
| Código-fonte ([A CONFIRMAR]; há uma cópia no mini-PC, em /home/estante/estante) | Modificar ou reinstalar o programa | O desenvolvedor de origem | Denise Prado [A CONFIRMAR] | [A CONFIRMAR] |

### Trocar e recuperar

| Acesso | Como trocar | Se for perdido ou vazar |
|---|---|---|
| Servidor | No mini-PC, trocar a senha da conta (comando passwd) ou apagar a conta. A nova senha vai para o Bitwarden da escola [A CONFIRMAR]. | Trocar na hora a senha da conta em questão. Avisar Marcia Okafor. |
| Bitwarden da escola | Marcia Okafor retira ou acrescenta a pessoa na organização | [A CONFIRMAR] |
| Conta de administrador do aplicativo | [A CONFIRMAR] | [A CONFIRMAR] |
| Banco de dados | [A CONFIRMAR]: trocar POSTGRES_PASSWORD exige trocar também dentro do banco. Até 31/01/2027, com o desenvolvedor. | [A CONFIRMAR] |
| Equipamentos | [A CONFIRMAR] | [A CONFIRMAR] |
| Roteador da escola | [A CONFIRMAR] | [A CONFIRMAR] |
| Domínio e certificado | [A CONFIRMAR] | [A CONFIRMAR] |
| Conta do MailExemplo | Trocar a senha no MailExemplo, guardar no Bitwarden da escola [A CONFIRMAR] e tirar do arquivo docker-compose.yml | A senha atual já pode ser lida por qualquer pessoa que tenha o código: trocar antes da assinatura do documento 6 |
| Internet (Provedor Exemplo) | [A CONFIRMAR] | [A CONFIRMAR] |
| Espaço dos backups | Os mesmos acessos do servidor | Um backup tem os dados dos alunos: avisar Marcia Okafor |
| Código-fonte | [A CONFIRMAR] | [A CONFIRMAR] |

## Parâmetros sensíveis do sistema (só os nomes)

Um parâmetro é um ajuste lido na inicialização do programa. Aqui, só o nome. O valor fica guardado no mini-PC.

| Nome do parâmetro | Para que serve | Onde é definido no servidor |
|---|---|---|
| POSTGRES_USER | Nome da conta do banco de dados | deploy/.env |
| POSTGRES_PASSWORD | Senha do banco de dados | deploy/.env |
| POSTGRES_DB | Nome do banco de dados | deploy/.env |
| DATABASE_URL | Endereço completo do banco para o programa, montado a partir dos três ajustes acima | deploy/docker-compose.yml |
| SECRET_KEY | Chave que protege as sessões das pessoas conectadas | deploy/.env |
| SMTP_HOST | Servidor de envio dos e-mails (MailExemplo) | deploy/docker-compose.yml, escrito em claro |
| SMTP_USER | Conta de envio dos e-mails | deploy/docker-compose.yml, escrito em claro |
| SMTP_PASSWORD | Senha da conta de envio dos e-mails | deploy/docker-compose.yml, escrito em claro: ponto a resolver, documento 6 |
| PRINTER_URL | Endereço da impressora de etiquetas na rede | deploy/.env |
| TZ | Fuso horário do programa (não o do mini-PC) | deploy/docker-compose.yml |
| ADMIN_EMAIL | [A CONFIRMAR]: está em deploy/.env.example, mas o programa não lê | deploy/.env [A CONFIRMAR] |

## Backups

- Onde: /home/estante/backups, no próprio mini-PC.
- Com que frequência: toda noite às 02:30 (hora do mini-PC).
- Guardados durante: 30 dias.
- Cópia fora do servidor: [A CONFIRMAR] (o desenvolvedor acha que Denise Prado às vezes copia para um HD externo, sem certeza). Criptografada: [A CONFIRMAR] (segundo o desenvolvedor, não).
- Última restauração provada: em [A CONFIRMAR], por [A CONFIRMAR]. Segundo o desenvolvedor, nenhuma restauração foi testada.
- Quem sabe restaurar: ninguém provou [A CONFIRMAR]. O procedimento está no documento 3, "Quando for preciso".
- Quem pode ler um backup (ele contém informações pessoais): [A CONFIRMAR].

## Próximos prazos ligados a acessos

| Data | O quê (certificado, domínio, licença, senha a renovar) | Quem |
|---|---|---|
| Antes da assinatura do documento 6 | Trocar SMTP_PASSWORD (escrita em claro no repositório) | Denise Prado [A CONFIRMAR] |
| Fim de novembro de 2026 (data exata [A CONFIRMAR]) | Retirar o acesso do desenvolvedor ao Bitwarden e trocar as senhas que ele conhece | Marcia Okafor |
| 31/01/2027 | Fim da disponibilidade do desenvolvedor por e-mail | Marcia Okafor |
| Todo mês | Plano do MailExemplo | Roberto, financeiro |
| 14/03/2027 | Endereço jacaranda.example.org no registrador de domínios | Roberto, financeiro |
| [A CONFIRMAR] | Bateria do nobreak APC, trocada em 2024 | [A CONFIRMAR] |
| [A CONFIRMAR] | Contrato de internet Provedor Exemplo | Secretaria |

---
Este documento faz parte da pasta de passagem (6 documentos). Erro ou esquecimento? Avise Denise Prado.
