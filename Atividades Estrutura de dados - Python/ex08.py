import random

vet =[]


lista_pares = []

lista_impares = []


for i in range (10):
    vet.append(random.randint(1,10))

for i in range(10):
    if vet[i] % 2 == 0:
        lista_pares.append(vet[i])
    else:
        lista_impares.append(vet[i])


print(f"LISTA COMPLETA = {vet}")
print(f"LISTA PARES = {lista_pares}")
print(f"LISTA IMPARES = {lista_impares}")
