def soma_exibe_vetor(vetor):
    soma = 0
    for valor in vetor:
        soma = soma + valor
    print(f"A soma dos elementos do vetor é {soma}")


def maior_elemento(vetor):
    maior_elemento = vetor[0]
    for valor in vetor:
        if valor > maior_elemento:
            maior_elemento = valor
    print(f"O maior elemento é: {maior_elemento}")


def exibe_menor_elemento(vetor):
    menor_elemento = vetor[0]
    for valor in vetor:
        if valor < menor_elemento:
            menor_elemento = valor
    print(f"O menor elemento é: {menor_elemento}")


def exibe_ocorrencias_primeiro_elemento(vetor):
    qtd_ocorrencia = 0
    for valor in vetor:
        if valor == vetor[0]:
            qtd_ocorrencia = qtd_ocorrencia + 1

    print(f"A quantidade de ocorrencia do primeiro elemento {vetor[0]} é: {qtd_ocorrencia}")


def exibe_media_vetor(vetor):
    soma = 0
    for valor in vetor:
        soma = soma + valor
    media = soma / len(vetor)
    print(f"a media é igual a {media}")


def exibe_valores_pares(vetor):
    qtd_pares = 0
    for valor in vetor:
        if valor % 2 == 0:
            qtd_pares = qtd_pares + 1

    print(f"A quantidade de valores pares é: {qtd_pares}")

def exibe_valores_impares(vetor):
    qtd_impares = 0
    for valor in vetor:
        if valor % 2 != 0:
            qtd_impares = qtd_impares + 1

    print(f"A quantidade de valores IMPARES é: {qtd_impares}")


def soma_valores_pares(vetor):
    soma_pares = 0
    for valor in vetor:
        if valor % 2 == 0:
            soma_pares = soma_pares + valor

    print(f"A soma dos valores pares é: {soma_pares}")

def soma_valores_impares(vetor):
    soma_impares = 0
    for valor in vetor:
        if valor % 2 != 0:
            soma_impares = soma_impares + valor

    print(f"A soma dos valores impares é: {soma_impares}")


vet = []
for i in range(1, 11, 1):
    vet.append(int(input(f"Informe o {i}º valor: ")))

print(vet)

print()

soma_exibe_vetor(vet)
maior_elemento(vet)
exibe_menor_elemento(vet)
exibe_ocorrencias_primeiro_elemento(vet)
exibe_media_vetor(vet)
exibe_valores_pares(vet)
exibe_valores_impares(vet)
soma_valores_pares(vet)
soma_valores_impares(vet)