#06) - A concessionária de veículos “CARANGO VELHO” está vendendo os seus veículos com desconto.
# Faça um algoritmo que calcule e exiba o valor do desconto e o valor a ser pago pelo cliente de vários carros.
# O desconto deverá ser calculado de acordo com o ano do veículo.
# Até 2000 - 12% e acima de 2000 - 7%.
# O sistema deverá perguntar se o usuário deseja continuar calculando desconto até que a resposta seja: “(N) Não”.
# Informar total de carros com ano até 2000 e total geral.

contador = True
contador_2000 = 0
contador_geral = 0
contador_desconto = 0


while contador == True:
    ano_veiculo = int(input("Digite o ano do veiculo: "))
    valor_veiculo = float(input("Digite o valor do veiculo: "))
    print()
    if ano_veiculo <= 2000:
        desconto = valor_veiculo * 12 / 100
        valor_final = valor_veiculo - desconto
        contador_2000 = contador_2000 + 1
        contador_geral = contador_geral + 1
        contador_desconto = contador_desconto + desconto

    else:
        if ano_veiculo > 2000:
            desconto = valor_veiculo * 7 / 100
            valor_final = valor_veiculo - desconto
            contador_geral = contador_geral + 1
            contador_desconto = contador_desconto + desconto

    print(f"Valor do veiculo: R${valor_veiculo}")
    print(f"Aplicado desconto de: R${desconto}")
    print(f"Valor a ser pago: R${valor_final}")
    print()

    resposta = input("Deseja calcular o desconto de outro veiculo? ( S ou N )")
    if resposta == "N" or resposta == "n":
        contador = False

print(f"Total de carros = {contador_geral}")
print(f"Total de carros até ano 2000 = {contador_2000}")
print(f"Total de descontos: R${contador_desconto}")
