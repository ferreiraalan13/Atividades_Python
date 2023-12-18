multiplo_5 = 0


for i in range(10):
    numero = int(input(f"Digite o {i+1}º valor: "))

    if numero % 5 == 0:
        multiplo_5 = multiplo_5 + 1


print(f"A quantidade de multiplos de 5 foram: {multiplo_5}")