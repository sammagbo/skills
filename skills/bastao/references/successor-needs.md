# O que um sucessor precisa no primeiro dia — lições de passagens reais

Lista extraída de passagens reais de sistemas pequenos (um servidor, docker compose, equipamentos ligados), reescrita sem dados de nenhuma organização. Serve ao agente para julgar se a pasta está completa, além do que os scripts verificam.

## O que o sucessor procura, na ordem em que procura

1. Uma página que diga o que o sistema é e o que ele não faz — porque a primeira ligação que ele recebe é sobre algo que o sistema nunca fez.
2. Quem decide — porque a segunda ligação é «posso mudar isso?».
3. O que fazer quando quebra, com o primeiro gesto sem risco — porque a terceira ligação é às 8h, com gente parada.
4. Onde estão as senhas e quem tem a chave — nunca as senhas em si.
5. O que acontece sozinho e como saber que aconteceu — backup, importação, fechamento automático.
6. As datas que vencem — licença, certificado, domínio — com quem cuida de cada uma.
7. Como instalar uma nova versão e como voltar atrás, com backup antes.
8. Quem chamar fora da casa — fornecedor do equipamento, hospedagem — com horários.
9. Onde a pasta fica e quem a atualiza — senão ela morre em um mês.

## O que costuma faltar nas passagens feitas à mão

- A palavra «migração» no guia de instalação: o sucessor instala a nova versão e o banco não acompanha.
- O ciclo anual: a importação da volta às aulas, a renovação do certificado, o arquivamento.
- A hora do servidor versus a hora local: a verificação do backup «das 3h» é feita na hora errada.
- As contas compartilhadas: existem, ninguém assume, ninguém troca na saída de alguém.
- Os acessos pessoais do desenvolvedor que ficam abertos por esquecimento.
- A prova de restauração: todo mundo tem backup; poucos já restauraram.
- A direção informada por escrito de uma data de vencimento — e não só por um aviso na tela.
- O que o sistema não faz: o sistema que não tranca portas, o relatório que não é um documento oficial, a lista que não é a chamada.

## O que o sucessor não precisa e que atrapalha

- A história do projeto e as razões de cada decisão (vai para um apêndice, se for).
- Diagramas de arquitetura para leitores não técnicos.
- Mais de uma página para «se quebrar»: ninguém lê a segunda página com gente parada na porta.
- Comandos sem a frase que diz o que se deve ver depois.

## Sinais de que a pasta está pronta

- Um leitor não técnico responde «o que você faria se o sistema caísse amanhã de manhã?» só com a pasta.
- A referência técnica consegue reinstalar a versão atual em uma máquina limpa só com o documento 3.
- O dono conhece as datas dos próximos doze meses sem abrir o sistema.
- Nenhum valor de senha, chave ou token aparece em nenhum arquivo, inclusive nos comentários e nos exemplos.
