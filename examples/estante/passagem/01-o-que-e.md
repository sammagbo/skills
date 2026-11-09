# Estante: o que é e o que não faz

Preparado em 09/11/2026 por Lucas Ferreira, para a direção e a equipe de TI.

## Em uma frase

Estante serve para registrar empréstimos e devoluções de livros da biblioteca da Escola Jacarandá. Quem usa: Joana Lima, bibliotecária.

## O que ele faz

- Registra empréstimos e devoluções, com o código de barras do livro e a carteirinha.
- Manda e-mail de lembrete aos responsáveis, quando um livro passa de 3 dias de atraso. Às 07:00, de segunda a sexta.
- Imprime a etiqueta dos livros novos.

Lucas Ferreira diz que tudo isso funciona. O texto entregue só o descreve: documento 6.

## O que ele não faz

- Não bloqueia a saída do livro. Não tem portal antifurto, mas a escola acha que tem.
- Não manda SMS nem WhatsApp.
- Não cobra multa: desativada em 2025, por decisão da direção.
- Não se liga à secretaria: a lista de alunos é importada à mão.

## Onde ele roda

- Na máquina ESTANTE01, na sala da coordenação, ligada num nobreak.
- Três partes: estante-app (o programa da tela), estante-db (as informações) e estante-caddy (o cadeado do endereço).
- Acesso: navegador, em estante.jacaranda.example.org.
- As informações são copiadas todo dia às 02:30, na mesma máquina. Cópia fora dela: Lucas Ferreira acha que Denise Prado copia às vezes para um disco externo [A CONFIRMAR].

## Quem é responsável

| Papel | Nome e cargo | O que essa pessoa decide ou faz |
|---|---|---|
| Dono do sistema | Marcia Okafor, diretora pedagógica | Decide as mudanças |
| Referência técnica | Denise Prado, técnica de informática | Primeira pessoa a chamar |
| Desenvolvedor de origem | Lucas Ferreira | Sai em 11/2026. Dúvidas por e-mail até 31/01/2027 |

## O que tem data

| Prazo | O quê | Quem cuida | Se for esquecido |
|---|---|---|---|
| 14/03/2027 | Renovação do domínio | Roberto, do financeiro (paga); quem renova: [A CONFIRMAR] | [A CONFIRMAR] |
| Todo mês | Plano do e-mail MailExemplo | Roberto, do financeiro (paga) | Lembretes pararam em 06/2026 |

## As três coisas que nunca se deve fazer

1. Desligar a opção que liga o programa com a máquina: em 11/03/2025 o sistema não voltou após uma queda de luz.
2. Importar alunos sem verificar os acentos: em 19/02/2026 a importação duplicou 212 alunos.
3. Mudar o endereço da impressora de etiquetas: em 08/2026 ela parou de imprimir.

---
Este documento faz parte da pasta de passagem (6 documentos). Erro ou esquecimento? Avise Denise Prado.
