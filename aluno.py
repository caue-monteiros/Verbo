nome = "Ana"
plano = "anual"
mensalidade = 89.90

print(f"Aluna: {nome}")
print(f"Plano: {plano}")
print(f"Mensalidade: R$ {mensalidade:.2f}")

meses_pagos = 5
total_pago = meses_pagos * mensalidade
print(f"total: R$ {total_pago:.2f}")