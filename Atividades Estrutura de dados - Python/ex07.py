
lista = []

for i in range(1,6,1):
    aux = int(input(f"Digite o {i}º numero: "))
    if aux in lista:
        print("VALOR JA CADASTRADO")
    else:
        lista.append(aux)

print(f"VALORES CADASTRADOS {lista}")