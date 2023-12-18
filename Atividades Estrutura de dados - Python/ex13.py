import random

lista =[]


for i in range (1,16,1):
    #lista.append(int(input(f"DIGITE O {i}º valor para lista: ")))
    lista.append(random.randint(1,9))

print(lista)

valor_procurado = int(input("Qual valor deseja procurar na lista? "))

for i in range (15):
    if valor_procurado == lista[i]:
        print(f"O indice do valor procurado é {i}")