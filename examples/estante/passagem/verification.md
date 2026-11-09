# Verificação da pasta de passagem

Run: 09/11/2026, commit 1e3f9c2
Status: draft
Second folder: passation

## Checks

- inventory.py: executado de novo. Sem diferença no inventário (sem o bloco git): inventory.json mantido, inventory.new.json apagado.
- Arquivos da lista do sucessor: `git diff --name-only 1e3f9c2` não lista nenhum arquivo rastreado; `git status --short` lista só deploy/.env (não aberto, já existia na primeira rodada) e a pasta da passagem. A mudança que disparou esta rodada é o conjunto de respostas novas em 00-perguntas.md.
- secret_scanner.py: 0 findings, em passagem e em passation.
- coverage_check.py (passagem, com --pair passation): 0 problemas, 0 avisos. Palavras (documentos 1, 4 e 6): português 399, 392, 377; francês 400, 400, 397. Marcas [A CONFIRMAR]: 3, 38, 27, 7, 44, 9; [À CONFIRMER]: 3, 38, 27, 7, 44, 9.
- style_check.py: 0 flags, em passagem e em passation.
- Marcas dos quatro campos da regra 3 (cofre, última restauração, cópia fora da máquina, criptografia): conferidas dentro da frase, nos documentos 1, 2, 3, 5 e 6, nas duas línguas.
- Leitura final como leitor (checklist de references/writing-style.md): feita nos documentos mudados. Nenhuma linha reescrita depois do script.

## Fixed

- Respostas 1 a 12 e C1 a C3 lidas e levadas para answers.yml e para os documentos 1 a 6. Perguntas movidas para "Respondidas"; o que ficou aberto virou as perguntas 16 a 28.
- Autor do histórico (Lucas Ferreira), dono, referência técnica, leitores, local da pasta e quem atualiza deixaram de levar a marca, porque as respostas 1, 2, 6 e 10 os dão.
- Documento 4: quarto incidente (lembretes, 06/2026) entrou; a impressora (08/2026) saiu por ser o sintoma que para menos gente e está na pergunta 16, para a qual a linha "Outros sintomas" aponta.
- Língua francesa criada (pasta passation), porque a resposta 10 pede cópia em francês. Português continua primeiro.
- Documentos 1, 4 e 6 de novo dentro de 400 palavras; linha "Sem solução de emergência" e conta lucas ficaram só nos documentos 2, 4 e 5 por falta de espaço no 6.

## Still marked

- Documento 1: 3. Documento 2: 38. Documento 3: 27. Documento 4: 7. Documento 5: 44. Documento 6: 9 (nas duas línguas).
- Sem resposta ainda (perguntas 13 a 28): quem confere a cópia, confirmação da Marcia Okafor sobre cofre, última restauração, cópia fora da máquina e criptografia, conta estante e senha do painel da Zebra, telefones dos fornecedores e contatos das pessoas, solução de emergência, quem importa em fevereiro, caderno de registro, decisões restantes, quem mexe nas migrações e restaura cópias depois de janeiro de 2027, quem renova o domínio e validade da bateria do nobreak, endereço da impressora, quem recebe a pasta e quem abre o Drive.

## Still to rewrite

Nenhum.

## Words kept on purpose

- "Docker", "git", "SSH", "CSV", "UTF-8" e "Bitwarden" nos documentos 2, 3 e 5, explicados na primeira vez em cada documento. Não aparecem nos documentos 1, 4 e 6 (só o nome Bitwarden, no documento 6, com a frase que diz onde as senhas ficam).
- "portal antifurto" (documento 1): é o equipamento da saída da biblioteca, não a tela do programa.
- "Google Drive"/"Drive" (documento 6): nome do produto onde a pasta fica.

## Words chosen

- "a caixa do programa" (documento 4) para o contêiner Docker.
- "texto do programa" para o repositório, nos documentos 1, 3 e 6.
- "cópia" no lugar de "backup" nos documentos 1, 4 e 6. No francês, "copie" nesses três e "sauvegarde" nos documentos 2, 3 e 5. No português dos documentos 2, 3 e 5 a rodada também escreveu "cópia", e não "backup" como a tabela de palavras aprovadas manda: divergência conhecida, não corrigida.
- "dono" é Marcia Okafor, pela resposta 1. "Referência técnica" é Denise Prado, porque a resposta 6 a põe em primeiro na ordem de chamada e a resposta 2 lhe dá o acesso técnico: ninguém usou a expressão. Nenhuma pergunta pede ainda essa confirmação.
- "Erro ou esquecimento? Avise Denise Prado": a resposta 10 diz que ela atualiza a pasta; nenhuma resposta nomeia quem recebe os avisos de erro.
- "Roberto" sem sobrenome (a resposta não o dá).

## Contradictions found

