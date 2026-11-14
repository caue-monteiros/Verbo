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

def ler_plano(pergunta):
    while True:
        plano = input(pergunta).strip().lower()
        if plano in ("mensal","anual"):
            return plano
        print("Inválido. Só existem planos anuais ou mensais")

def ler_nome(pergunta):
    while True:
        nome = input(pergunta).strip()
        if nome != "":
            return nome
        print("Insira algum nome.")

turma = []
while True:
    nome = ler_nome("Nome do aluno: ")
    plano = ler_plano("Plano (anual ou mensal): ")
    mensalidade = ler_valor("valor da mensalidade: ")
    meses_pagos = ler_inteiro("quantos meses: ")
    mensalidade = aplicar_desconto(mensalidade, plano)


    print(f"Aluno: {nome}")
    print(f"Plano: {plano}")
    print(f"Mensalidade: R$ {mensalidade:.2f}")

    total_pago = meses_pagos * mensalidade
    print(f"total: R$ {total_pago:.2f}")
    ficha = {"nome": nome, "plano": plano, "total": total_pago}
    turma.append(ficha)

    continuar = input("Cadastrar outro aluno? (s/n): ").strip().lower()
    if continuar != "s":
        break

print(f"Alunos cadastrados: {len(turma)}")
total_turma = 0
print("Turma:")
for ficha in turma:
    print(f"- {ficha['nome']}: R$ {ficha['total']:.2f}")
    total_turma = total_turma + ficha['total']
print(f"Total da turma: R$ {total_turma:.2f}")



