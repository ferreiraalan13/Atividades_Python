"""1) - Criar um algoritmo que leia os elementos de uma matriz inteira de 5 X 5 e imprima a matriz (em forma de matriz)."""

import random

mat = []

for linha in range(5):
    aux = []
    for coluna in range(5):
        #aux.append(int(input(f"Informe o elemento [{linha} , {coluna}] = ")))
        aux.append(random.randint(10,99))
    mat.append(aux)

for linha in range(5):
    for coluna in range(5):
        print(mat[linha][coluna], end=" ")
    print("")


