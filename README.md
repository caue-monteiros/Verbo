# Verbo

A Verbo é uma escola de idiomas online fictícia que criei para praticar. Ela imita a operação de uma edtech de verdade: planos, mensalidades, descontos e cobrança, sem usar dados reais de nenhuma empresa.

## Por que este repositório existe

Trabalho desde 2023 no pós-vendas de uma edtech, lidando com cobrança, cancelamentos e negociação com alunos. Estou migrando para tecnologia, e aqui construo, passo a passo, ferramentas que resolvem problemas reais de uma operação como essa: dados entrando, regras de negócio aplicadas, resultados que dá para medir.

## O que já funciona

- **aluno.py**: cadastra uma turma inteira. Para cada aluno, pergunta nome, plano, mensalidade e meses pagos, aplica 15% de desconto no plano anual e guarda tudo numa ficha. No fim, mostra quantos alunos foram cadastrados, o total da turma e o total separado por plano (anual e mensal).
- **cobranca.py**: régua de cobrança. Cadastra parcelas em atraso (aluno, valor e dias de atraso), aplica multa de 2% nas parcelas com mais de 30 dias e mostra o total a recuperar e um bloco de **Prioridade** só com as parcelas mais atrasadas.
- Entradas protegidas: o programa não quebra se o aluno digitar letras no valor, aceita vírgula ou ponto e repete a pergunta até receber um plano válido.
- **exercicios/**: exercícios de fixação resolvidos (condições, laços, tratamento de erros e estrutura de programas), um arquivo por tema.

## Como rodar

    python aluno.py
    python cobranca.py

## O que aprendi construindo

- Variáveis e tipos de dado (texto, número inteiro e número decimal)
- Entrada de dados com `input()` e conversão de tipos com `int()` e `float()`
- Regras de negócio com `if`
- Padronização de texto com `.strip()` e `.lower()`
- Arredondamento de valores em dinheiro com `round()`
- Laços com `while` e `for`, validação de entrada com `try/except`
- Funções com parâmetros e `return`, para não repetir código
- Listas e dicionários: cada aluno vira uma ficha, e a turma é uma lista de fichas
- Acumuladores, contadores e filtros para gerar resumos (total geral, por plano e por prioridade)
- Estrutura de um programa: o que vem antes, dentro e depois de um laço
- Leitura de mensagens de erro e caça a bugs silenciosos
- Versionamento com Git e publicação no GitHub