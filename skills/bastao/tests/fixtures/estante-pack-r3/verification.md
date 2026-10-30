# Verificação da pasta Estante (passo 4), 30/10/2026

Os scripts do Bastão ainda não existem. Cada verificação foi feita à mão ou com um script provisório fora da pasta, seguindo os contratos do SKILL.md e de references/secret-patterns.md.

## 1. Segredos

- Resultado: nenhum segredo nos 12 documentos nem em answers.yml.
- Verificado: atribuições com nome de segredo, endereços com credencial, senha em comando, formatos de chave e token conhecidos, sequências com cara de senha.
- Valores escritos direto no docker-compose.yml: comparados por hash com cada palavra dos documentos. Nenhum aparece.
- Falsos positivos corrigidos no script provisório: palavras com acento ou apóstrofo ("Propriétaire", "Código-fonte", "L'imprimante") contavam como senha.
- Não feito: a comparação com as linhas de deploy/.env (regra 7 do scanner). A regra do teste proíbe abrir esse arquivo.
- Segredo em claro no repositório: SMTP_PASSWORD (deploy/docker-compose.yml, gravado no commit 16590fd e no histórico git). O valor não foi reproduzido. Está como ponto aberto no documento 6 e no documento 5.

## 2. Cobertura

- Variáveis: as 11 do inventário estão explicadas no documento 5, nas duas línguas. São POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_DB, DATABASE_URL, SECRET_KEY, SMTP_HOST, SMTP_USER, SMTP_PASSWORD, PRINTER_URL, TZ e ADMIN_EMAIL.
- Tarefas agendadas: as duas estão no documento 3 (backup às 02:30, lembretes às 07:00).
- Serviços: o documento 1 descreve onde o programa roda (mini-PC, endereço do site, onde ficam as informações) em linguagem corrente. Os nomes app, db e caddy aparecem no documento 3, na verificação.
- Nenhum `{{campo}}` sem preencher. Nenhum comentário de modelo sobrou.

### Marcadores restantes por documento (FR = PT)

| Documento | Marcadores |
|---|---|
| 01 | 7 |
| 02 | 46 |
| 03 | 17 |
| 04 | 6 |
| 05 | 60 |
| 06 | 18 |

Total: 154 por língua.

Os quatro campos da regra 3 (vault, last_restore_date, backup_offsite, backup_encrypted) continuam marcados. O documento 5 traz, ao lado de cada um, o que o desenvolvedor disse. O dono, Marcia Okafor, ainda precisa confirmar de viva voz.

## 3. Tamanho (palavras contadas no texto sem a sintaxe Markdown)

| Documento | FR | PT | Limite |
|---|---|---|---|
| 01 | 380 | 378 | 350 a 380 |
| 04 | 379 | 378 | cerca de 380 |
| 06 | 376 | 356 | cerca de 350 a 380 |

O que foi cortado para chegar a esses números:

- Documento 1, primeira versão com 549 palavras:
  - "não se conecta sozinho ao sistema da secretaria" virou parte da linha da importação, em "O que ele faz".
  - Saíram da lista de dependências: os leitores, o domínio e o modelo do nobreak. Eles continuam no documento 5.
- Documento 4, primeira versão com 484 palavras:
  - Os três sintomas foram mantidos e os textos encurtados.
  - Provedor Exemplo saiu da tabela "Quem chamar" e ficou na linha do sintoma "o site não abre".
  - A importação duplicada (19/02/2026) não virou sintoma. Ela está nas três coisas proibidas e no procedimento anual do documento 3.
  - O incidente de 06/2026 (MailExemplo) entrou como sintoma 3.
- Documento 6, primeira versão com 427 palavras:
  - Nenhuma caixa foi retirada. Só a redação foi encurtada.

## 4. Paridade FR / PT

Comparados nos seis pares de documentos:

- Os títulos, na mesma ordem e no mesmo nível, com o mesmo sentido.
- O mesmo número de marcadores.
- O mesmo número de linhas de tabela.
- O mesmo número de caixas de seleção.

