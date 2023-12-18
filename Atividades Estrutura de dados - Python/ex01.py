valores = []

for indice in range (10):
    valor = int(input(f"Digite o {indice + 1}º valor"))
    valores.append(valor)

for valor in valores:
    print(valor)


for i in range(10):
    print(valores[i])

for i in range (10):
    if i % 2 == 0:
        print(valores[i])