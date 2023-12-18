nome = 0

salario: 0
total_vendas = 0
comissao = 0
salario_total = 0

nome = input("Informe o nome completo do funcionario :")
salario = float(input("Informe o salario do funcionario: "))
total_vendas = float(input("Informe o total de vendas em R$ do mês: "))

comissao = total_vendas * 0.15
salario_total = comissao + salario

print(f"NOME DO FUNCIONARIO: {nome} ")
print(f"SALARIO FIXO: {salario}")
print(f"SALARIO FINAL COM COMISSÃO: {salario_total:.2f} ")
