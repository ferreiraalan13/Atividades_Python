import random

vet =[]

qtd_pares = 0
lista_pares = []
qtd_impares = 0
lista_impares = []
media_pares = 0
media_impares = 0


for i in range (10):
    vet.append(random.randint(1,10))

for i in range(10):
    if vet[i] % 2 == 0:
        qtd_pares = qtd_pares + 1
        lista_pares.append(vet[i])
    else:
        qtd_impares = qtd_impares + 1
        lista_impares.append(vet[i])


media_pares = sum(lista_pares) / len(lista_pares)
media_impares = sum(lista_impares) / len(lista_impares)

print(f" {vet}")
print()

print(f"A quantidade de números pares = {qtd_pares}")
print(f"Os números pares = {lista_pares}")
print(f"A média dos valores pares = {media_pares:.2f}")

print()

print(f"A quantidade de números impares = {qtd_impares}")
print(f"Os números impares = {lista_impares}")
print(f"A média dos valores impares = {media_impares:.2f}")

print()

print(f"A média da soma dos valores pares mais os valores ímpares = {media_pares + media_impares:.2f}")
