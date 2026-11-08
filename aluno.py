nome = input("Nome do aluno: ")
plano = input("Plano (anual ou mensal): ").strip().lower()
while plano != "anual" and plano != "mensal":
    print("Plano inválido. Digite anual ou mensal.")
    plano = input("Plano (anual ou mensal): ").strip().lower()
while True:
    try:
        mensalidade = float(input("valor da mensalidade: ").replace(",", "."))
        break
    except ValueError:
        print("Valor inválido. Digite um número, ex: 89.90")
while True:
    try:
        meses_pagos = int(input("quantos meses: "))
        break
    except ValueError:
        print("Valor inválido. Digite um número inteiro, ex: 3")
if plano == "anual":
    mensalidade = round(mensalidade * 0.85, 2)


print(f"Aluna: {nome}")
print(f"Plano: {plano}")
print(f"Mensalidade: R$ {mensalidade:.2f}")

total_pago = meses_pagos * mensalidade
print(f"total: R$ {total_pago:.2f}")





