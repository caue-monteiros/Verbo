# Simulador Verbo — Degrau 11: try / except
# Resolvidos por Cauê em 20/11/2026

# Exercícios 1 e 2: valor inválido x valor certo (testado com "abc" e "89.9")
try:
    valor = float(input("Valor: "))
    print("Valor ok")
except ValueError:
    print("Valor inválido")

# Exercício 3: inteiro
try:
    meses = int(input("Meses: "))
except ValueError:
    print("Digite um número inteiro, ex: 3")

# Exercício 4: aceitar vírgula
valor = float(input("Valor: ").replace(",", "."))
print(f"Registrado: R$ {valor:.2f}")

# Exercício 5: repetir até vir um número
while True:
    try:
        mensalidade = float(input("Mensalidade: "))
        break
    except ValueError:
        print("Digite um número, ex: 89.90")
print(f"Mensalidade: R$ {mensalidade:.2f}")

# Exercício 6: o mesmo com inteiro
while True:
    try:
        meses = int(input("Meses: "))
        break
    except ValueError:
        print("Digite um número inteiro")
total = meses * 85
print(f"Total: R$ {total}")
