import random

num = []

for indice in range (15):
    numero = int(input(f"Digite o {indice +1}º numero: "))
    num.append(numero)



for i in range(15):
    if num[i] % 2 == 0:
        print(f"{num[i]} = PAR")
    else:
        print(f"{num[i]} = IMPAR")