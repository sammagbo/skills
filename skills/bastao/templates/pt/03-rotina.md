# {{system_name}}: rotina

Preparado em {{doc_date}} por {{author}}, para {{readers}} (quem faz o sistema funcionar no dia a dia).

Cada gesto feito e cada verificação são anotados em {{logbook}}: a data, o gesto, quem fez, o resultado. É o mesmo caderno dos incidentes (documento 4).

<!-- Resposta à pergunta 3, completada pelo repositório (scripts, tarefas agendadas, backups, importações).
     Cada gesto é escrito para ser executado, não compreendido: o comando exato para colar, ou a tela e o botão exatos.
     Nenhum comando que modifica algo sem dizer antes como verificar que deu certo.
     Nunca uma senha ou um token num comando ou numa captura de tela; nenhum endereço com credencial (usuario:senha@…, token numa URL); nenhum comando com senha como argumento ou variável de ambiente. Quando um procedimento exigir um segredo, escrever "(a senha está em {{vault}})".
     Se o repositório contiver um valor em claro (docker-compose, script), nunca reproduzi-lo: registrar como ponto a resolver no documento 6 ("segredo em claro no repositório: {{param_name}}").
     Dizer se a hora é a do servidor ou a local, quando forem diferentes.
     O que o repositório não prova e o dono não confirmou fica [A CONFIRMAR]. Escrever como uma pessoa (references/writing-style.md). -->

## O que acontece sozinho, e como verificar que aconteceu

<!-- Tarefas agendadas encontradas no repositório (cron, tarefas do sistema, scripts). Uma linha por tarefa: quando (hora do servidor ou hora local, dizer qual), o quê, e como ver que rodou.
     A coluna "Se não aconteceu" dá o gesto, ou remete a um sintoma que existe de fato no documento 4. -->

| Quando | O que acontece | Como verificar | Se não aconteceu |
|---|---|---|---|
| {{auto_time}} | {{auto_task}} | {{auto_check}} | {{auto_if_missed}} |

## Todo dia

<!-- Três a cinco gestos no máximo. Se a lista for maior, alguma coisa deveria ser automatizada: anotar no documento 6, "O que falta resolver". -->

1. {{step}}: {{step_how}} ({{step_owner}}, cerca de {{step_duration}}).
2. {{step}}: {{step_how}} ({{step_owner}}, cerca de {{step_duration}}).

## Toda semana

1. {{step}}: {{step_how}} ({{step_owner}}).

## Todo mês

1. {{step}}: {{step_how}} ({{step_owner}}).

## Todo ano

<!-- A parte que se perde: volta às aulas, importação das listas, renovações, arquivamento, virada de ano. Pôr o período habitual e o prazo de preparação. A última linha (releitura da pasta) é fixa. -->

| Quando | O quê | Quem | Prazo de preparação | Como |
|---|---|---|---|---|
| {{period}} | {{yearly_task}} | {{yearly_owner}} | {{lead_time}} | {{yearly_procedure}} |
| {{review_period}} | Reler os seis documentos da pasta: nomes, contatos, datas, acessos, pontos [A CONFIRMAR] restantes | {{review_owner}} | nenhum | Corrigir, redatar, redistribuir. O documento 5 só aos seus destinatários. |

## Quando for preciso

<!-- Nova pessoa a cadastrar, saída de alguém, troca ou pane de equipamento, nova versão do programa, restauração de um backup. As quatro últimas linhas são fixas. -->

- {{event}}: {{event_procedure}} ({{event_owner}}).
- Alguém citado na pasta chega ou sai: {{update_owner}} atualiza os documentos 2 e 5 no mesmo dia.
- Acontece um incidente novo: {{update_owner}} acrescenta ao documento 4 e tira dele um sintoma que não acontece mais, para o documento continuar numa página.
- Instalar uma nova versão, com o acordo previsto no documento 2 ("Quem decide o quê"). Primeiro um backup: {{backup_procedure}}. Depois: {{upgrade_procedure}}. Verificar que deu certo: {{upgrade_check}}. Se não deu, voltar atrás: {{rollback_procedure}}. Se a nova versão mudou as informações gravadas, recuperá-las também a partir do backup.
- Restaurar um backup. Atenção: isso substitui todas as informações atuais pelas do backup, e tudo o que foi digitado desde então se perde. Primeiro salvar o estado atual ({{backup_procedure}}), depois {{restore_procedure}}. Última restauração provada em {{last_restore_date}}. <!-- mesma data que o documento 5, "Backups" -->

## Os comandos para colar

Esta parte é para a referência técnica. Os demais leitores podem pular.

<!-- Cada comando vem precedido do que ele faz e seguido do que se deve ver. Os comandos de verificação primeiro (eles não modificam nada), o comando que modifica depois, nunca encadeados numa linha só. -->

```bash
# Verificar que o programa está rodando. Não modifica nada. Deve aparecer: {{expected_state}}
{{check_command}}

# Ver as últimas mensagens do programa. Não modifica nada. Não deve aparecer: {{error_word}}
{{log_command}}

# Reiniciar o programa. Só se a verificação acima não mostrar {{expected_state}}. Depois, refazer a verificação.
{{restart_command}}
```

---
Este documento faz parte da pasta de passagem ({{doc_count}} documentos). Erro ou esquecimento? Avise {{corrections_contact}}.
