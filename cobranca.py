from decimal import Decimal, InvalidOperation, ROUND_HALF_UP

LIMITE_DIAS = 30
PERCENTUAL_MULTA = Decimal("0.02")
CENTAVOS = Decimal("0.01")

def ler_nome(pergunta):
    while True:
        nome = input(pergunta).strip()
        if nome != "":
            return nome
        print("Insira algum nome.")

def ler_valor(pergunta):
    while True:
        try:
            valor = Decimal(input(pergunta).strip().replace(",", "."))
            if valor.is_finite():
                return valor
        except InvalidOperation:
            pass
        print("Valor inválido. Digite um número, ex: 89.90")

def ler_inteiro(pergunta):
    while True:
        try:
            return int(input(pergunta))
        except ValueError:
            print("Valor inválido. Digite um número inteiro, ex: 15")

def aplicar_multa(valor, dias):
    if dias > LIMITE_DIAS:
        return (valor * (1 + PERCENTUAL_MULTA)).quantize(CENTAVOS, rounding=ROUND_HALF_UP)
    return valor

parcelas = []
while True:
    nome = ler_nome("Nome do aluno: ")
    valor = ler_valor("Valor da parcela: ")
    dias = ler_inteiro("Dias de atraso: ")
    valor_atualizado = aplicar_multa(valor, dias)
    print(f"Valor atualizado: R$ {valor_atualizado:.2f}")

    ficha = {"nome": nome, "dias": dias, "valor": valor_atualizado}
    parcelas.append(ficha)

    continuar = input("Cadastrar outra? (s/n): ").strip().lower()
    if continuar != "s":
        break

print(f"Parcelas cadastradas: {len(parcelas)}")
total = Decimal("0")
for ficha in parcelas:
    total += ficha['valor']
print(f"Total a recuperar: R$ {total:.2f}")

print(f"Prioridade (mais de {LIMITE_DIAS} dias)")
total_prioridade = Decimal("0")
for ficha in parcelas:
    if ficha['dias'] > LIMITE_DIAS:
        print(f"- {ficha['nome']}: R$ {ficha['valor']:.2f}")
        total_prioridade += ficha['valor']
print(f"Total prioridade: R$ {total_prioridade:.2f}")
