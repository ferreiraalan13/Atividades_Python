import random

lista_A =[]
lista_B = []
lista_C = []


for i in range (1,11,1):
    #lista_A.append(int(input(f"DIGITE O {i}º valor para lista A: ")))
    lista_A.append(random.randint(1,9))

for i in range (1,11,1):
    #lista_B.append(int(input(f"DIGITE O {i}º valor para lista B: ")))
    lista_B.append(random.randint(1,9))



for i in range(10):
    lista_C.append(lista_A[i] + lista_B[i])

print(f"LISTA A = {lista_A}")
print(f"LISTA B = {lista_B}")
print(f"LISTA C = {lista_C}")