
contador = 1

while contador <= 10:
    nome = input(f"Digite o nome do {contador}º funcionario: ")
    idade = int(input(f"Digite a idade do {contador}º funcionario: "))
    sexo = input(f"Digite o sexo do {contador}º funcionario (M ou F) ")

    if sexo == "M" or sexo == "m":
        if idade >= 30:
            salario = 100
            print(f"Salario liquido: R${salario}")
            print()
        else:
            if idade < 30:
                salario = 50
                print(f"Salario liquido: R${salario}")
                print()

    else:
        if sexo == "F" or sexo == "f":
            if idade >= 30:
                salario = 200
                print(f"Salario liquido: R${salario}")
                print()
            else:
                if idade < 30:
                    salario = 80
                    print(f"Salario liquido: R${salario}")
                    print()

    contador = contador + 1
