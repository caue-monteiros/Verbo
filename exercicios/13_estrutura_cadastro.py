# Degrau 13 - Antes, dentro, depois (cadastro com while True)

# Exercicio 1: cadastro numa lista com while True, append e len
planos = []
while True:
    plano = input("Plano: ")
    planos.append(plano)
    continuar = input("Outro? (s/n): ")
    if continuar != "s":
        break
print(f"Planos cadastrados: {len(planos)}")


# Exercicio 2 (conserte): nomes = [] saiu de dentro do while e subiu para antes dele
nomes = []
while True:
    nome = input("Nome: ")
    nomes.append(nome)
    continuar = input("Outro? (s/n): ")
    if continuar != "s":
        break
print(f"Cadastrados: {len(nomes)}")


# Exercicio 3: cada cadastro vira uma ficha (dicionario); resumo com for depois do while
parcelas = []
while True:
    nome = input("Nome: ")
    valor = float(input("Valor: "))
    ficha = {"nome": nome, "valor": valor}
    parcelas.append(ficha)
    outro = input("Outro? (s/n): ")
    if outro != "s":
        break
for ficha in parcelas:
    print(f"- {ficha['nome']}: R$ {ficha['valor']:.2f}")

