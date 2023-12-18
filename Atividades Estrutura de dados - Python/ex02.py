nomes = []

for indice in range(1, 11, 1):
    nome = input(f"Digite o {indice}º nome: ")
    nomes.append(nome)


for i in range(10):
    print(f"{i+1}º {nomes[i]}")