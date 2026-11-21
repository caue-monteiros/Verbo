def ler_nome(pergunta):
    while True:
        nome = input(pergunta).strip()
        if nome != "":
            return nome
        print("Insira algum nome.")

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
            print("Valor inválido. Digite um número, ex: 15")

def aplicar_multa(valor, dias):
    if dias > 30:
        return round(valor * 1.02, 2)
    return valor

parcelas = []
while True:
    nome = ler_nome("Nome do aluno: ")
    valor = ler_valor("Valor da parcela: ")
    dias = ler_inteiro("Dias de atraso: ")
    valor_atualizado = aplicar_multa(valor, dias)
    print(f"Valor atualizado: R$ {valor_atualizado:.2f}")

    ficha =  {"nome": nome, "dias": dias, "valor": valor_atualizado}
    parcelas.append(ficha)

    continuar = input("Cadastrar outra? (s/n): ").strip().lower()
    if continuar != "s":
        break

print(f"Parcelas cadastradas: {len(parcelas)}")
total = 0
for ficha in parcelas:
    total = total + ficha['valor']
print(f"Total a recuperar: R$ {total:.2f}")

print("Prioridade (mais de 30 dias)")
total_prioridade = 0
for ficha in parcelas:
    if ficha['dias'] > 30:
        print(f"- {ficha['nome']}: R$ {ficha['valor']:.2f}")
        total_prioridade = total_prioridade + ficha['valor']
print(f"Total prioridade: R$ {total_prioridade:.2f}")