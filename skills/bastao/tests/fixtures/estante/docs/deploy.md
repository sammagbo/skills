# Deploy

O sistema roda no mini-PC "ESTANTE01" (Ubuntu 24.04), na sala da coordenação, ligado no nobreak.

1. `ssh estante@192.168.0.20`
2. `cd ~/estante && git pull`
3. Aplicar as migrações novas, na ordem: `docker exec -i estante-db psql -U estante -d estante < migrations/00X_nome.sql`
4. `docker compose -f deploy/docker-compose.yml up -d --build`
5. Abrir https://estante.jacaranda.example.org e fazer um empréstimo de teste com o livro "TESTE-0001".

O domínio jacaranda.example.org é registrado no registrador de domínios pela escola. O certificado HTTPS é renovado sozinho pelo Caddy.
