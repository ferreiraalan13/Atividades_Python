gabarito = []

for i in range(30):
    gabarito.append(input(f"Informe a resposta da {i+1}º questão: "))

qtd_alunos = int(input("Informe a quantidade de alunos que fizeram a prova: "))

respostas = []

for i in range(qtd_alunos):
    aux_notas = []
    acertos = 0
    for c in range(30):
        aux_notas.append(input(f"Informe a {c+1}º resposta do {i+1}º aluno: "))
        if aux_notas[c] == gabarito[c]:
            acertos = acertos + 1
    print("-" * 50)
    print(f"GABARITO DO {i+1}º ALUNO CONFERIDO")
    print("-" * 50)
    aux_notas.append(acertos)
    respostas.append(aux_notas)

for i in range(qtd_alunos):
    print(f"{i+1}º ALUNO - NOTA = {respostas[i][30]}")



