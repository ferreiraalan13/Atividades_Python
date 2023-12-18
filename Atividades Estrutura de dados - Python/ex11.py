import random

vet =[]
maior_valor = 0


for i in range (10):
    #vet.append(int(input(f"DIGITE O {i}º valor para a lista: ")))
    vet.append(random.randint(1,100))
    maior_valor = vet[0]

for i in range(10):
    if vet[i] > maior_valor:
        maior_valor = vet[i]

print(vet)
print(f"O maior valor digitado pelo usuario é: {maior_valor}")
