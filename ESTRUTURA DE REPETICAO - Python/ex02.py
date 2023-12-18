contador = True
qtd_apto = 0
qtd_nao_apto = 0
while contador == True:
    nome = input("Digite o nome da pessoa: ")
    sexo = input("Digite o sexo: ")
    idade = int(input("Digite a idade: "))
    saude = input("Informe a saude: (ok) ou (ruim) ")

    if sexo.upper() == "MASCULINO" and idade >= 18 and saude.upper() == "OK":
        qtd_apto = qtd_apto + 1
    else:
        print("Não esta apto ")
        qtd_nao_apto = qtd_nao_apto + 1

    stop = input("Deseja consultar outra pessoa? (sim ou nao) ")
    if stop.upper() == "NAO":
        contador = False

print(f"O total de pessoas aptas a alistamento é: {qtd_apto}")
print(f"O total de pessoas NAO aptas a alistamento é: {qtd_nao_apto}")