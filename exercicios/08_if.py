# Simulador Verbo — Degrau 8: if
# Resolvidos por Cauê em 20/11/2026

# Exercício 1: desconto só no plano anual
plano = "anual"
if plano == "anual":
    print("Tem desconto de 15%")

# Exercício 2: o que fica fora do if roda sempre
plano = "mensal"
if plano == "anual":
    print("Tem desconto de 15%")
print("Fim")

# Exercício 3: maior ou igual (>=)
meses = 12
if meses >= 12:
    print("Aluno fiel")

# Exercícios 4 e 5: desconto aplicado só no anual (testado com "anual" e "mensal")
mensalidade = 100
plano = input("Plano: ")
if plano == "anual":
    mensalidade = mensalidade * 0.85
print(f"Mensalidade: R$ {mensalidade:.2f}")

# Exercício 6: limpando o texto antes de comparar
plano = input("Plano: ").strip().lower()
if plano == "anual":
    print("Plano anual confirmado")
