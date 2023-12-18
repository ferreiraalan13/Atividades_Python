#FUNCOES

def calcula_operacoes(valor1: float, valor2: float, operacao: int):
    """
    :autor: Alan Ferreira
    :param valor1:  Primeiro valor para realizar a operacao informada
    :param valor2: Segundo valor para realizar a operacao informada
    :param operacao: Valor da operacao a ser realizada [+-/*]
    :return: Resultado da operacao escolhida.
    """
    if operacao == 1:
        return valor1 + valor2
    elif operacao == 2:
        return valor1 + valor2
    elif operacao == 3:
        return valor1 * valor2
    elif operacao == 4:
        return valor1 / valor2







#PROGRAMA PRINCIPAL

continuar = True
while continuar:
    print("""=====CALCULADORA=====
    = 1 - Somar         =
    = 2 - Subtrair      =
    = 3 - multiplicar   =
    = 4 - Dividir       =
    = 5 - Sair          =
    =====================""")

    operacao = int(input("Informe a operacao: "))



    if operacao >= 1 and operacao <= 4:
        valor1 = float(input("Informe um valor: "))
        valor2 = float(input("Informe outro valor"))
        resultado = calcula_operacoes(valor1, valor2, operacao)
        print("=" * 30)
        print(f"O resultado da operacao é: {resultado}")

    elif operacao == 5:
        continuar = False

    else:
        print(f"OPERACAO {operacao} INVALIDA")
        print("=" * 30)

