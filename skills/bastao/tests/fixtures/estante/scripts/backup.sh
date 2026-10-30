#!/bin/sh
# Backup diário da base. Guarda 30 dias em /home/estante/backups.
set -e
DEST=/home/estante/backups
mkdir -p "$DEST"
docker exec estante-db sh -c 'pg_dump -U "$POSTGRES_USER" -d "$POSTGRES_DB" -F c' > "$DEST/estante-$(date +%F).dump"
find "$DEST" -name 'estante-*.dump' -mtime +30 -delete
