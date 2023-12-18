import random
mat = []
maior_media = 0
maior_media_matricula = 0

for linha in range(10):
    aux = []
    media = 0
    for coluna1 in range(1):
        aux.append(int(input(f"Qual a matricula do {linha+1}º aluno: ")))
        for coluna in range(1,5,1):
            aux.append(int(input(f"Qual a {coluna}º nota do aluno: ")))
        media = (aux[1] + aux[2] + aux[3] + aux[4]) / 4
        aux.append(media)
        print()
    mat.append(aux)
    if media > maior_media:
        maior_media = media
        maior_media_matricula = mat[linha][coluna1]

print(mat)

for linha in range(10):
        print(f"MATRICULA: {mat[linha][0]}    MEDIA: {mat[linha][5]}")

print()

print(f"A matricula com a maior media foi {maior_media_matricula} com a media de notas de {maior_media}")
