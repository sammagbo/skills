# Bastão — dicionário de campos (`{{chave}}`)

Regras: chaves em inglês, únicas por sentido, iguais nos modelos FR e PT (só o texto ao redor muda). Uma chave usada em linhas repetidas (tabela, lista) tem o mesmo sentido em cada linha. Origem: Q1…Q10 = pergunta ao desenvolvedor; repo = lido do repositório pelo inventário; fixo = constante; auto = calculado na geração; recepção = preenchido no dia da entrega. Nenhum campo recebe valor de segredo, endereço com credencial ou comando com senha.

## Globais (vários documentos)

| Chave | Significado | Origem | Docs |
|---|---|---|---|
| system_name | Nome do sistema | repo (README, compose) + confirmar | 1–6 |
| doc_date | Data de geração do documento | auto | 1–6 |
| author | Desenvolvedor que entrega (nome) | Q10 / git | 1–6 |
| readers | Leitores do documento | Q10 | 1, 3, 4 |
| doc_count | Número de documentos da pasta | fixo (6) | 1–6 |
| corrections_contact | A quem avisar erros ou esquecimentos | Q10 | 1–6 |
| owner | Dono do sistema (nome e cargo) | Q1 | 1, 2, 4, 5, 6 |
| tech_lead | Referência técnica (nome e cargo) | Q2 / Q6 | 1, 2, 4, 5, 6 |
| developer_availability | Condições em que o desenvolvedor continua disponível | Q10 | 1, 2, 4 |
| vault | Lugar de referência onde os segredos ficam guardados | Q2 | 3, 5 |
| logbook | Caderno de registro de rotina e incidentes | Q3 / Q5 | 3, 4 |
| repo_location | Onde está o código-fonte | repo (git remote) | 5, 6 |
| repo_version | Versão ou commit entregue | repo (git) | 6 |
| param_name | Nome de um parâmetro sensível (nunca o valor) | repo | 3 (comentário), 5 |
| backup_frequency | Frequência do backup | Q7 / repo | 1, 5 |
| last_restore_date | Data da última restauração provada | Q7 | 3, 5 |
| update_owner | Quem mantém a pasta atualizada | Q10 | 3 |

## Documento 1 — o que é e o que não faz

| Chave | Significado | Origem |
|---|---|---|
| purpose_plain | Finalidade em linguagem corrente | repo (README) + Q1 |
| users | Quem usa o sistema | Q1 |
| feature / feature_users / feature_when | Uma função, quem a usa, quando (linha repetida) | repo + Q1 |
| not_feature / not_feature_reason | O que não faz e por que alguém acharia que faz (linha repetida) | Q4 |
| server_location | Onde o programa roda, em linguagem corrente | repo (deploy) + confirmar |
| access_mode | Como se acessa (aplicativo, navegador) | repo + confirmar |
| external_dependencies | Equipamentos, serviços e rede de que depende | Q9 |
| storage_plain | Onde as informações ficam gravadas, em linguagem corrente | repo (compose) |
| due_date / due_item / due_owner / due_consequence | Um prazo, o que vence, quem cuida, consequência (linha repetida) | Q8 |
| forbidden_1 … forbidden_3 / forbidden_1_reason … | As três coisas a nunca fazer e as razões | Q5 / Q9 |

## Documento 2 — quem faz o quê

| Chave | Significado | Origem |
|---|---|---|
| person_name / person_title / person_contact | Pessoa, cargo, contato profissional (linha repetida) | Q1 / Q2 |
| operator_location | Onde atua o operador do dia a dia | Q1 |
| decision_maker / decision_consulted / decision_informed | Para cada uma das cinco decisões fixas: quem decide, quem é consultado, quem é avisado | Q1 |
| task / task_owner / task_deputy / task_frequency / task_if_missed | Tarefa recorrente, responsável, substituto, frequência, consequência (linha repetida) | Q3 |
| role | Papel (operador, vida escolar, TI…) — linha repetida nas três últimas tabelas | Q6 |
| alone_list / with_owner_list / never_without_tech_list | O que o papel pode fazer sozinho, com acordo do dono, nunca sem a referência técnica | Q6 |
| account / access_level_plain / custody_place | Conta do papel, nível em linguagem corrente, onde fica guardada | Q2 |
| transfer_what / transfer_to / accesses_to_change | Na saída de um papel: o que transferir, para quem, que acessos trocar | Q2 / Q6 |

