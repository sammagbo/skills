# Estante: custódia de acessos

Preparado em 30/10/2026 por Lucas Ferreira, só para Márcia Okafor e Denise Prado. Não repassar.

## Regras de custódia

1. Cada acesso tem um guardião nomeado e um substituto.
2. Os segredos vivem num único lugar de referência: o Bitwarden da escola, organização "Jacarandá TI" [A CONFIRMAR] (um gerenciador de senhas). Márcia Okafor administra a organização. Denise Prado tem a coleção "Estante".
3. Quando alguém sai, os acessos que essa pessoa conhecia são trocados em até [A CONFIRMAR]. A lista está no documento 2, "Quando alguém sai".
4. Nenhum segredo por e-mail, por mensagem ou em documento compartilhado. Nunca nesta pasta.
5. Uma conta compartilhada ("admin", "root", a conta de um equipamento) só é usada se a ferramenta não oferecer contas individuais. Mesmo assim ela tem um guardião e um substituto, fica guardada no Bitwarden da escola [A CONFIRMAR] e é trocada a cada saída de alguém que a conhecia. No inventário, essas contas levam a marca "(compartilhada)".

## Inventário de acessos

| Acesso | Para que serve | Quem detém | Substituto | Guardado onde |
|---|---|---|---|---|
| Servidor: conexão à máquina (mini-PC ESTANTE01, 192.168.0.20, sala da coordenação) | Conexão técnica (SSH) para verificar, reiniciar e instalar | Denise Prado (conta "denise", criada em 09/2026); Lucas Ferreira (conta "estante", a retirar na saída; o backup e os lembretes rodam nela) | [A CONFIRMAR] | Coleção "Estante" do Bitwarden da escola [A CONFIRMAR] |
| Conta de administrador do aplicativo | Administrar o Estante | Joana Lima (conta "joana"); Lucas Ferreira (conta "lucas", a retirar na saída) | [A CONFIRMAR] | Bitwarden da escola [A CONFIRMAR] |
| Banco de dados: acesso direto às informações | Ler e mudar as informações gravadas, sem passar pelo Estante | Quem entra no mini-PC: Denise Prado | [A CONFIRMAR] | Arquivo deploy/.env no mini-PC; cópia no Bitwarden: [A CONFIRMAR] |
| Equipamentos (impressora de etiquetas Zebra GK420t) | Imprimir as etiquetas | Sem senha no painel, segundo Lucas Ferreira; se alguém mudou: [A CONFIRMAR] (compartilhada) | [A CONFIRMAR] | [A CONFIRMAR] |
| Domínio e certificado | Manter o endereço jacaranda.example.org; o cadeado do navegador se renova sozinho | Roberto, do financeiro, paga; quem tem a conta no registrador: [A CONFIRMAR] | [A CONFIRMAR] | [A CONFIRMAR] |
| E-mail biblioteca@jacaranda.example.org (MailExemplo) | Enviar os e-mails de lembrete | [A CONFIRMAR] | [A CONFIRMAR] | Senha escrita em claro no código (ver SMTP_PASSWORD abaixo) |
| Espaço onde os backups são depositados | Guardar as cópias de segurança | Quem entra no mini-PC: Denise Prado | [A CONFIRMAR] | /home/estante/backups, no mini-PC |
| Código-fonte (origem do git pull no mini-PC [A CONFIRMAR]; cópia em /home/estante/estante) | Instalar uma nova versão | Lucas Ferreira | [A CONFIRMAR] | [A CONFIRMAR] |

O roteador da escola serve para fixar o endereço da impressora na rede (192.168.0.50). Quem tem o acesso, o substituto e onde fica guardado: [A CONFIRMAR].

### Trocar e recuperar

