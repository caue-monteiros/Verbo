# Degrau 14 - Mini-bateria dos 3 pontos que mais travaram
# (1) os () que mandam executar; (2) o nome do for igual ao de dentro;
# (3) contador (+1, QUANTAS) x acumulador (+ valor, QUANTO)
# Feitos no simulador da conversa em 25/11 e refeitos sozinho, sem olhar a resposta, em 27/11

parcelas = [{"nome": "Ana", "valor": 100.0, "dias": 10},
            {"nome": "Bruno", "valor": 204.51, "dias": 45},
            {"nome": "Carla", "valor": 150.0, "dias": 60}]


# Exercicio 1: append com () e len
planos = []
planos.append("mensal")
planos.append("anual")
print(f"Planos: {len(planos)}")


# Exercicio 2: o apelido do for (singular) e o mesmo usado dentro do laco
alunos = [{"nome": "Ana"}, {"nome": "Bruno"}, {"nome": "Carla"}]
for aluno in alunos:
    print(f"- {aluno['nome']}")


# Exercicio 3: contador com filtro (QUANTAS parcelas tem mais de 30 dias)
atrasadas = 0
for parcela in parcelas:
    if parcela['dias'] > 30:
        atrasadas = atrasadas + 1
print(f"Atrasadas: {atrasadas}")


# Exercicio 4: acumulador com filtro (QUANTO somam as parcelas com mais de 30 dias)
total_atrasado = 0
for parcela in parcelas:
    if parcela['dias'] > 30:
        total_atrasado = total_atrasado + parcela['valor']
print(f"Total atrasado: R$ {total_atrasado:.2f}")


# Exercicio 5: funcao com acumulador e return; a funcao calcula, o print formata (:.2f)
def total_geral(parcelas):
    total = 0
    for parcela in parcelas:
        total = total + parcela['valor']
    return total

print(f"Total: R$ {total_geral(parcelas):.2f}")
