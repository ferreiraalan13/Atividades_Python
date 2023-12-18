import random

vetor =[]

invertido = []

for i in range (20):
    #vetor.append(int(input(f"DIGITE O {i+1}º valor para lista: ")))
    vetor.append(random.randint(1,9))

for a in range(19,-1,-1):
    invertido.append(vetor[a])

print(vetor)

print(invertido)