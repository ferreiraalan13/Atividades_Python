qtd_dolar = float(input("Informe a quantidade de dolar para realizar a conversao: "))
cotacao_dolar = float(input("Informe a cotacao atual do dolar atual: "))

valor_real = qtd_dolar * cotacao_dolar


print(f"O valor {qtd_dolar} convertido para real é R$ {valor_real:.2f}")