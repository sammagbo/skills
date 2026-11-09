# Estante: rotina

Preparado em 09/11/2026 por Lucas Ferreira, para Marcia Okafor, Paula Reis, Joana Lima e Denise Prado.

Anote cada tarefa e cada verificação no caderno de registro. Lucas Ferreira não conhece nenhum caderno: o lugar é [A CONFIRMAR].

Escreva a data, a tarefa, quem fez e o resultado. É o mesmo caderno dos incidentes (documento 4).

A hora da máquina ESTANTE01 pode ser diferente da hora da escola. O fuso da máquina é [A CONFIRMAR]. As horas abaixo são as da máquina.

## O que acontece sozinho, e como verificar que aconteceu

| Quando | O que acontece | Como verificar | Se não aconteceu |
|---|---|---|---|
| 02:30, todos os dias | A máquina copia as informações para a pasta /home/estante/backups e apaga as cópias com mais de 30 dias | Ver se existe um arquivo estante com a data de hoje (comando em "Os comandos para colar"). O registro fica em /home/estante/backup.log | Fazer a cópia agora (ver "Os comandos para colar") e avisar Denise Prado, a referência técnica |
| 07:00, de segunda a sexta | O programa envia o e-mail de lembrete aos responsáveis dos alunos com livro atrasado há mais de 3 dias | O texto do programa não guarda registro desse envio: como verificar é [A CONFIRMAR] | Avisar Denise Prado, a referência técnica |

## Todo dia

1. Verificar que a cópia de hoje existe: comando em "Os comandos para colar" ([A CONFIRMAR], duração [A CONFIRMAR]).
2. Abrir o endereço https://estante.jacaranda.example.org e ver que a página abre ([A CONFIRMAR], duração [A CONFIRMAR]).

Esses dois gestos são uma sugestão desta pasta. Lucas Ferreira não combinou com ninguém quem os faz [A CONFIRMAR].

## Toda semana

Nenhuma tarefa semanal, segundo Lucas Ferreira.

## Todo mês

1. Manter pago o plano do e-mail MailExemplo: o plano é mensal, no cartão da escola (Roberto, do financeiro). Em 06/2026 o cartão não pagou e os lembretes pararam uma semana.

## Todo ano

| Quando | O quê | Quem | Prazo de preparação | Como |
|---|---|---|---|---|
| Fevereiro | Importar a lista de alunos, vinda da secretaria em CSV (planilha em texto). O arquivo deve estar em UTF-8 (a codificação das letras com acento) | Denise Prado [A CONFIRMAR] | [A CONFIRMAR] | Ver "Os comandos para colar". Segundo o comentário do programa, os alunos ausentes da lista ficam inativos [A CONFIRMAR] |
| No começo de cada semestre | Cadastrar os livros novos e imprimir as etiquetas | Joana Lima | [A CONFIRMAR] | [A CONFIRMAR] |
| 14/03/2027 | Renovar o domínio jacaranda.example.org, registrado pela escola | Roberto, do financeiro, paga; quem renova [A CONFIRMAR] | [A CONFIRMAR] | No site do registrador de domínios [A CONFIRMAR] |
| Fevereiro, junto com a importação | Reler os seis documentos da pasta: nomes, contatos, datas, acessos, pontos [A CONFIRMAR] restantes | Denise Prado, com Marcia Okafor | nenhum | Corrigir, mudar a data, redistribuir. O documento 5 só aos seus destinatários. |

## Quando for preciso

- Alguém citado na pasta chega ou sai: Denise Prado atualiza os documentos 2 e 5 no mesmo dia.
- Acontece um incidente novo: Denise Prado acrescenta o incidente ao documento 4 e tira dele um sintoma que sumiu. O documento continua numa página.
- Instalar uma nova versão, com o acordo de Marcia Okafor (documento 2). Até janeiro de 2027, o passo 2 só depois de falar com Lucas Ferreira. Os passos estão em "Os comandos para colar". Primeiro faça uma cópia.
- Verificar a nova versão: abrir o endereço do sistema e fazer um empréstimo de teste com o livro "TESTE-0001".
- Voltar atrás numa nova versão: o procedimento não está escrito no texto do programa [A CONFIRMAR]. Não apague nada. Guarde a cópia feita antes. Chame Denise Prado, a referência técnica.
- Se a nova versão mudou as informações gravadas, não continue sozinho: veja o item sobre restaurar uma cópia, logo abaixo.
- De onde vem o código novo: Lucas Ferreira não lembra [A CONFIRMAR]. O programa não tem endereço remoto, então `git pull` (baixar a versão nova) não funciona.
- Antes de restaurar uma cópia, salvar o estado atual: ver "Fazer a cópia agora". A restauração substitui todas as informações atuais. O que foi digitado desde a cópia restaurada se perde.
- Restaurar uma cópia: até janeiro de 2027, só depois de falar com Lucas Ferreira. Depois dessa data: [A CONFIRMAR]. O procedimento não está escrito no texto do programa [A CONFIRMAR]. Primeiro gesto seguro: não faça nada que não possa desfazer. Faça uma cópia nova e escreva a Denise Prado, a referência técnica. Última restauração provada em [A CONFIRMAR]: Lucas Ferreira acha que nunca testou.

