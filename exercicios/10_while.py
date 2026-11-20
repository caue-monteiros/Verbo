# Simulador Verbo — Degrau 10: while
# Resolvidos por Cauê em 20/11/2026

# Exercício 1: contador de meses
mes = 1
while mes <= 3:
    print(f"Mês {mes}")
    mes = mes + 1

# Exercício 2: parcelas
parcelas = 1
while parcelas <= 4:
    print(f"Parcela {parcelas} de 4")
    parcelas = parcelas + 1

# Exercício 3: acumulador (zero antes, soma dentro, mostra depois)
mes = 1
total = 0
while mes <= 12:
    total = total + 85
    mes = mes + 1
print(f"Total do ano: R$ {total}")

# Exercício 4: while True + break
while True:
    resposta = input("Digite sair: ")
    if resposta == "sair":
        break
    print("Ainda não")
print("Saiu do laço")

# Exercício 5: repetir até vir um plano válido
while True:
    plano = input("Plano: ").strip().lower()
    if plano in ("anual", "mensal"):
        break
    print("Plano inválido")
print(f"Plano escolhido: {plano}")

# Exercício 6: contando cadastros
alunos = 0
while True:
    nome = input("Nome: ")
    alunos = alunos + 1
    continuar = input("Outro? (s/n): ")
    if continuar != "s":
        break
print(f"Alunos cadastrados: {alunos}")
