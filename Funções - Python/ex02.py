def exibe_valores_pares_vetor(vet):
    print("Elementos do vetor Par")
    for i in range(0,10,1):
        if vet[i] % 2 == 0:
            print(f"Indice = {i} valor = {vet[i]}")

def exibe_valores_impares_vetor(vet):
    print("Elementos do vetor Par")
    for i in range(0,10,1):
        if vet[i] % 2 != 0:
            print(f"Indice = {i} valor = {vet[i]}")

def retorna_soma_dos_elementos_vetor(vet):
    soma = 0
    for valor in vet:
        soma = soma + valor
    return soma

vetor = []

for valor in range (1,11,1):
    vetor.append(int(input(f"Digite o {valor}º elemento do vetor: ")))


print("=" * 30)


exibe_valores_pares_vetor(vetor)

print("=" * 30)


exibe_valores_impares_vetor(vetor)

print("=" * 30)

soma = retorna_soma_dos_elementos_vetor(vetor)
print(f"A soma dos elementos do vetor é {soma}")