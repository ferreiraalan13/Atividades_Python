contador = 1
qtd_valor_no_intervalo = 0

while contador <= 80:
    numero = int(input("Informe um numero qualquer "))
    if numero >= 10 and numero <= 150:
        qtd_valor_no_intervalo = qtd_valor_no_intervalo + 1

    contador = contador + 1

print(f"A quantidade de numeros entre 10 e 150 foi de {qtd_valor_no_intervalo}")