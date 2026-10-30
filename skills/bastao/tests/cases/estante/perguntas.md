# Mensagens para o desenvolvedor (passo 1 e passo 2)

Cada bloco abaixo é uma mensagem separada. A mensagem seguinte só sai depois da resposta à anterior.

---

## Mensagem 0: inventário

Li o repositório em <repo> (sem abrir deploy/.env). Encontrei isto:

1. Estante: empréstimo de livros da biblioteca da Escola Jacarandá, versão v1.4.0 mais 1 commit (ba8e891).
2. Roda no mini-PC ESTANTE01 (Ubuntu 24.04, sala da coordenação, ligado no nobreak), com Docker Compose.
3. Três serviços: app (Flask), db (PostgreSQL 16, volume pgdata), caddy (HTTPS, portas 80 e 443).
4. Acesso pelo navegador em estante.jacaranda.example.org. O domínio está no registrador de domínios em nome da escola.
5. Duas tarefas agendadas: backup todo dia às 02:30 (guarda 30 dias, no próprio mini-PC) e lembretes por e-mail de segunda a sexta às 07:00.
6. Uma tarefa anual: importação dos alunos com o CSV da secretaria, em fevereiro (UTF-8 obrigatório).
7. Dependências: impressora Zebra de etiquetas (IP fixo no roteador), PC Windows da biblioteca, servidor de e-mail externo.
8. Três incidentes em docs/incidentes.md: queda de luz (11/03/2025), importação duplicada (19/02/2026), impressora (08/2026).
9. A senha do e-mail (SMTP_PASSWORD) está em claro no docker-compose.yml e no histórico git. Vai para o documento 6 como ponto aberto.
10. Não há remote git: não sei onde o código fica fora do mini-PC. ADMIN_EMAIL está no .env.example, mas o compose não usa.

O que está errado aqui?

---

## Mensagem 1

Quem é o dono do Estante a partir de dezembro (nome e cargo), e quem decide mudanças no sistema?

O README diz que a bibliotecária registra empréstimos e devoluções. Ela é a única pessoa que usa o sistema no dia a dia, ou há outras (coordenação, secretaria)?

---

## Mensagem 2

Quem tem acesso técnico ao Estante: o login SSH no mini-PC (usuário estante), o painel do registrador de domínios, a conta de e-mail que envia os lembretes, o roteador?

E onde as senhas ficam guardadas: gerenciador de senhas, cofre, envelope? Preciso só do lugar e de quem guarda. Não me mande nenhuma senha aqui.

---

## Mensagem 3

No repositório estão o backup das 02:30, os lembretes das 07:00 e a importação de alunos em fevereiro. Alguém da escola faz alguma coisa à mão todo dia, toda semana ou todo mês? E no ano, há outra tarefa além da importação (fim do ano letivo, inventário da biblioteca, livros novos para etiquetar)?

Os horários do crontab seguem o relógio do mini-PC. Ele está no horário de Brasília?

---

## Mensagem 4

O que o Estante NÃO faz, e que as pessoas tendem a achar que faz?

Achei duas pistas: os lembretes saem só por e-mail (sem SMS nem WhatsApp), e a migração 002 tem o comentário "multa desativada", mas o SQL só cria a coluna "ativo". O sistema cobra multa ou não?

---

## Mensagem 5

Em docs/incidentes.md há três incidentes: o site que não voltou depois da queda de luz (11/03/2025), os 212 alunos duplicados na importação (19/02/2026) e a impressora que mudou de IP (08/2026). São esses os três mais prováveis de voltar a acontecer? Há algum outro que quase aconteceu e não foi anotado?

E se o Estante parar no meio do dia, como a bibliotecária continua emprestando livros (caderno, planilha)?

---

## Mensagem 6

Quando algo falha, quem a escola chama primeiro, e depois? Há alguém de TI na escola?

Até onde a bibliotecária ou a coordenação pode ir sozinha: reiniciar o mini-PC, religar o nobreak, reiniciar a impressora? O que só a referência técnica pode fazer?

---

## Mensagem 7

O backup.sh grava um arquivo por dia em /home/estante/backups e apaga os que têm mais de 30 dias. Tudo fica no próprio mini-PC. Existe alguma cópia fora dessa máquina (pendrive, nuvem, outro computador)? Essa cópia é criptografada?

Quando foi a última vez que alguém restaurou um desses backups e conferiu que funcionava? Quem fez?

---

## Mensagem 8

Há prazos ou custos que vencem? O Caddy renova o certificado HTTPS sozinho. Mas qual é a data de vencimento do domínio jacaranda.example.org no registrador de domínios, e quem na escola paga? O serviço de envio de e-mail tem plano, contrato ou limite que vence?

---

## Mensagem 9

Dependências externas que encontrei: a impressora Zebra, o roteador da escola (onde está a reserva do IP 192.168.0.50), o PC Windows da biblioteca, o serviço de e-mail, o registrador de domínios e o nobreak. Para cada uma, quem é o contato (empresa ou pessoa)?

O leitor de código de barras e o de carteirinha não aparecem no repositório. Que modelo são, e quem cuida deles?

---

## Mensagem 10

Pelo seu pedido, a pasta sai só em português, na pasta passagem/. Confirma? Quem vai ler (direção, bibliotecária, TI da escola) e quem recebe o sistema no seu lugar (nome e cargo)?

Você sai no fim de novembro. Depois disso, continua disponível? Em que condições (prazo, horários, pago ou não) e por qual contato?

O repositório não tem remote. Onde o código vai ficar para quem vier depois?
