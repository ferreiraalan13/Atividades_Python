contador = 0
inicial = int(input("Digite o valor inicial: "))
final = int(input("Digite o valor final: "))
contador_pares = 0
contador_impar = 0

while inicial <= final:
    if inicial % 2 == 0:
        contador_pares = inicial
        inicial = inicial + 1
    else:
        contador_impar = inicial

        inicial = inicial + 1


print(f"Total pares = {contador_pares}")
print(f"Total impares = {contador_impar}")