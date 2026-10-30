# Incidentes

- 11/03/2025 — Depois de uma queda de luz longa, o site não voltou. O nobreak descarregou e o Docker não subiu sozinho porque o serviço estava desabilitado no boot. Corrigido com `systemctl enable docker`.
- 19/02/2026 — Importação de alunos duplicou 212 alunos: o CSV veio em Latin-1 e os nomes com acento não bateram. Apagamos os duplicados à mão e o script passou a exigir UTF-8.
- 08/2026 — A impressora de etiquetas parou de imprimir depois de uma atualização do Windows do PC da biblioteca (mudou o IP). Voltou fixando o IP 192.168.0.50 no roteador.
