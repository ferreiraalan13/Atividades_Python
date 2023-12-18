def calcula_novo_salario(salario_atual):
    return salario_atual + (salario_atual * 15 / 100)


for i in range(1, 11, 1):
    salario = float(input(f"Informe o salario do {i}º funcionario: "))
    print(f"O novo salario do funcionario é: R${calcula_novo_salario(salario):.2f}")
    print()
