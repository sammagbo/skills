# O que o scanner de segredos recusa: especificação (sem código)

O scanner roda sobre a pasta gerada (e opcionalmente sobre `answers.yml`) antes da entrega. Qualquer ocorrência faz a verificação falhar, com arquivo e linha. Falso positivo é aceitável; falso negativo não. O usuário pode marcar uma linha como exceção só com um comentário explícito no `verification.md`, nunca silenciosamente.

## Recusado

1. Atribuições com valor onde o nome sugere segredo: `PASSWORD`, `PASSWD`, `PWD`, `SECRET`, `TOKEN`, `API_KEY`, `APIKEY`, `PRIVATE_KEY`, `ACCESS_KEY`, `CLIENT_SECRET`, `JWT`, `PIN`, `SENHA`, `MOT_DE_PASSE`, `CLE`, seguido de `=`, `:` ou `: ` e um valor não vazio que não seja um marcador (`[À CONFIRMER]`, `[A CONFIRMAR]`, `{{…}}`, `xxx`, `***`).
2. Endereços com credencial: `scheme://usuario:algo@host` (http, https, postgres, postgresql, mysql, redis, amqp, mongodb, ftp, sftp, s3), qualquer esquema.
3. Comandos com senha em argumento ou variável de ambiente: `PGPASSWORD=`, `MYSQL_PWD=`, `-p<valor>` colado, `--password=`, `--password <valor>`, `-P <valor>` em contexto de banco, `sshpass`, `curl -u usuario:senha`, `Authorization: Bearer <valor>`, `Basic <base64>`.
4. Formatos de chave e token conhecidos: `-----BEGIN … PRIVATE KEY-----`, `AKIA` + 16 caracteres (AWS), `ghp_`, `github_pat_`, `glpat-`, `sk-` + longo, `xox[abp]-`, JWT (`eyJ` + `.` + `eyJ` + `.`), `ssh-rsa AAAA`, `ssh-ed25519 AAAA`.
5b. Um bloco base64 que decodifica em texto legível é tratado como valor: um marcador de desenvolvimento guardado em base64 parece uma chave aleatória.
5. Cadeias com cara de senha: 12+ caracteres sem espaço, com pelo menos três classes (maiúscula, minúscula, dígito, símbolo), que não sejam um identificador de commit (40 ou 7 hex), um nome de arquivo, uma URL sem credencial, um IP, uma data ou um nome de parâmetro conhecido do inventário.
6. Valores inline do compose: para cada serviço do `inventory.json`, qualquer valor literal encontrado em `environment:` no compose que reapareça em qualquer documento gerado. O inventário guarda só os NOMES; para cada valor inline de nome secreto ele guarda o comprimento e o hash SHA-256, nunca o valor, e o scanner compara por hash numa janela desse comprimento. Quando o valor é igual ao nome de um serviço ou de uma imagem (o caso de `postgres`), o scanner dá um AVISO em vez de falhar: a linha é conferida à mão e anotada no `verification.md`.
7. Conteúdo de `.env`: com `--repo`, o scanner lê os arquivos `.env` do repositório só para calcular, em memória, o hash dos valores de nome secreto (6 caracteres ou mais), e falha se um deles aparecer em qualquer documento. Nada do `.env` é impresso nem gravado.

## Permitido

- Nomes de variáveis e de parâmetros, sozinhos ou em tabelas.
- `(le mot de passe est dans {{vault}})` / `(a senha está em {{vault}})`.
- Últimos quatro caracteres de um identificador quando o próprio documento os pede (raro; nunca de senha).
- Endereços sem credencial, IPs internos, portas, nomes de host.
- Identificadores de commit e tags.

## Saída do scanner

- Código 0: nada encontrado.
- Código 1: lista `arquivo:linha: categoria: trecho mascarado` (o trecho mostra os três primeiros caracteres e `…`; nunca o valor inteiro).
- Nunca grava o que encontrou em arquivo; só imprime.
