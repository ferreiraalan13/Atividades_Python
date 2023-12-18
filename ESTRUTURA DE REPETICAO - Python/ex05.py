
reajuste = 0
contador = 1
contador_reajuste = 0

while contador <= 584:
    nome = input("Digite o nome do funcionario: ")
    salario = float(input("Digite o salario do funcionario: "))

    salario_minimo = float(input("Digite o salario minimo atual: "))

    print()

    if salario < (salario_minimo * 3):
        reajuste = salario * 50 / 100
        salario_final = reajuste + salario
        contador_reajuste = contador_reajuste + reajuste
    else:
        if salario >= (salario_minimo * 3) and salario <= (salario_minimo * 10):
            reajuste = salario * 20 / 100
            salario_final = reajuste + salario
            contador_reajuste = contador_reajuste + reajuste

        else:
            if salario > (salario_minimo * 10) and salario <= (salario_minimo * 20):
                reajuste = salario * 15 / 100
                salario_final = reajuste + salario
                contador_reajuste = contador_reajuste + reajuste
            else:
                if salario > (salario_minimo * 20):
                    reajuste = salario * 10 / 100
                    salario_final = reajuste + salario
                    contador_reajuste = contador_reajuste + reajuste

    contador = contador + 1

    print(f"Nome do funcionario: {nome} ")
    print(f"O valor do reajuste foi: R${reajuste}")
    print(f"O novo salario é de: R${salario_final}")
    print()

print(f"A empresa aumentou sua folha de pagamento em R${contador_reajuste}")