## Os comandos para colar

Esta parte é para a referência técnica. Os demais leitores podem pular.

Os comandos rodam na máquina ESTANTE01, na pasta /home/estante/estante. Denise Prado entra com a conta denise: `ssh denise@192.168.0.20`. A senha está no Bitwarden da escola (o programa onde as senhas ficam guardadas) [A CONFIRMAR].

Se a conta denise pode rodar os comandos abaixo: [A CONFIRMAR]. O texto do programa usa a conta estante.

### Verificar

```bash
# Verificar que o programa está rodando. Não modifica nada.
# Deve aparecer: as três partes estante-db, estante-app e estante-caddy, com o estado "Up" ou "running".
cd /home/estante/estante
docker compose -f deploy/docker-compose.yml ps

# Ver as últimas mensagens do programa. Não modifica nada. Não deve aparecer: Error nem Traceback.
cd /home/estante/estante
docker compose -f deploy/docker-compose.yml logs --tail 50 app

# Verificar que o Docker (o programa que cria a caixa do sistema) liga sozinho com a máquina. Não modifica nada. Deve aparecer: enabled
systemctl is-enabled docker

# Verificar que a cópia de hoje existe. Não modifica nada.
# Deve aparecer: um arquivo estante-AAAA-MM-DD.dump com a data de hoje.
ls -l /home/estante/backups | tail -n 3

# Ver o registro da última cópia. Não modifica nada.
tail -n 5 /home/estante/backup.log
```

### Reiniciar

Só reinicie se a verificação acima não mostrar "Up". Depois, refaça a verificação.

```bash
# Reiniciar o programa.
cd /home/estante/estante
docker compose -f deploy/docker-compose.yml restart app
```

### Fazer a cópia agora

Verifique antes com o último comando de "Verificar". Depois, rode o bloco abaixo. Deve aparecer um arquivo novo, com a data de hoje.

```bash
# Fazer a cópia agora. Cria um arquivo novo.
cd /home/estante/estante
sh scripts/backup.sh
```

### Instalar uma nova versão

Faça a cópia antes. Cada bloco é um passo.

Passo 1: o código novo precisa estar na pasta /home/estante/estante. Como ele chega é [A CONFIRMAR]: Lucas Ferreira não lembra.

Passo 2: até janeiro de 2027, só depois de falar com Lucas Ferreira. Aplique cada mudança nova, na ordem dos números. Troque 00X_nome.sql pelo arquivo novo.

Quais já foram aplicadas é [A CONFIRMAR]. Denise Prado ou Lucas Ferreira verificam no lugar das informações gravadas, antes da saída dele.

```bash
# Aplicar uma mudança na forma de guardar as informações (migração). Deve aparecer: nenhuma linha com ERROR.
cd /home/estante/estante
docker exec -i estante-db sh -c 'psql -U "$POSTGRES_USER" -d "$POSTGRES_DB"' < migrations/00X_nome.sql
```

Passo 3: monte e ligue o programa de novo. Depois, faça a verificação.

```bash
# Montar e ligar o programa de novo.
cd /home/estante/estante
docker compose -f deploy/docker-compose.yml up -d --build
```

### Importar a lista de alunos

Em fevereiro. Verifique a codificação do arquivo antes. Em 19/02/2026, um arquivo com outra gravação duplicou 212 alunos.

```bash
# Verificar o arquivo. Não modifica nada. Deve aparecer: utf-8 no fim da linha.
file -i alunos.csv
```

Importe só se a verificação mostrou utf-8. Deve aparecer: "N alunos lidos".

O texto do programa recebido só conta as linhas do arquivo. Onde está o programa que importa de verdade: [A CONFIRMAR] (pergunta 18).

```bash
# Importar a lista de alunos.
cd /home/estante/estante
docker exec -i estante-app python scripts/importar_alunos.py < alunos.csv
```

---
Este documento faz parte da pasta de passagem (6 documentos). Erro ou esquecimento? Avise Denise Prado.
