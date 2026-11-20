# Simulador Verbo — Aquecimento (input + int/float)
# Resolvidos por Cauê em 20/11/2026

# Exercício 1: perguntar os meses como inteiro
meses = int(input("Meses: "))
print(f"Você pagou {meses} meses")

# Exercício 2: valor como float, com 15% de desconto
valor = float(input("Valor: "))
print(f"Com desconto: R$ {valor * 0.85:.2f}")

# Exercício 3: mensalidade (float) x meses (int)
mensalidade = float(input("Mensalidade: "))
meses = int(input("Meses: "))
total = mensalidade * meses
print(f"Total: R$ {total:.2f}")
