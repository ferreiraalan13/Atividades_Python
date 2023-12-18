
continuar = True

while continuar == True:
    numero = int(input("Informe um numero"))
    if numero > 80:
        print("Numero maior que 80")
    else:
        if numero < 25:
            print("Numero menor que 25")
        else:
            if numero == 40:
                print("Numero igual a 40")

    resposta = input("Deseja digitar outro valor? (sim ou nao)")
    if resposta == "nao":
        continuar = False


print("FIM DO PROGRAMA")