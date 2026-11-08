nome = input("Nome do aluno: ")
plano = input("nome do plano: ").strip().lower()
mensalidade = float(input("valor da mensalidade: "))
meses_pagos = int(input("quantos meses: "))
if plano == "anual":
    mensalidade = round(mensalidade * 0.85, 2)   # vira 76.42


print(f"Aluna: {nome}")
print(f"Plano: {plano}")
print(f"Mensalidade: R$ {mensalidade:.2f}")

total_pago = meses_pagos * mensalidade
print(f"total: R$ {total_pago:.2f}")





