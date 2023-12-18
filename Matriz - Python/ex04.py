import random
mat = []
for linha in range(3):
    aux = []
    for coluna in range(3):
        #aux.append(int(input(f"Informe o elemento da matriz [{linha},{coluna}]")))
        aux.append(random.randint(1, 9))
    mat.append(aux)

print(mat)

soma_par = 0
soma_impar = 0
cont_par = 0
cont_impar = 0

for linha in range(3):
    for coluna in range(3):
        if (linha + coluna) % 2 == 0:
            soma_par = soma_par + mat[linha][coluna]
        else:
            soma_impar = soma_impar + mat[linha][coluna]

for linha in range(3):
    for coluna in range(3):
        if mat[linha][coluna] % 2 == 0:
            cont_par = cont_par + 1
        else:
            cont_impar = cont_impar + 1

print (f"a) A soma dos elementos onde a soma do índice da linha + o índice da coluna é PAR: {soma_par}")
print (f"b) A soma dos elementos onde a soma do índice da linha + o índice da coluna é IMPAR: {soma_impar}")
print(f"c) A quantidade de valores pares na matriz: {cont_par}")
print(f"d) A quantidade de valores ímpares na matriz: {cont_impar}")
