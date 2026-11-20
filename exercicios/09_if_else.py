# Simulador Verbo — Degrau 9: if / else
# Resolvidos por Cauê em 20/11/2026

# Exercício 1: com desconto ou valor cheio
plano = "mensal"
if plano == "anual":
    print("Com desconto")
else:
    print("Valor cheio")

# Exercício 2: desconto conforme o plano digitado
plano = input("Plano: ")
if plano == "anual":
    print("Desconto: 15%")
else:
    print("Desconto: 0%")

# Exercício 3: conta dentro das chaves do f-string
meses = int(input("Meses pagos: "))
if meses >= 12:
    print("Plano completo")
else:
    print(f"Faltam {12 - meses} meses")

# Exercício 4: continuar o cadastro?
continuar = input("Cadastrar outro? (s/n): ")
if continuar == "s":
    print("Vamos lá!")
else:
    print("Cadastro encerrado.")

# Exercício 5: nome vazio
nome = input("Nome: ").strip()
if nome != "":
    print(f"Olá, {nome}!")
else:
    print("Insira algum nome.")

# Exercício 6: total conforme o plano
plano = input("Plano: ")
valor = float(input("Valor: "))
if plano == "anual":
    total = valor * 0.85
else:
    total = valor
print(f"Total: R$ {total:.2f}")
