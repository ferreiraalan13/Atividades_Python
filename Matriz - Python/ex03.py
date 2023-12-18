import random

mat = []

for linha in range(8):
    aux = []
    for coluna in range(8):
        #aux.append(int(input(f"Informe o elemento da matriz [{linha},{coluna}]")))
        aux.append(random.randint(1, 1))
    mat.append(aux)

soma_auxiliar = 0

for linha in range(8):
    for coluna in range(8):
        soma_auxiliar = soma_auxiliar + mat[linha][coluna]

print(f"a) A soma dos elementos da matriz é {soma_auxiliar}")

soma_par = 0
soma_impar = 0
for linha in range(8):
    for coluna in range(8):
        if mat[linha][coluna] % 2 == 0:
            soma_par = soma_par + mat[linha][coluna]
        else:
            soma_impar = soma_impar + mat[linha][coluna]
print(f"b) A soma dos elementos PARES da matriz é {soma_par}")
print(f"c) A soma dos elementos IMPARES da matriz é {soma_impar}")