Resultado: idênticos nos seis pares.

## 5. Estilo

Verificado mecanicamente fora dos blocos de código:

- Travessões, negrito em listas, aspas curvas no PT, emoji, ponto do meio, títulos em Title Case.
- As listas de palavras de references/writing-style.md.
- Frases com mais de 35 palavras.

Corrigido:

- Três frases acima de 35 palavras, divididas: documento 2 ("Quando alguém sai", desenvolvedor) e documento 3 (instalar nova versão), nas duas línguas.
- A frase do cofre no documento 5 encurtada. Saiu o exemplo entre parênteses do modelo, porque o lugar já tem nome.
- Jargão nos documentos 1, 4 e 6 trocado pela expressão corrente:
  - PT: "backup" virou "cópia de segurança".
  - "commit" virou "alteração" (PT) e "modification" (FR).
- Datas de mês no documento 4 em formato 08/2026 e 06/2026.

Palavras sinalizadas e mantidas de propósito:

- "o mesmo" (documento 3 PT, "É o mesmo caderno dos incidentes"): texto fixo do modelo, adjetivo, não pronome.
- "a mesma" (documento 6 PT, "é a mesma do código-fonte recebido"): texto fixo do modelo.

Frases entre 26 e 31 palavras mantidas, todas abaixo de 35:

- documento 3, cabeçalho (texto fixo);
- documento 4 FR, "Après l'incident" (texto fixo);
- documento 4 PT, primeira linha de "Antes de tudo";
- documento 5, regra 5 (texto fixo).

Leitura como leitor. Pergunta: "o que soa como máquina?" Mudanças:

- Linhas de função no documento 1 reduzidas a substantivo e uso.
- Sem frase de encerramento.
- Ninguém chamado por sinônimo: "le propriétaire" / "o dono" e "le référent technique" / "a referência técnica" em todos os documentos.

Pergunta: "às 8h, com gente esperando, a pessoa sabe o que fazer?" Resposta: só em parte. A solução de emergência (como emprestar sem o sistema) não foi combinada. O que Joana Lima pode fazer sozinha também não. Os dois estão marcados e o primeiro é ponto aberto no documento 6.

## Decisões tomadas sem o usuário

- Nome do desenvolvedor: marcado [À CONFIRMER] / [A CONFIRMAR]. Ele não deu o nome. O endereço lucas.ferreira.dev@example.com sugere um, mas sugerir não é responder.
- Quem e quando, nos pontos abertos do documento 6: marcados. São campos do dia da recepção. Ficaram preenchidos só os prazos que decorrem das respostas: saída no fim de novembro de 2026, disponibilidade até 31/01/2027.
- Data do backup visto e incidente percorrido (documento 6): espaços em branco para preencher à mão (`__/__/____`, `________`). São campos do dia da recepção, não informações que faltam.
- Linhas retiradas do documento 5:
  - "Hébergeur / Provedor de hospedagem": a máquina é da escola, não há provedor.
  - "Clé de licence / Chave de licença": o repositório não mostra nenhuma.
- Linhas acrescentadas ao documento 5, a partir das respostas: Bitwarden, roteador, conta do MailExemplo, internet Provedor Exemplo.
- Os nomes ficaram como o usuário escreveu, sem acento ("Marcia", "Direcao > TI > Estante"). Ele escreve sem acento em tudo, então o acento real é [A CONFIRMAR].
- Contradição encontrada: docs/deploy.md manda fazer `git pull`, mas o repositório não tem remote. A pergunta "de onde vem a nova versão" ficou marcada no documento 3. "Onde fica o código-fonte" é ponto aberto no documento 6.
- Contradição nas respostas: o desenvolvedor diz "nunca sem mim até janeiro" para migrações e restauração (resposta 6). Ele também diz que não mexe no servidor depois de sair (resposta 10). A pasta escreve "com o desenvolvedor", por e-mail. Quem assume essas tarefas depois de 31/01/2027 está marcado.
