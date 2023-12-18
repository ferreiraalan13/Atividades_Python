salario = float(input("Informe o salario do funcionario: "))

if salario <= 600.00:
    aumento = salario * 30 / 100
    salario = salario + aumento
    print(f"O aumento do funcionario é 30% R${aumento}. Novo salario: R${salario:.2f} ")

elif salario >= 600.01 and salario <= 1100.00:
    aumento = salario * 25 / 100
    salario = salario + aumento
    print(f"O aumento do funcionario é 25% R${aumento}. Novo salario: R${salario:.2f} ")

elif salario >= 1100.01 and salario <= 2400.00:
    aumento = salario * 20 / 100
    salario = salario + aumento
    print(f"O aumento do funcionario é 20% R${aumento}. Novo salario: R${salario:.2f} ")

elif salario >= 2400.01 and salario <= 3550.00:
    aumento = salario * 15 / 100
    salario = salario + aumento
    print(f"O aumento do funcionario é 15% R${aumento}. Novo salario: R${salario:.2f}")

elif salario >= 3550.01:
    aumento = salario * 10 / 100
    salario = salario + aumento
    print(f"O aumento do funcionario é 10% R${aumento}. Novo salario: R${salario:.2f} ")


print("FIM DO PROGRAMA")