## Documento 3 — rotina

| Chave | Significado | Origem |
|---|---|---|
| auto_time / auto_task / auto_check / auto_if_missed | Tarefa automática: quando (hora do servidor ou local), o quê, como verificar, o que fazer se não rodou (linha repetida) | repo (cron, scripts) |
| step / step_how / step_owner / step_duration | Gesto de rotina, como exatamente, quem, duração (linha repetida; sem duração nas listas semanal e mensal) | Q3 |
| period / yearly_task / yearly_owner / lead_time / yearly_procedure | Tarefa anual (linha repetida) | Q3 |
| review_period / review_owner | Linha fixa: releitura anual da pasta | Q10 |
| event / event_procedure / event_owner | Evento eventual e seu procedimento (linha repetida) | Q3 |
| backup_procedure | Como fazer um backup agora | repo (scripts) / Q7 |
| upgrade_procedure / upgrade_check / rollback_procedure | Instalar nova versão, verificar, voltar atrás | repo (deploy) + Q3 |
| restore_procedure | Como restaurar um backup | repo / Q7 |
| expected_state / check_command | Estado esperado e comando de verificação (não modifica nada) | repo (compose, systemd) |
| error_word / log_command | Palavra que indica problema e comando que mostra as mensagens | repo |
| restart_command | Comando de reinício | repo |

## Documento 4 — se quebrar

| Chave | Significado | Origem |
|---|---|---|
| blocked_example / fallback_procedure | Exemplo de pessoas bloqueadas e solução de emergência (como continuar sem o sistema) | Q5 / Q6 |
| symptom_N / symptom_N_check / symptom_N_cause / symptom_N_action / symptom_N_fixed_when / symptom_N_who / symptom_N_how | Para N = 1, 2, 3 (4 no máximo): sintoma, verificação sem risco, causa provável, o que fazer sozinho, sinal de que voltou, quem chamar, como | Q5 / Q6 |
| tech_lead_contact / tech_lead_hours | Contato e horários da referência técnica | Q6 |
| vendor / vendor_scope / vendor_contact / vendor_hours | Fornecedor ou prestador, para quê, contato, horários | Q9 |
| author_contact / author_hours | Contato e horários do desenvolvedor | Q10 |

## Documento 5 — custódia de acessos

| Chave | Significado | Origem |
|---|---|---|
| access_change_deadline | Prazo para trocar acessos quando alguém sai | Q2 |
| equipment_type | Tipo de equipamento (terminal, câmera, leitor) | Q9 / repo |
| access_use / access_holder / access_deputy / access_place | Para cada linha fixa do inventário: para que serve, quem detém, substituto, onde fica guardado | Q2 |
| access_change_procedure / access_loss_recovery | Para cada linha: como trocar; o que acontece e o que fazer se for perdido ou vazar | Q2 |
| param_role_plain / param_location | Para cada parâmetro sensível: papel em linguagem corrente, onde é definido | repo |
| backup_location / backup_retention / backup_offsite / backup_encrypted | Onde, por quanto tempo, cópia fora do servidor, criptografado | Q7 |
| last_restore_by / restore_person / backup_readers | Quem provou a última restauração; quem sabe restaurar; quem pode ler um backup | Q7 |
| due_date / due_item / due_owner | Prazos ligados a acessos (mesmas chaves do documento 1; o documento 5 é a referência) | Q8 |

## Documento 6 — checklist de recepção

| Chave | Significado | Origem |
|---|---|---|
| successor / successor_title / successor_role | Quem recebe, cargo, papel no sistema | Q10 |
| installed_version / installed_date | Versão instalada e data | repo / máquina |
| main_access | Acesso principal que o sucessor usa | Q2 |
| expected_result | Resultado esperado da verificação diária (documento 3) | repo |
| backup_seen_date | Data do backup visto na recepção | recepção |
| drill_incident | Incidente do documento 4 percorrido em simulação | recepção |
| dossier_location | Onde a pasta fica guardada | Q10 |
| open_point / open_point_owner / open_point_due | Ponto a resolver antes da assinatura, quem, para quando (linha repetida) | recepção |
