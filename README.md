# Verbo

A Verbo é uma escola de idiomas online fictícia que criei para praticar. Ela imita a operação de uma edtech de verdade: planos, mensalidades, descontos e cobrança, sem usar dados reais de nenhuma empresa.

## Por que este repositório existe

Trabalho desde 2023 no pós-vendas de uma edtech, lidando com cobrança, cancelamentos e negociação com alunos. Estou migrando para tecnologia, e aqui construo, passo a passo, ferramentas que resolvem problemas reais de uma operação como essa: dados entrando, regras de negócio aplicadas, resultados que dá para medir.

## O que já funciona

- **aluno.py**: cadastra uma turma inteira. Para cada aluno, pergunta nome, plano, mensalidade e meses pagos, aplica 15% de desconto no plano anual e guarda tudo numa ficha. No fim, mostra quantos alunos foram cadastrados, o total da turma e o total separado por plano (anual e mensal).
- Entradas protegidas: o programa não quebra se o aluno digitar letras no valor, aceita vírgula ou ponto e repete a pergunta até receber um plano válido.
- **exercicios/**: exercícios de fixação resolvidos (condições, laços e tratamento de erros), um arquivo por tema.

## Como rodar

    python aluno.py

## O que aprendi construindo

- Variáveis e tipos de dado (texto, número inteiro e número decimal)
- Entrada de dados com `input()` e conversão de tipos com `int()` e `float()`
- Regras de negócio com `if`
- Padronização de texto com `.strip()` e `.lower()`
- Arredondamento de valores em dinheiro com `round()`
- Laços com `while` e `for`, validação de entrada com `try/except`
- Funções com parâmetros e `return`, para não repetir código
- Listas e dicionários: cada aluno vira uma ficha, e a turma é uma lista de fichas
- Acumuladores e filtros para gerar resumos (total geral e por plano)
- Leitura de mensagens de erro e caça a bugs silenciosos
- Versionamento com Git e publicação no GitHub