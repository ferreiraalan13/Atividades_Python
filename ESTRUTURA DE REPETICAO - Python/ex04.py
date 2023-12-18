contador = 1
qtd_positivo = 0
qtd_negativo = 0
qtd_zero = 0

while contador <= 5:
    numero = int(input(f"Digite o {contador}o numero: "))
    if numero < 0:
        qtd_negativo = qtd_negativo + 1
    else:
        if numero == 0:
            qtd_zero = qtd_zero + 1
        else:
            if numero > 0:
                qtd_positivo = qtd_positivo + 1

    contador = contador + 1


print(f"POSITIVOS: {qtd_positivo}")
print(f"ZEROS: {qtd_zero}")
print(f"NEGATIVOS: {qtd_negativo}")