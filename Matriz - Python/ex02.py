"""2) - Desenvolva um algoritmo que leia os elementos de uma matriz inteira de 5 X 5 e imprima a soma dos elementos da matriz."""

import random

mat = []

for linha in range(5):
    aux = []
    for coluna in range(5):
        aux.append(random.randint(1, 1))
    mat.append(aux)

soma_auxiliar = 0
for linha in range(5):
    for coluna in range(5):
        soma_auxiliar = soma_auxiliar + mat[linha][coluna]

print(f"A soma dos elementos da matriz é {soma_auxiliar}")