| Acesso | Como trocar | Se for perdido ou vazar |
|---|---|---|
| Servidor | Cada pessoa troca a senha da própria conta no mini-PC; a conta "estante" é desativada depois que o backup e os lembretes passarem para outra conta [A CONFIRMAR] | Entrar no mini-PC com teclado e tela, na sala da coordenação [A CONFIRMAR] |
| Conta de administrador do aplicativo | Por outra conta de administrador, com o acordo de Márcia Okafor [A CONFIRMAR] | Denise Prado cria outra conta, com o acordo de Márcia Okafor |
| Banco de dados | Com Lucas Ferreira até 31/01/2027: a senha está em deploy/.env e em DATABASE_URL [A CONFIRMAR] | Trocar a senha e avisar Márcia Okafor: o banco tem dados pessoais dos alunos |
| Equipamentos | [A CONFIRMAR] | Etiquetas Exemplo [A CONFIRMAR] |
| Domínio e certificado | No site do registrador [A CONFIRMAR] | Roberto, do financeiro, fala com o registrador [A CONFIRMAR] |
| E-mail biblioteca@ | No painel do MailExemplo, depois mudar SMTP_PASSWORD no mini-PC [A CONFIRMAR] | Trocar a senha na hora: alguém pode mandar e-mails em nome da biblioteca |
| Espaço dos backups | Junto com o servidor | Os backups têm dados pessoais dos alunos: avisar Márcia Okafor |

Para o roteador da escola e para o código-fonte, o jeito de trocar e o que fazer se o acesso se perder não são conhecidos [A CONFIRMAR].

## Parâmetros sensíveis do sistema (só os nomes)

São ajustes lidos quando o programa liga. Aqui está só o nome. O valor fica no mini-PC.

| Nome do parâmetro | Para que serve | Onde é definido no servidor |
|---|---|---|
| POSTGRES_USER | Nome do usuário do banco de dados | deploy/.env |
| POSTGRES_PASSWORD | Senha do banco de dados | deploy/.env |
| POSTGRES_DB | Nome do banco de dados | deploy/.env |
| DATABASE_URL | Endereço que o programa usa para falar com o banco, montado com os três anteriores | deploy/docker-compose.yml |
| SECRET_KEY | Chave que protege as sessões de quem entra no Estante | deploy/.env |
| SMTP_HOST | Servidor do e-mail MailExemplo | deploy/docker-compose.yml |
| SMTP_USER | Conta de e-mail que manda os lembretes | deploy/docker-compose.yml |
| SMTP_PASSWORD | Senha dessa conta de e-mail. Está escrita em claro no arquivo: ponto aberto no documento 6 | deploy/docker-compose.yml |
| PRINTER_URL | Endereço da impressora de etiquetas na rede | deploy/.env |
| TZ | Fuso horário do programa (hora de Brasília) | deploy/docker-compose.yml |
| ADMIN_EMAIL | Aparece no arquivo de exemplo, mas nenhuma parte do programa usa [A CONFIRMAR] | deploy/.env.example |

## Backups

- Onde: /home/estante/backups, no próprio mini-PC ESTANTE01.
- Com que frequência: todo dia às 02:30, na hora do mini-PC.
- Guardados durante: 30 dias.
- Cópia fora do servidor: talvez um HD externo, copiado às vezes por Denise Prado [A CONFIRMAR]. Criptografada: não, segundo Lucas Ferreira [A CONFIRMAR].
- Última restauração provada: nunca testada, segundo Lucas Ferreira [A CONFIRMAR].
- Quem sabe restaurar: Lucas Ferreira, até 31/01/2027 [A CONFIRMAR]. O procedimento está no documento 3, "Quando for preciso".
- Quem pode ler um backup (ele contém informações pessoais): quem entra no mini-PC, hoje Denise Prado e Lucas Ferreira. Quem lê o arquivo /home/estante/backup.log: [A CONFIRMAR].

## Próximos prazos ligados a acessos

| Data | O quê (certificado, domínio, licença, senha a renovar) | Quem |
|---|---|---|
| Fim de 11/2026 | Retirar as contas de Lucas Ferreira e trocar as senhas que ele conhecia | Denise Prado |
| Todo mês | Pagamento do MailExemplo, no cartão da escola | Roberto, do financeiro |
| 31/01/2027 | Fim da disponibilidade de Lucas Ferreira | Márcia Okafor |
| 14/03/2027 | Renovação do domínio jacaranda.example.org | Roberto, do financeiro |
| Automático | Certificado do cadeado, renovado sozinho | Ninguém |

---
Este documento faz parte da pasta de passagem (6 documentos). Erro ou esquecimento? Avise Denise Prado.
