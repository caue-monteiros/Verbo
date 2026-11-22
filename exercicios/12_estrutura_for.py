# Degrau 12 - Antes, dentro, depois (for)

# Exercicio 1: somar os meses pagos com for e acumulador
meses = [12, 6, 3]
total = 0
for mes in meses:
    total = total + mes
print(f"Meses pagos: {total}")

# Exercicio 2 (conserte): total = 0 subiu para antes do for e o print desceu para depois
valores = [100, 204.51, 153]
total = 0
for valor in valores:
    total = total + valor

print(f"Total: R$ {total:.2f}")


# Exercicio 3: contador com filtro (if dentro do for)
dias = [10, 45, 60, 30]
contador = 0
for dia in dias:
    if dia > 30:
        contador = contador + 1
print(f"Parcelas com mais de 30 dias: {contador}")

# Aquecimento (22/11): contador com filtro de texto
planos = ["anual", "mensal", "anual", "anual"]
contador = 0
for plano in planos:
    if plano == "anual":
        contador = contador + 1
print(f"Alunos no plano anual: {contador}")

# Exercicio 4: lista nova com append dentro do for
valores = [100, 200.5, 150]
com_multa = []
for valor in valores:
    com_multa.append(round(valor * 1.02, 2))
print(com_multa)

# Exercicio 5: fichas com filtro e acumulador (3 niveis de recuo)
parcelas = [
    {"nome": "Ana", "dias": 10, "valor": 100},
    {"nome": "Bruno", "dias": 45, "valor": 204.51},
    {"nome": "Carla", "dias": 60, "valor": 153},
]
total = 0
for ficha in parcelas:
    if ficha['dias'] > 30:
        print(f"- {ficha['nome']}: R$ {ficha['valor']:.2f}")
        total = total + ficha['valor']
print(f"Total prioridade: R$ {total:.2f}")
