# Estante: rotina

Preparado em 30/10/2026 por Lucas Ferreira, para Márcia Okafor, Paula Reis, Joana Lima e Denise Prado (quem faz o sistema funcionar no dia a dia).

Cada gesto feito e cada verificação são anotados em [A CONFIRMAR]: a data, o gesto, quem fez, o resultado. É o mesmo caderno dos incidentes (documento 4).

## O que acontece sozinho, e como verificar que aconteceu

As horas abaixo são as do relógio do mini-PC ESTANTE01. Se esse relógio está na hora de Brasília: [A CONFIRMAR]. O programa usa America/Sao_Paulo (a hora de Brasília).

| Quando | O que acontece | Como verificar | Se não aconteceu |
|---|---|---|---|
| 02:30, todo dia | O script backup.sh grava uma cópia das informações (backup) em /home/estante/backups, no próprio mini-PC, e apaga as cópias com mais de 30 dias | Existe um arquivo estante-AAAA-MM-DD.dump com a data do dia, e o arquivo /home/estante/backup.log não mostra erro | Denise Prado faz um backup na hora (comandos no fim) e avisa Lucas Ferreira até 31/01/2027 |
| 07:00, de segunda a sexta | O programa app.lembretes manda um e-mail aos responsáveis de cada aluno com livro atrasado há mais de 3 dias | Não há registro próprio. O sinal é um responsável dizer que não recebeu. | Ver o sintoma "Os responsáveis não recebem os e-mails de lembrete" no documento 4 |

## Todo dia

1. Verificação da manhã: abrir https://estante.jacaranda.example.org no navegador e ver a tela do Estante ([A CONFIRMAR] quem faz, decisão de Márcia Okafor; cerca de [A CONFIRMAR]).

## Toda semana

Nenhum gesto semanal definido em 30/10/2026.

## Todo mês

1. Pagamento do e-mail MailExemplo: o plano é mensal, no cartão da escola (Roberto, do financeiro).

## Todo ano

| Quando | O quê | Quem | Prazo de preparação | Como |
|---|---|---|---|---|
| Fevereiro | Importar a lista dos alunos, a partir do arquivo CSV da secretaria | Denise Prado | Pedir o arquivo à secretaria antes; quem pede: [A CONFIRMAR] | O arquivo tem de estar em UTF-8. Os alunos que não estão no arquivo ficam inativos, não são apagados. Comandos no fim. |
| Começo de cada semestre | Cadastrar os livros novos e imprimir as etiquetas | Joana Lima | nenhum | Na tela do Estante [A CONFIRMAR] |
| Antes de 14/03/2027 | Renovar o domínio jacaranda.example.org (o endereço do site, alugado todo ano) | Roberto, do financeiro | [A CONFIRMAR] | No registrador de domínios da escola, nome [A CONFIRMAR] |
| Fevereiro | Reler os seis documentos da pasta: nomes, contatos, datas, acessos, pontos [A CONFIRMAR] restantes | Denise Prado com Márcia Okafor | nenhum | Corrigir, redatar, redistribuir. O documento 5 só aos seus destinatários. |

## Quando for preciso

- Uma etiqueta saiu errada ou não saiu: reimprimir a etiqueta, de um jeito ainda não escrito [A CONFIRMAR] (Denise Prado).
- Uma nova conta de administrador no Estante: criar com o acordo de Márcia Okafor (Denise Prado).
- Alguém citado na pasta chega ou sai: Denise Prado atualiza os documentos 2 e 5 no mesmo dia.
- Acontece um incidente novo: Denise Prado acrescenta ao documento 4 e tira dele um sintoma que não acontece mais, para o documento continuar numa página.
- Instalar uma nova versão, com o acordo previsto no documento 2 ("Quem decide o quê"). Primeiro um backup: rodar o script backup.sh (comandos no fim). Depois: seguir os passos de "Instalar uma nova versão" nos comandos no fim. Se a versão trouxer uma migração (atualização da forma como as informações são organizadas), só com Lucas Ferreira até 31/01/2027. Verificar que deu certo: abrir https://estante.jacaranda.example.org e fazer um empréstimo de teste com o livro "TESTE-0001". Se não deu, voltar atrás: o procedimento não está escrito [A CONFIRMAR]. Se a nova versão mudou as informações gravadas, recuperá-las também a partir do backup.
- Restaurar um backup. Atenção: isso substitui todas as informações atuais pelas do backup, e tudo o que foi digitado desde então se perde. Primeiro salvar o estado atual (rodar o script backup.sh), depois chamar Lucas Ferreira: o procedimento não está escrito, e até 31/01/2027 só se faz com ele [A CONFIRMAR]. Última restauração provada em: nunca testada, segundo Lucas Ferreira [A CONFIRMAR].

## Os comandos para colar

Esta parte é para a referência técnica. Os demais leitores podem pular.

Todos os comandos rodam no mini-PC ESTANTE01, depois de entrar nele pela conexão técnica (SSH). Se a conta "denise" tem permissão para usar o Docker e para gravar em /home/estante/backups: [A CONFIRMAR].

```bash
# Entrar no mini-PC pela rede da escola. (a senha está no Bitwarden da escola [A CONFIRMAR])
ssh denise@192.168.0.20

# Verificar que o programa está rodando. Não modifica nada. Deve aparecer: estante-db, estante-app e estante-caddy, cada um com "Up"
docker ps --filter name=estante

# Verificar que o Docker volta sozinho depois de uma queda de luz. Não modifica nada. Deve aparecer: enabled
systemctl is-enabled docker

# Ver as últimas mensagens do programa. Não modifica nada. Não deve aparecer: Traceback
docker logs --tail 50 estante-app

# Reiniciar o programa. Só se a verificação acima não mostrar "Up". Depois, refazer a verificação.
docker restart estante-db estante-app estante-caddy
```

```bash
# Fazer um backup na hora. Depois, o arquivo do dia deve aparecer na lista.
/home/estante/estante/scripts/backup.sh
ls -l /home/estante/backups | tail -3
```

```bash
# Importação anual. Primeiro verificar o formato do arquivo. Não modifica nada. Deve aparecer a palavra utf-8
file -i alunos.csv

# Só se apareceu utf-8: importar. Deve aparecer o número de alunos lidos.
docker exec -i estante-app python scripts/importar_alunos.py < alunos.csv
```

Instalar uma nova versão (docs/deploy.md), com o acordo de Márcia Okafor e depois de um backup:

1. Entrar na pasta do código e baixar a nova versão. A origem desse download não está confirmada [A CONFIRMAR].
2. Aplicar as migrações novas, uma por uma, na ordem dos números (só com Lucas Ferreira até 31/01/2027).
3. Reconstruir e religar o programa.
4. Refazer a verificação acima.
5. Fazer um empréstimo de teste com o livro "TESTE-0001".

```bash
# Passo 1
cd /home/estante/estante && git pull

# Passo 2, uma vez por migração nova, trocando 00X_nome.sql pelo nome do arquivo
docker exec -i estante-db sh -c 'psql -U "$POSTGRES_USER" -d "$POSTGRES_DB"' < migrations/00X_nome.sql

# Passo 3
docker compose -f deploy/docker-compose.yml up -d --build
```

---
Este documento faz parte da pasta de passagem (6 documentos). Erro ou esquecimento? Avise Denise Prado.
