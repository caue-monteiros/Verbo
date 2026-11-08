# Verbo

A Verbo é uma escola de idiomas online fictícia que criei para praticar. Ela imita a operação de uma edtech de verdade: planos, mensalidades, descontos e cobrança, sem usar dados reais de nenhuma empresa.

## Por que este repositório existe

Trabalho há 3 anos no pós-vendas de uma edtech, lidando com cobrança, cancelamentos e negociação com alunos. Estou migrando para tecnologia, e aqui construo, passo a passo, ferramentas que resolvem problemas reais de uma operação como essa: dados entrando, regras de negócio aplicadas, resultados que dá para medir.

## O que já funciona

- **aluno.py**: pergunta os dados do aluno (nome, plano, mensalidade e meses pagos), aplica 15% de desconto no plano anual e calcula o total pago. Aceita o plano digitado de qualquer jeito (maiúsculas, minúsculas, espaços sobrando) e arredonda os valores em centavos, para a mensalidade e o total sempre baterem.

## Como rodar

    python aluno.py

## O que aprendi construindo

- Variáveis e tipos de dado (texto, número inteiro e número decimal)
- Entrada de dados com `input()` e conversão de tipos com `int()` e `float()`
- Regras de negócio com `if`
- Padronização de texto com `.strip()` e `.lower()`
- Arredondamento de valores em dinheiro com `round()`
- Leitura de mensagens de erro e caça a bugs silenciosos
- Versionamento com Git e publicação no GitHub