- README e comentários dos programas dizem que os lembretes, as etiquetas e a importação funcionam; Lucas Ferreira confirma na resposta 11 (09/11/2026). Os arquivos app/lembretes.py (função vazia), app/etiquetas.py (só descrição) e scripts/importar_alunos.py (só conta linhas) não contêm o trecho que faz o trabalho. Está nos documentos 1 e 6, e na pergunta 18.
- docs/deploy.md manda rodar "git pull", mas o repositório não tem endereço remoto (inventário). Lucas Ferreira não lembra de onde vem o código novo (resposta C3, 09/11/2026). Está nos documentos 3 e 6, e na pergunta 17.
- migrations/002_ativo.sql: comentário "multa desativada", comando acrescenta a coluna "ativo". A resposta 12 (09/11/2026) diz que a coluna de multa foi desativada em 2025 por decisão da direção, e não diz que foi essa mudança. Fica o que a resposta diz, no documento 1.
- O comentário de scripts/importar_alunos.py diz que os alunos ausentes ficam inativos, mas o programa só conta linhas; Lucas Ferreira não lembra de ter mexido (resposta 4). Documento 3, com a marca; a linha saiu do documento 1 por falta de espaço.
- Segredo escrito sem proteção: SMTP_PASSWORD em deploy/docker-compose.yml. Valor não copiado. Está no documento 6.
- O comando de migração de docs/deploy.md tinha o nome do usuário e do banco escritos. O documento 3 usa as variáveis do contêiner (regra 10).
- Resposta 10 (09/11/2026): a pasta fica no Google Drive da escola, em Direção, TI, Estante, e os leitores são quatro pessoas. O documento 5 vai só a Marcia Okafor e Denise Prado (regra 7). Quem pode abrir essa pasta não foi dito. Mantido o que a resposta diz; ponto aberto no documento 6 e pergunta 28.
- Resposta 6 (09/11/2026): "nunca sem mim, até jan/2027" para migrações e restauração de cópia. Resposta 10: ele sai no fim de novembro de 2026 e só responde dúvidas por e-mail, sem mexer na máquina. As duas juntas deixam essas duas tarefas sem quem as faça. Documentos 2, 3, 5 e 6; pergunta 25.
- Resposta 9: o endereço fixo da impressora é de 08/2026 (mais de 30 dias). Lucas Ferreira diz que não mudou, mas não sabe se alguém mexeu depois. Documento 4 pergunta se é o mesmo; pergunta 27.

## Fingerprints

| File | SHA-256 |
|---|---|
| passagem/01-o-que-e.md | 250e0b443751a3e370011fcfb805b81627d198d3d3a24dd2bf50174d3c76ed26 |
| passagem/02-quem-faz-o-que.md | 5f74e57f329d1278b67462abe1b9a6865c835a8c9c6c8c3254760f0bfc7c1f35 |
| passagem/03-rotina.md | 4446c04b8b497228a57a5b36fb6fc172f550f60026d6f1f04a040604a43a4036 |
| passagem/04-se-quebrar.md | 2f0dc54f58da695d222d5a8f72d27ceff2c1ec321c5f716b2f6161a26e9b66db |
| passagem/05-custodia-de-acessos.md | 5959330c066777d88b75d63b67502c52e3a25217d371a728d40f90b9292e9213 |
| passagem/06-checklist-de-recepcao.md | 9394984f697a5dc47ef7b6cc9523056018e1e8baf1ccbb753e84295c45662f4f |
| passation/01-ce-que-cest.md | 22a6863867ac1c2223ebb69ada63297dc9d02f9b7d8015b7ad6a6a984dc11af0 |
| passation/02-qui-fait-quoi.md | c3f78d7bde3feaa1b3f91d7a6ba095eac002986e73538a90f417a36f15a250d4 |
| passation/03-routine.md | 5aae4473421e2e027fe3706d82f390379f7efbdbd91fe620b285c8516d9142cd |
| passation/04-si-ca-casse.md | fad6d01d1b6d4b31a6dbba402a8d95007e2a96ca42efec1cf7664d95ef017b46 |
| passation/05-garde-des-acces.md | 81d65399874c7a7a14385f053176b6b9a36cc5b493e7475d12205be8e14d1fec |
| passation/06-checklist-reception.md | f7c28a5b0d8e6c8f3aa67f89a030df40500d13107cedc2a0f2d3cc8411f37ed4 |

## History

### 09/11/2026, commit 1e3f9c2

Primeira rodada. Repositório lido: README, docs de instalação e de incidentes, compose, crontab, scripts. deploy/.env existe e não foi aberto.
Nenhuma resposta ainda. Pasta em português, uma língua; a segunda vem com a pergunta 10.
Documentos 1 a 6, 00-perguntas.md, answers.yml e inventory.json criados.

### 09/11/2026, commit 1e3f9c2 (rodada disparada pelo hook)

Repositório sem mudança nos arquivos que a pasta descreve (inventário igual). Respostas 1 a 12 e C1 a C3 chegaram em 00-perguntas.md.
Resposta 10 pede francês também: pasta passation criada, a partir do português já verificado. Perguntas 13 a 28 abertas ou reescritas.
Documentos 1 a 6 mudaram nas duas línguas; 00-perguntas.md e answers.yml reescritos.

### 09/11/2026, revisão à mão depois de quatro juízes

Correções em 26 linhas, nas duas línguas: versão instalada do programa (documento 6), vencimento do domínio sem frequência inventada (documentos 2 e 3), aviso de que o texto entregue só conta as linhas na importação (documento 3), francês "dédoublé", "paie" e uma frase sem verbo, português "conferir", "Operador" e "administradora".
Nenhuma resposta nova. Marcas: documento 3 e documento 6 com uma marca a mais cada, nas duas línguas.
Impressões digitais recalculadas sobre os arquivos corrigidos.
