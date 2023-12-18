import random

vet =[]
menor_valor = 0


for i in range (10):
    #vet.append(int(input(f"DIGITE O {i}º valor para a lista: ")))
    vet.append(random.randint(1,100))
    menor_valor = vet[0]

for i in range(10):
    if vet[i] < menor_valor:
        menor_valor = vet[i]

print(vet)
print(f"O menor valor digitado pelo usuario é: {menor_valor}")
