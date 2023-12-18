
contador = 1

while contador <= 3:
    tipo_cliente = input("Informe qual o tipo de cliente: (Residencia, Comercio  ou Industria): ")
    total_kw = float(input("Informe quantos KW/h foram gastos pelo cliente no mes: "))

    if tipo_cliente == "residencia":
        pagamento = (total_kw * 0.60)
        print(f"O valor a ser pago  da conta de luz é R${pagamento}")
    else:
        if tipo_cliente == "comercio":
            pagamento = (total_kw * 0.48)
            print(f"O valor a ser pago  da conta de luz é R${pagamento}")
        else:
            if tipo_cliente == "industria":
                pagamento = (total_kw * 1.29)
                print(f"O valor a ser pago  da conta de luz é R${pagamento}")

