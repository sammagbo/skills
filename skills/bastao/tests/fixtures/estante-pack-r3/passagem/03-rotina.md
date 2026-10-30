# Estante: rotina

Preparado em 30/10/2026 pelo desenvolvedor de origem (nome [A CONFIRMAR]), para Denise Prado e Joana Lima (quem faz o sistema funcionar no dia a dia).

Cada gesto feito e cada verificação são anotados no caderno de registro [A CONFIRMAR]: a data, o gesto, quem fez, o resultado. É o mesmo caderno dos incidentes (documento 4).

## O que acontece sozinho, e como verificar que aconteceu

Os horários são os do relógio do mini-PC. O fuso horário dele nunca foi conferido [A CONFIRMAR]. O programa tem o seu próprio ajuste de hora (parâmetro TZ, documento 5).

| Quando | O que acontece | Como verificar | Se não aconteceu |
|---|---|---|---|
| Toda noite às 02:30 (hora do mini-PC) | Backup das informações em /home/estante/backups. As cópias com mais de 30 dias são apagadas. | Há um arquivo estante-AAAA-MM-DD.dump com a data do dia em /home/estante/backups. Os erros ficam em /home/estante/backup.log. | Denise Prado roda um backup manual (ver "Quando for preciso"). |
| De segunda a sexta às 07:00 (hora do mini-PC) | Envio de um e-mail às famílias de cada aluno com livro atrasado há mais de 3 dias | [A CONFIRMAR]: essa tarefa não escreve em nenhum arquivo de registro | Documento 4, "As famílias não recebem mais os lembretes" |

## Todo dia

Nenhum gesto manual conhecido em 30/10/2026. A verificação de que o programa está rodando está em "Os comandos para colar".

## Toda semana

Nenhum gesto conhecido em 30/10/2026.

## Todo mês

Nenhum gesto conhecido em 30/10/2026. O plano do MailExemplo é pago todo mês com o cartão da escola (Roberto, financeiro). Em junho de 2026, um pagamento que faltou parou os e-mails por uma semana.

## Todo ano

| Quando | O quê | Quem | Prazo de preparação | Como |
|---|---|---|---|---|
| Fevereiro | Importar a lista de alunos | [A CONFIRMAR] | [A CONFIRMAR] | Pedir à secretaria o arquivo CSV (uma tabela em texto) dos alunos. Verificar que ele está salvo em UTF-8. Fazer um backup (ver "Quando for preciso"). Rodar `docker exec -i estante-app python scripts/importar_alunos.py < alunos.csv`. Verificar que o número mostrado ("N alunos lidos") é o número de linhas do arquivo. Os alunos que não estão no arquivo ficam inativos, não são apagados. |
| Começo de cada semestre | Cadastrar os livros novos e imprimir as etiquetas | Joana Lima | [A CONFIRMAR] | Telas e botões: [A CONFIRMAR]. A impressora é a Zebra GK420t da biblioteca, no endereço 192.168.0.50. |
| Antes de 14/03/2027 | Renovar o endereço jacaranda.example.org no registrador de domínios | Roberto, financeiro | [A CONFIRMAR] | Na área do cliente do registrador de domínios. Quem tem acesso: [A CONFIRMAR]. |
| Fevereiro | Reler os seis documentos da pasta: nomes, contatos, datas, acessos, pontos [A CONFIRMAR] restantes | Denise Prado, com Marcia Okafor | nenhum | Corrigir, redatar, redistribuir. O documento 5 só aos seus destinatários. |

## Quando for preciso

- Criar uma conta de administrador no Estante: com o acordo de Marcia Okafor, como exatamente [A CONFIRMAR] (Denise Prado).
- Depois de uma queda de luz longa: quando a energia voltar, verificar que o programa está rodando ("Os comandos para colar"). O Docker (o programa que faz rodar as caixas do sistema) liga sozinho com a máquina desde 11/03/2025 (Denise Prado).
- Alguém citado na pasta chega ou sai: Denise Prado atualiza os documentos 2 e 5 no mesmo dia.
- Acontece um incidente novo: Denise Prado acrescenta ao documento 4 e tira dele um sintoma que não acontece mais, para o documento continuar numa página.
- Instalar uma nova versão, com o acordo previsto no documento 2 ("Quem decide o quê"). Primeiro um backup: rodar `/home/estante/estante/scripts/backup.sh` no mini-PC (qual conta tem permissão: [A CONFIRMAR]). Verificar que apareceu um arquivo com a data do dia em /home/estante/backups. Depois: entrar no mini-PC (192.168.0.20) com a sua conta e ir para /home/estante/estante. Buscar a nova versão (de onde: [A CONFIRMAR], o repositório não tem endereço remoto). Aplicar na ordem as migrações novas (atualizações da forma como as informações são organizadas): `docker exec -i estante-db psql -U estante -d estante < migrations/00X_nome.sql`. Então rodar `docker compose -f deploy/docker-compose.yml up -d --build`. Até 31/01/2027, migrações só com o desenvolvedor. Verificar que deu certo: abrir estante.jacaranda.example.org e fazer um empréstimo de teste com o livro "TESTE-0001". Se não deu, voltar atrás: [A CONFIRMAR]. Se a nova versão mudou as informações gravadas, recuperá-las também a partir do backup.
- Restaurar um backup. Atenção: isso substitui todas as informações atuais pelas do backup, e tudo o que foi digitado desde então se perde. Primeiro salvar o estado atual (rodar `/home/estante/estante/scripts/backup.sh` e verificar o arquivo novo), depois [A CONFIRMAR]: o repositório não tem nenhum procedimento de restauração. Até 31/01/2027, nunca sem o desenvolvedor. Última restauração provada em [A CONFIRMAR].

## Os comandos para colar

Esta parte é para a referência técnica. Os demais leitores podem pular.

```bash
# Verificar que o programa está rodando. Não modifica nada. Deve aparecer: três linhas, estante-app, estante-db e estante-caddy, cada uma com "Up"
docker ps --filter name=estante

# Ver as últimas mensagens do programa. Não modifica nada. Não deve aparecer: Traceback ou Error
docker logs --tail 50 estante-app

# Reiniciar o programa. Só se a verificação acima não mostrar as três linhas com "Up". Depois, refazer a verificação.
docker compose -f /home/estante/estante/deploy/docker-compose.yml restart
```

---
Este documento faz parte da pasta de passagem (6 documentos). Erro ou esquecimento? Avise Denise Prado.
