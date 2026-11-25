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


# Exercicio 5 (final): a regua de cobranca inteira de memoria
# Cadastro com multa de 2% acima de 30 dias; resumo com len, acumulador do total
# e um segundo for com if para a prioridade (dados sempre da ficha da volta)
def aplicar_multa(valor, dias):
    if dias > 30:
        return round(valor * 1.02, 2)
    return valor

parcelas = []
while True:
    nome = input("Nome: ")
    valor = float(input("Valor: "))
    dias = int(input("Quantos dias em atraso: "))
    valor_atualizado = aplicar_multa(valor, dias)
    ficha = {"nome": nome, "valor": valor_atualizado, "dias": dias}
    parcelas.append(ficha)
    outro = input("Outro? (s/n): ")
    if outro != "s":
        break
print(f"Parcelas: {len(parcelas)}")
total = 0
for ficha in parcelas:
    total = total + ficha['valor']
print(f"Total: R$ {total:.2f}")
print("Prioridade:")
for parcela in parcelas:
    if parcela['dias'] > 30:
        print(f"- {parcela['nome']}: R$ {parcela['valor']:.2f}")


# Exercicio gemeo: contador (+1, QUANTAS) e acumulador (+ preco, QUANTO) no mesmo for
matriculas = [{"plano": "mensal", "preco": 89.9}, {"plano": "anual", "preco": 799.0}, {"plano": "mensal", "preco": 89.9}]

quantidade = 0
faturamento = 0
for matricula in matriculas:
    quantidade = quantidade + 1
    faturamento = faturamento + matricula['preco']
print(f"Matrículas: {quantidade}")
print(f"Faturamento: R$ {faturamento:.2f}")
