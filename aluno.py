def aplicar_desconto(valor, plano):
    if plano == "anual":
        return round(valor * 0.85, 2)
    return valor

def ler_valor(pergunta):
    while True:
        try:
            return float(input(pergunta).replace(",","."))
        except ValueError:
            print("Valor inválido. Digite um número, ex: 89.90")


def ler_inteiro(pergunta):
    while True:
        try:
            return int(input(pergunta))
        except ValueError:
            print("Valor inválido. Digite um número inteiro, ex: 3")

nome = input("Nome do aluno: ")
plano = input("Plano (anual ou mensal): ").strip().lower()
while plano != "anual" and plano != "mensal":
    print("Plano inválido. Digite anual ou mensal.")
    plano = input("Plano (anual ou mensal): ").strip().lower()
mensalidade = ler_valor("valor da mensalidade: ")
meses_pagos = ler_inteiro("quantos meses: ")

mensalidade = aplicar_desconto(mensalidade, plano)


print(f"Aluna: {nome}")
print(f"Plano: {plano}")
print(f"Mensalidade: R$ {mensalidade:.2f}")

total_pago = meses_pagos * mensalidade
print(f"total: R$ {total_pago:.2f}")





