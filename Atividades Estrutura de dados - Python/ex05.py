import random

vet =[]
vet_invertido = []
for i in range (30):
    vet.append(random.randint(1,10))

print(f"Vetor normal = {vet}")


i = 0
aux = []
for i in range (29,-1,-1):
    vet_invertido.append(vet[i])


print(f"Vetor Invetido = {vet_invertido}")