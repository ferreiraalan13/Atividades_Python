import random
a = []
b = []
for linha in range(3):
    aux = []
    for coluna in range(4):
        aux.append(int(input(f"Informe o elemento da matriz[{linha},{coluna}]")))
    a.append(aux)

print(a)

for linha in range(3):
    aux = []
    for coluna in range(4):
        aux.append(a[linha][coluna] * 3)
    b.append(aux)

print(b)

