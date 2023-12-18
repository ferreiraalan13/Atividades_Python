resposta = True
valor = []
valorb = []
while resposta == True:
    valor.append(int(input("Digite um valor para o Vetor A")))
    resposta1 = input("Deseja digitar outro valor? (S ou N)")
    if resposta1 == "N" or resposta1 == "n":
        resposta = False

    print(f"VETOR A = {valor}")
