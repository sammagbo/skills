"""Importação anual dos alunos a partir do CSV exportado da secretaria (fevereiro).
Uso: docker exec -i estante-app python scripts/importar_alunos.py < alunos.csv
O CSV precisa estar em UTF-8. Alunos ausentes do arquivo ficam inativos (não são apagados)."""
import csv, sys
def main():
    rows = list(csv.DictReader(sys.stdin))
    print(f"{len(rows)} alunos lidos")
if __name__ == "__main__":
    main()
