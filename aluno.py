nome = input("Nome do aluno: ")
plano = input("nome do plano: ")
mensalidade = float(input("valor da mensalidade: "))
meses_pagos = int(input("quantos meses: "))
if plano == "anual":
    mensalidade = mensalidade * 0.85

print(f"Aluna: {nome}")
print(f"Plano: {plano}")
print(f"Mensalidade: R$ {mensalidade:.2f}")

total_pago = meses_pagos * mensalidade
print(f"total: R$ {total_pago:.2f}")




