import random

lista_alunos = []
lista_nota = []
for i in range(1,4,1):
    lista_alunos.append(input(f"Digite o nome do {i}º aluno: "))

for i in range(3):
    lista_nota.append(int(input(f"Digite a nota do ({lista_alunos[i]}): ")))



aluno_procurado = input("Deseja pesquisar a nota de qual aluno? ")

if aluno_procurado in lista_alunos:
    indice = lista_alunos.index(aluno_procurado)
    nota_aluno = lista_nota[indice]
    print(f"Aluno: {aluno_procurado}")
    print(f"Nota: {nota_aluno}")
else:
    print("Aluno não cadastrado.")