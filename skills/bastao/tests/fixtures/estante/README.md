# Estante

Estante é o sistema de empréstimo de livros da biblioteca da Escola Jacarandá (escola fictícia). A bibliotecária registra empréstimos e devoluções lendo o código de barras do livro e a carteirinha do aluno; o sistema manda um e-mail de lembrete aos responsáveis quando um livro passa do prazo e imprime as etiquetas dos livros novos.

## Stack

- Python 3.12, Flask, SQLAlchemy
- PostgreSQL 16
- Caddy (HTTPS automático) na frente do app
- Docker Compose num mini-PC da escola (sala da coordenação)

## Rodar localmente

    cp deploy/.env.example deploy/.env
    docker compose -f deploy/docker-compose.yml up -d

Acesso: https://estante.jacaranda.example.org (rede da escola e internet).

## Operação

Ver `docs/deploy.md` e `docs/incidentes.md`.
