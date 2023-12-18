contador = 1


while contador <= 50:
    nivel = int(input("Informe o nivel do professor (1 a 3): "))
    horas = float(input("Informe quantas horas o professor trabalhou: "))

    if nivel == 1:
        salario = 12 * horas
        print(f"O salario do professor é R${salario}")
        print()
        contador = contador + 1
    else:
        if nivel == 2:
            salario = 17 * horas
            print(f"O salario do professor é R${salario}")
            print()
            contador = contador + 1
        else:
            if nivel == 3:
                salario = 25 * horas
                print(f"O salario do professor é R${salario}")
                print()
                contador = contador + 1